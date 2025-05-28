from datetime import datetime, timezone
from app import db
from app.models import User, Post, Image


def seed_database(data, drop = False):

    if drop:
        db.drop_all()
        db.create_all()
        print('+ Delet all data')
    else:
        print('- Delet all data')

    username_to_user = {}

    # пользователи
    for user_data in data['users']:
        username = user_data['username']
        existing_user = User.query.filter_by(username=username).first()
        if not existing_user:
            user = User(
                username=username,
                email=user_data['email'],
                about_me=user_data.get('about_me', '')
            )
            user.set_password(user_data['password'])
            db.session.add(user)
            db.session.flush()
            username_to_user[username] = user
        else:
            username_to_user[username] = existing_user

    db.session.commit()
    print("+ Users added")

    # подписки
    for follow_data in data['follows']:
        follower_name = follow_data['follower']
        followed_name = follow_data['followed']

        follower = username_to_user.get(follower_name)
        followed = username_to_user.get(followed_name)

        if follower and followed:
            if not follower.is_following(followed):
                follower.follow(followed)

    db.session.commit()
    print("+ Subscriptions added")

    # создание постов
    for post_data in data['posts']:
        author_username = post_data['username']
        author = username_to_user.get(author_username)
        if not author:
            continue

        existing_post = Post.query.filter_by(title=post_data['title'], author=author).first()
        if existing_post:
            continue

        post = Post(
            title=post_data['title'],
            body=post_data['body'],
            timestamp=datetime.now(timezone.utc),
            author=author
        )
        db.session.add(post)
        db.session.flush()

        # картинки 
        for image_data in post_data.get('images', []):
            image = Image(
                url=image_data['url'],
                caption=image_data.get('caption', ''),
                position=0,
                post=post
            )
            db.session.add(image)

    db.session.commit()
    print("+ Posts and images added")

