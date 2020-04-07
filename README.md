# Overview
* Docker container using Flask and Postgres.
* This application creates an endpoint /inbound to recieve POST or GET requests.
* Use this application to store requests in Postgres.

# How to
* Open Terminal and go to root folder
```
docker-compose up -d --build
```

* Create table in Postgres
```
docker-compose exec web python manage.py create_db
```

* Test the database by running this function
```
docker-compose exec web python manage.py test_message
```

What you see:
```PowerShell
(env) ➜  flask-docker git:(master) docker-compose exec web python manage.py seed_db
Usage: manage.py [OPTIONS] COMMAND [ARGS]...
Try 'manage.py --help' for help.

Error: No such command 'seed_db'.
(env) ➜  flask-docker git:(master) docker-compose exec web python manage.py test_message
(env) ➜  flask-docker git:(master) docker-compose exec db psql --username=hello_flask --dbname=hello_flask_dev
psql (12.2)
Type "help" for help.

hello_flask_dev=# \c hello_flask_dev
You are now connected to database "hello_flask_dev" as user "hello_flask".
hello_flask_dev=# select * from messages;
 id |     push_id      | inbound_id | subscription_id | phone_number | keyword | contents
----+------------------+------------+-----------------+--------------+---------+----------
  1 | 123abcd4586eddfg |            |                 |              |         |
(1 row)

hello_flask_dev=# \q
```

# Does it work?
* Go to: http://localhost:5000/ once you build the container
