# Local install guide

1. Download the source code to your target folder
2. create a env.py file in the root foleder, create a variable named SECRET_KEY as a string to set your secret key.
3. use "python manage.py makemigrations" to create a new sqlite database file
4. use "python manage.py migrate" to migrate the initial settings.
5. use "python manage.py runserver" to run the backend api on port 8000
