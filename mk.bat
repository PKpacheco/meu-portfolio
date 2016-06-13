REM call Example (Windows only)
REM TIP: if using windows for python developer view this: https://www.continuum.io/downloads
REM > mk run  

if "%1"=="clean" 		goto :clean
if "%1"=="migrate" 		goto :migrate
if "%1"=="run" 			goto :run
if "%1"=="migrations" 	goto :migrations
if "%1"=="user" 		goto :user
if "%1"=="shell" 		goto :shell

:clean
	del *.pyc
:migrate:
	python manage.py migrate
:run
	python manage.py runserver 0.0.0.0:8000
:migrate
	python manage.py migrate
:migrations
	python manage.py makemigrations
:user
	python manage.py createsuperuser
:shell
	python manage.py shell