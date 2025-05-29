from flask import render_template, flash, redirect, url_for, request, g, jsonify, session
from flask_login import current_user, login_user, logout_user, login_required
from flask_babel import _, get_locale
from urllib.parse import urlsplit
import sqlalchemy as sa
from datetime import datetime, timezone
from app import app, db, photos
from app.models import User, Post, Image
from app.forms import LoginForm, RegistrationForm, EditProfileForm, EmptyForm, PostForm

@app.context_processor
def inject_timezone():
    return dict(timezone=timezone, datetime=datetime)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    posts = db.paginate(current_user.following_posts(), page=page, 
                        per_page=app.config['POSTS_PER_PAGE'], error_out=False)

    next_url = url_for('index', page=posts.next_num) if posts.has_next else None
    prev_url = url_for('index', page=posts.prev_num) if posts.has_prev else None
    return  render_template('index.html', title='Home', posts=posts.items,
                            prev_url=prev_url, next_url=next_url)

@app.route('/explore')
@login_required
def explore():
    page = request.args.get('page', 1, type=int)
    query = sa.select(Post).order_by(Post.timestamp.desc())
    posts = db.paginate(query, page=page, per_page=app.config['POSTS_PER_PAGE'], error_out=False)

    next_url = url_for('explore', page=posts.next_num) if posts.has_next else None
    prev_url = url_for('explore', page=posts.prev_num) if posts.has_prev else None
    return render_template('index.html', title='Explore', posts=posts.items, 
                           prev_url=prev_url, next_url=next_url)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data)
        )
        if user is None or not user.check_password(form.password.data):
            flash(_('Invalid username or password'))
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(_('You are a registered user!'))
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form = form)

@app.route('/user/<username>')
@login_required
def user(username):
    user = db.first_or_404(sa.select(User).where(User.username == username))
    page = request.args.get('page', 1, type=int)
    query = user.posts.select().order_by(Post.timestamp.desc())
    posts = db.paginate(query, page=page, per_page=app.config['POSTS_PER_PAGE'], error_out=False)

    next_url = url_for('user', username=user.username, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('user', username=user.username, page=posts.prev_num) \
        if posts.has_prev else None

    form = EmptyForm()
    return render_template('user.html', user=user, posts=posts, form=form,
                           next_url=next_url, prev_url=prev_url)

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now(timezone.utc)
        db.session.commit()
        g.locale = str(get_locale())


@app.route('/profile/generate-token', methods=['POST'])
@login_required
def generate_api_token():
    token = current_user.get_token()
    db.session.commit()
    flash(_('Create token.'))
    return redirect(url_for('user', username=current_user.username))

@app.route('/profile/revoke-token', methods=['POST'])
@login_required
def revoke_api_token():
    current_user.revoke_token()
    db.session.commit()
    flash(_('Token revoked.'))
    return redirect(url_for('user', username=current_user.username))


@app.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            body=form.body.data,
            author=current_user
        )
        db.session.add(post)
        db.session.flush()  

        if form.image.data:
            filename = photos.save(form.image.data)
            url = f"/static/images/{filename}"
            image = Image(url=url, caption=filename, post=post)
            db.session.add(image)
        elif form.image_url.data:
            image = Image(url=form.image_url.data, caption=form.image_url.data, post=post)
            db.session.add(image)

        db.session.commit()
        flash(_('Post created successfully!'), 'success')
        return redirect(url_for('index'))

    return render_template('new_post.html', form=form)

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash(_('Your changes have been saved.'))
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile', form=form)

@app.route('/follow/<username>', methods=['POST'])
@login_required
def follow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(User).where(User.username == username))
        if user is None:
            flash(_('User %(username)s not found.', username=username))
            return redirect(url_for('index'))
        if user == current_user:
            flash(_('You cannot follow yourself!'))
            return redirect(url_for('user', username=username))
        current_user.follow(user)
        db.session.commit()
        flash(_('You are following %(username)s!', username=username))
        return redirect(url_for('user', username=username))
    else:
        return redirect(url_for('index'))
    
@app.route('/unfollow/<username>', methods=['POST'])
@login_required
def unfollow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(User).where(User.username == username))
        if user is None:
            flash(_('User %(username)s not found.'))
            return redirect(url_for('index'))
        if user == current_user:
            flash(_('You cannot unfollow yourself!'))
            return redirect(url_for('user', username=username))
        current_user.unfollow(user)
        db.session.commit()
        flash(_('You are unfollowing %(username)s!', username=username))
        return redirect(url_for('user', username=username))
    else:
        return redirect(url_for('index'))
    

@app.route('/set-lang/<lang>')
def set_language(lang):
    if lang in app.config['LANGUAGES']:
        session['language'] = lang
    resp = redirect(request.referrer or url_for('index'))
    resp.set_cookie('language', lang, max_age=60*60*24*30)  # 30 дней
    return resp

@app.context_processor
def inject_lang():
    return {
        'current_lang': session.get('language', 'en')
    }

