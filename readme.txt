- create new database with name 'newsFeed' in postgres
- restore database from dump in file newsFeedDB
- default settings for database connection: 
	"ENGINE": "django.db.backends.postgresql_psycopg2"
        "NAME": "newsFeed"
        "USER": "postgres"
        "PASSWORD": "admin"
        "HOST": "127.0.0.1"
        "PORT": "5432"


run with docker:
run this commands from ./newsFeed/newsFeed
	- docker-compose build
	- docker-compose up