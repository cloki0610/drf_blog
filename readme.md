# Local install guide

1. Download the source code to your target folder
2. Use "pip install -r requirements.txt" to install all packages in project
3. create a env.py file in the root foleder, create a variable named SECRET_KEY as a string to set your secret key.
4. use "python manage.py makemigrations" to create a new sqlite database file
5. use "python manage.py migrate" to migrate the initial settings.
6. use "python manage.py runserver" to run the backend api on port 8000
