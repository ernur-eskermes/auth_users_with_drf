# Авторизация юзеров DRF

# Локальный запуск
git clone https://github.com/ernur-eskermes/auth_users_with_drf.git

cd auth_users_with_drf

pip install -r requirements.txt

python manage.py runserver

# Использование
Username: admin

Password: admin

Регистрация - <http://127.0.0.1:8000/api/v1/users/create/>

Получение jwt токена для авторизаций - <http://127.0.0.1:8000/api/token/>

Авторизация через передачи токена в headers - \
  curl -H "Authorization: Bearer token"
  http://localhost:8000/api/v1/clients/

Вывод всех и активных клиентов (видны только авторизованным через jwt токен юзерам) - <http://127.0.0.1:8000/api/v1/clients/>
  
Подтверждение (активация аккаунтов) по почте происходить по динамической ссылке - <http://127.0.0.1:8000/api/v1/users/create/activate/<uuid>/<user_id>/>
