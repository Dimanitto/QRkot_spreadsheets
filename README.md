# Приложение QRKot

## Технологии:
 ![GitHub](https://img.shields.io/badge/-GitHub-464646??style=flat-square&logo=GitHub)  ![Python](https://img.shields.io/badge/-Python-464646??style=flat-square&logo=Python)
 ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

## Описание проекта
Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

* Проекты
 
В Фонде QRKot может быть открыто несколько целевых проектов. У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается. Пожертвования в проекты поступают по принципу First In, First Out: все пожертвования идут в проект, открытый раньше других; когда этот проект набирает необходимую сумму и закрывается — пожертвования начинают поступать в следующий проект.

* Пожертвования

Каждый пользователь может сделать пожертвование и сопроводить его комментарием. Пожертвования не целевые: они вносятся в фонд, а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.

* Добавлена возможность выгрузки отчёта по пожертвованиям в google

Доступна по адрессу http://127.0.0.1:8000/google/
![Отчёт](https://i.ibb.co/Rpk57y5/2023-04-26-14-54-36.png)

___
## Как запустить проект

Клонируйте репозиторий, перейдите в папку, создайте виртуальное окружение и активируйте:
```
python3 -m venv env
```
MacOS/Linux:
```
. venv/bin/activate
```
Windows:
```
. venv\Scripts\activate
```

Обновите менеджер пакетов (pip) и установите зависимости из файла requirements.txt:

```
(venv) python3 -m pip install --upgrade pip
```
```
(venv) pip install -r requirements.txt
```
___
## Запуск проекта:
Создать файл .env

* Если у вас Linux/MacOS
```
touch .env
```

* Если у вас Windows
```
type nul > .env
```
Заполнить файл .env:

```
APP_TITLE=Благотворительный фонд котиков
DESCRIPTION=Сбор пожертвований на нужды хвостатых
DATABASE_URL=your_database_url
SECRET=your_secret_key (any symbols)
Далее идут переменные окружения вашего сервисного аккаунта google sheets 
EMAIL=Ваша почта
TYPE=service_account
PROJECT_ID=
PRIVATE_KEY_ID=
PRIVATE_KEY=
CLIENT_EMAIL=
CLIENT_ID=
AUTH_URI=https://accounts.google.com/o/oauth2/auth
TOKEN_URI=https://oauth2.googleapis.com/token
AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
CLIENT_X509_CERT_URL=
```
Пример данных сервисного аккаунта:
```
{
  "type": "service_account",
  "project_id": "fluid-dreamer-343515",
  "private_key_id": "47169bcc4c4......8a331d4b769eb1ff",
  "private_key": "-----BEGIN PRIVATE KEY-----\n....bTxwcv\n-----END PRIVATE KEY-----\n",
  "client_email": "test-testovich@fluid-dreamer-343515.iam.gserviceaccount.com",
  "client_id": "114239083367454348646",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/test-testovich%40fluid-dreamer-343515.iam.gserviceaccount.com"
} 
```
Выполнить миграции:
```
alembic upgrade head
```
Выполнить запус сервиса:
```
uvicorn app.main:app --reload
```
___
## Доступ к сервису:
Сервис будет доступен по адресу http://127.0.0.1:8000/

### Дополнительно
Документация по API доступна по адрессу: http://127.0.0.1:8000/swagger#/
___
### Автор
Selivanov Dmitry