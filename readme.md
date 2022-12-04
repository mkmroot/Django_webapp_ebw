--------------------------------
Open CMD
run:-
python -m venv djangoenv
djangoenv\Scripts\activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
cd ebw_project
python manage.py runserver

------------------------------------------------------------
auth_user
---------------
python manage.py create superuser  # it give errors
python manage.py makemigrations # nothing 
python manage.py migrate 
python manage.py create superuser # user name , password 
-----------------------------------------------------------
