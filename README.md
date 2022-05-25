# Django JWT authentication with simple jwt (Refresh and Access tokens)

This is a boiler plate code to get started with Django authentication.
This project can be used in 2 ways:

1. Using this project as boiler plate code to get started with your project. It has **users** app already integrated which has JWT authentication configured with main project.

2. Take **users** app from this project, then plug and play it with your project.

## Running the application

### 1. Using this project as boiler plate code.

1. Clone this repository.

2. Create a virtual environment inside root of the project.

```console
$ python -m venv .venv
```

(Make sure you have pyenv installed)

3. Activate virtual environment

```console
$ source .venv/bin/activate
```

For later if you want to exit virtual env `$ deactivate`

4. Install dependencies from requirements.txt

```console
$ pip install -r requirements.txt
```

upgrade the pip if you are asked to in terminal.

5. Make migrations and run server

```console
$ python manage.py makemigrations
$ python manage.py migrate --run-syncdb
$ python manage.py runserver
```

### 2. Plug and play "users" app

1. Copy **users** folder from this project and paste it in root of your own project.

2. Install the following libraries:

```console
$ pip install djangorestframework
$ pip install djangorestframework-simplejwt
```

3. In project's main app's urls.py file add:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    ...
]
```

4. In settings.py of project's main app, add following:

```python
INSTALLED_APPS = [
    ...
    # These needs to be added
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'users'
]

DATABASES={...}
...
# This needs to be added
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
...

DEFAULT_AUTO_FIELD = ...
# This needs to be added
AUTH_USER_MODEL = 'users.User'
```

5. Now you can make migrations and run the app.

## Endpoints available

### 1. User signup

**POST** `/auth/register`

> This request **doesn't need** authorization header.

Creates new user.
Body data:

```js
{
   "first_name": "ऋषभ",
   "last_name": "बहल",
   "username": "abc",
   "email": "abc@xyz.com",
   "password": "abc123"
}
```

Request response:

```js
{
   "id": 47,
   "first_name": "ऋषभ",
   "last_name": "बहल",
   "username": "abc",
   "email": "abc@xyz.com",
}
```

### 2. User login

**POST** `/auth/token/`

> This request **doesn't need** authorization header.

Body data:

```js
{
   "email": "abc@xyz.com",
   "password": "abc123"
}
```

Request response:

```js
{
   "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1MzUwNjYyNiwiaWF0IjoxNjUzNDIwMjI2LCJqdGkiOiI0YTViMWM1NmY4ZWM0MjdiODRjMjZiZmU1MTljZDI1YyIsInVzZXJfaWQiOjJ9.b4dFB9EXDVzVk_PC_-YRLkqAHNkYSUXH16PO4FhIErg",
   "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUzNDIwNTI2LCJpYXQiOjE2NTM0MjAyMjYsImp0aSI6IjRjZWNiOWFmNTRhNDRkYTE4NzE5ODgyNGFlYmE4ZWE0IiwidXNlcl9pZCI6Mn0.Zm8-iER46HtSlSfJf2Sz6cew2Jagj1OC1kC1rznm_mE"
}
```
### 3. User token from refresh token

**POST** `/auth/token/refresh/`

> This request **doesn't need** authorization header.

Body data:

```js
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1MzQ2MjIwMiwiaWF0IjoxNjUzMzc1ODAyLCJqdGkiOiIzYzVhYWI3ZGM3MTc0ZWRhYmI0MzM3ZGU0OGJiMGYxOCIsInVzZXJfaWQiOjJ9.slznJK7HmcFVu0nYmfgGHhqsuEZxOOFbmgvHmKJP81s"
}
```

Request response:

```js
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUzNDIwODIwLCJpYXQiOjE2NTM0MjA1MDcsImp0aSI6IjBlNzk1NDA0YWVkZDRhZTI5ZjEyYjA0MTQwYWQ3YzkzIiwidXNlcl9pZCI6Mn0.HbaNex9mBflz7XrAJcZ3tqdl6ikZlxb47eueOz29f3U"
}
```
### 4. Get logged in user details from authentication token

**GET** `/auth/user`

> This request **needs** to have authorization header.

Body data: None

Request response:

```js
{
   "id": 47,
   "first_name": "ऋषभ",
   "last_name": "बहल",
   "username": "abc",
   "email": "abc@xyz.com",
}
```
### 5. Test to see if protected routes are working

**GET** `/auth/test`

> This request **needs** to have authorization header.

Body data: None

Request response:

```js
{
    "message": "Test, Successful"
}
```
### 6. Logout user

**POST** `/auth/logout`

> This request **needs** to have authorization header.

Body data: 
```js
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1MzQ2MjQ3OSwiaWF0IjoxNjUzMzc2MDc5LCJqdGkiOiJjYjA1OWYwNWY1YmY0OWM3OTNiMjc2NzhjMTNhZWQ1NSIsInVzZXJfaWQiOjJ9.x303spZ5d7Nd_kE2rCJS8okOsUnQdMV00afNQDlM7xY"
}
```

Request response: None (Status 205)

> Logout end point blacklists the refresh token. Now this refresh token can't be used again.

> The blacklist app also provides a management command, `flushexpiredtokens`, which will delete any tokens from the outstanding list and blacklist that have expired. You should set up a cron job on your server or hosting platform which runs this command daily.

## How to authenticate rest of the routes in app?

In the endpoint definition in **views.py** add the following:
```python
...
# Add below line
from rest_framework.permissions import IsAuthenticated
...

class TestView(APIView):
    # Add below line
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        content = {'message': 'Test, Successful'}
        return Response(content)

```

## References
1. https://django-rest-framework-simplejwt.readthedocs.io/en/latest/
2. https://medium.com/django-rest/logout-django-rest-framework-eb1b53ac6d35
3. https://www.youtube.com/watch?v=PUzgZrS_piQ