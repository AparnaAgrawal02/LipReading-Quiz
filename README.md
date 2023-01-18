# LipReading-Quiz
simple quiz website 

## Getting started with development

Dependencies:

- Python 3.6.x
- Django 3.2.x

## 1. Clone this repository

```bash
git clone https://github.com/AparnaAgrawal02/LipReading-Quiz.git
cd lipreading
```

### 2. Install [Pipenv](https://pipenv.pypa.io/en/latest/)

### 3. Create the virtualenv

```bash
## run following command from `lets_quiz` directory
pipenv shell
```

### 4. Install python packages

```bash
pip install -r requirement.txt
```

### 5. Run database migrations

```bash
cd lets_quiz
python manage.py makemigrations
python  manage.py migrate
```

### 6. Create superuser

```bash
python manage.py createsuperuser
```

### 7. Run development server

```bash
python manage.py runserver
```