# Template RESTful API for NoticeBoard with posts and likes
***

<img src="https://user-images.githubusercontent.com/55922843/158646788-c446551e-4732-40f5-b64c-45feb73f27a0.png" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" width="650" height="500" />

# Endpoints:
***
- `api/auth/users/`
- `api/api-auth/login/`
- `api/posts/`
- `api/post_likes/:id`
- `/api/analitics/?date_from=2020-02-02&date_to=2020-02-15`
- `api/users/1/`

# Requirements
***
- **Python > 3.9**

# Run
***
- **Install virtualenv:** `pip install virtualenv`

- **Create virtual environment:** `virtualenv env` or `python -m venv env`

- **Activate virtualenv:**

    **unix:** `source env/Scripts/activate`
  
    **windows:** `env/Scripts/activate.bat`

- **Install all requirements:** `pip install -r requirements.txt`

- **Run all migrations:** `python manage.py migrate`
  
- **Run local server:** `python manage.py runserver`
