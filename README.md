Django CRM / Bootstrap / Bootswatch / SQLite 

<img src="https://github.com/rocketasia/Django-Chat-crm/assets/74543570/9619bb9d-d81f-4fc3-b478-3c3741946340" />
<img src="https://github.com/rocketasia/DjangoCrm-Chat-GPT/assets/74543570/1999f60f-ca36-493c-be15-693c93b22831" />
<img src="https://github.com/rocketasia/DjangoCrm-Chat-GPT/assets/74543570/803ed829-1201-4f1f-83d7-b0186ad2244f" />




This project uses Django v5 For Django to work, you must install a correct version of Python on your machine. More information here.
Visual Studio Code
Installation
1. Create a virtual environment
From the root directory, run:

python -m venv venv

2. Activate the virtual environment
From the root directory, run:

On macOS:

source venv/bin/activate

On Windows:

venv\scripts\activate

3. Install required dependencies
From the root directory, run:

pip3 install django-crispy-forms

4. Run migrations
From the root directory, run:

python manage.py makemigrations
python3 manage.py migrate

5. Create an admin user to access the Django Admin interface
From the root directory, run:

python manage.py createsuperuser
When prompted, enter a username, email, and password.

Run the application
From the root directory, run:

python3 manage.py runserver

Run the tests
From the root directory, run:


View the application
Go to http://127.0.0.1:8000/ to view the application.

Copyright and License<br>
Copyright © 2024 One Media Asia Co, Ltd. Code released under the MIT license.
