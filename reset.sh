echo "Install Component"
#pip install -r requirements.text

echo "Deleting database"
rm db.sqlite3

echo "Migration"
python manage.py migrate

echo "Create Cache"
python manage.py createcachetable

echo "Run App"
python manage.py runserver

