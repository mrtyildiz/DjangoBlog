python3 /opt/DatabaseCreate.py
python3 /app/DjangoBlog/manage.py makemigrations
python3 /app/DjangoBlog/manage.py migrate
python3 /app/DjangoBlog/manage.py runserver 0.0.0.0:8000 --insecure
