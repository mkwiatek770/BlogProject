# BlogProject

Blog webpage, for programmers. Built with RWD approach. Django CKEditor included which allows to create nice looking posts in easy way.

## Technology Stack
* Python
* Django
* Javascript
* jQuery
* PostgreSQL

## Installing
1. Clone git repository
2. Create virtualenv `virtualenv -p python3 venv`
3. Activate virtualenv `source venv/bin/activate`
4. Install dependencies `pip install -r requirements.txt`
5. Setup psql database called `blogproject_db`
6. Change psql password to yours 
7. `python manage.py migrate`
8. `python manage.py runserver`

You're ready to go ;)

