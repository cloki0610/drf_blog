# Local install guide

1. Download the source code to your target folder
2. Use "pip install -r requirements.txt" to install all packages in project
3. create a env.py file in the root foleder, create a variable named SECRET_KEY as a string to set your secret key.
4. use "python manage.py makemigrations" to create a new sqlite database file
5. use "python manage.py migrate" to migrate the initial settings.
6. use "python manage.py runserver" to run the backend api on port 8000
7. Optinal: you can write a docker file and attach a volume to store the sqlite file or use docker-compose with different db container.

```
FROM python:3.10
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
COPY . app
WORKDIR /app

EXPOSE 8000

# runs the production server
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
```
