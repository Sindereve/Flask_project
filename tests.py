import os
os.environ['DATABASE_URL'] = 'sqlite://'

import json
import base64
from datetime import datetime, timezone, timedelta
import unittest
from app import app, db
from app.models import User, Post

class UserModelCase(unittest.TestCase):
    def setUp(self):
        """Настройка перед каждым тестом"""
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'  # Используем БД в памяти
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """Очистка после теста"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        """"Правильная установка пароля и считывание"""
        u = User(username='Boris', email='boriska14@email.com')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

    def test_avatar(self):
        """"Работоспособность аватарок"""
        u = User(username='john', email='john@example.com')
        self.assertEqual(u.avatar(128), ('https://www.gravatar.com/avatar/d4c74594d841139328695756648b6bd6?d=retro&s=128'))
        
    def test_follow(self):
        """Работоспособность подписок"""
        u1 = User(username='Boris', email='boriska14@email.com')
        u2 = User(username='Alina', email='alinnnna@email.com')
        
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()

        following = db.session.scalars(u1.following.select()).all()
        followers = db.session.scalars(u1.followers.select()).all()
        self.assertEqual(following, [])
        self.assertEqual(followers, [])

        u1.follow(u2)
        db.session.commit()
        self.assertTrue(u1.is_following(u2))
        self.assertEqual(u1.following_count(), 1)
        self.assertEqual(u2.followers_count(), 1)
        u1_folowing = db.session.scalars(u1.following.select()).all()
        u2_folowers = db.session.scalars(u2.followers.select()).all()
        self.assertEqual(u1_folowing[0].username, 'Alina')
        self.assertEqual(u2_folowers[0].username, 'Boris')

        u1.unfollow(u2)
        db.session.commit()
        self.assertEqual(u1.following_count(), 0)
        self.assertEqual(u2.followers_count(), 0)

    def test_follow_posts(self):
        """Успешное получение постов от кураторов"""
        u1 = User(username='Ivan', email='ivanitin@email.com')
        u2 = User(username='Peter', email='petr12@email.com')
        u3 = User(username='Nikita', email='nikitka@email.com')
        u4 = User(username='Olya', email='olya88@email.com')
 
        db.session.add_all([u1, u2, u3, u4])

        now = datetime.now(timezone.utc)
        p1 = Post(body="post from ivan", author=u1,
                  timestamp=now + timedelta(seconds=1))
        p2 = Post(body="post from peter", author=u2,
                  timestamp=now + timedelta(seconds=4))
        p3 = Post(body="post fromnikita", author=u3,
                  timestamp=now + timedelta(seconds=3))
        p4 = Post(body="post from olya", author=u4,
                  timestamp=now + timedelta(seconds=2))

        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()
 
        u1.follow(u2)  
        u1.follow(u4)  
        u2.follow(u3)  
        u3.follow(u4)  

        db.session.commit()

        f1 = db.session.scalars(u1.following_posts()).all()
        f2 = db.session.scalars(u2.following_posts()).all()
        f3 = db.session.scalars(u3.following_posts()).all()
        f4 = db.session.scalars(u4.following_posts()).all()
        self.assertEqual(f1, [p2, p4, p1])
        self.assertEqual(f2, [p2, p3])
        self.assertEqual(f3, [p3, p4])
        self.assertEqual(f4, [p4])


class APITestCase(unittest.TestCase):
    def setUp(self):
        """Настройка перед каждым тестом"""
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'  # БД в памяти
        self.client = self.app.test_client()

        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()

        # Создаем тестового пользователя
        self.user = User(username='sindik', email='sindik@example.com')
        self.user.set_password('1861')
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        """Очистка после теста"""
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def get_token(self):
        """Получает токен через Basic Auth"""
        auth_header = 'Basic ' + base64.b64encode(b'sindik:1861').decode('utf-8')
        response = self.client.post('/api/tokens', headers={'Authorization': auth_header})
        self.assertEqual(response.status_code, 200)
        return response.get_json()['token']

    def test_get_token_success(self):
        """Успешное получение токена"""
        token = self.get_token()
        self.assertTrue(token)

    def test_get_token_invalid_credentials(self):
        """Ошибка при неверных учетных данных"""
        auth_header = 'Basic ' + base64.b64encode(b'wrong:wrong').decode('utf-8')
        response = self.client.post('/api/tokens', headers={'Authorization': auth_header})
        self.assertEqual(response.status_code, 401)

    def test_delete_token(self):
        """Успешный отзыв токена"""
        token = self.get_token()
        headers = {'Authorization': f'Bearer {token}'}
        response = self.client.delete('/api/tokens', headers=headers)
        self.assertEqual(response.status_code, 204)

        # Проверяем, что нельзя удалить уже отозванный токен
        response = self.client.delete('/api/tokens', headers=headers)
        self.assertEqual(response.status_code, 401)

    def test_get_user_profile(self):
        """Получение профиля пользователя с токеном"""
        token = self.get_token()
        headers = {'Authorization': f'Bearer {token}'}
        response = self.client.get('/api/users/1', headers=headers)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['username'], 'sindik')

    def test_get_user_unauthorized(self):
        """Ошибка при отсутствии токена"""
        response = self.client.get('/api/users/1')
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main(verbosity=2)