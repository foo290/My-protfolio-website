# My Portfolio
I created a website for my own portfolio which you can access through <a href='https://mydigitalprofile.herokuapp.com'>My Portfolio</a>, as i did'nt bought a domain name yet.

## Deployment Configurations
### Procfile
```
web: gunicorn Main_site_project.wsgi
```

### Requirements
```
asgiref==3.2.10
dj-database-url==0.5.0
Django==3.0.8
gunicorn==20.0.4
Pillow==7.2.0
psycopg2==2.8.5
pytz==2020.1
sqlparse==0.3.1
whitenoise==5.2.0
```
### Replacing security keys and setting debug false
```
settings.py

   SECURITY_KEY = os.eviron.get('SECURITY_KEY')
   DEBUG = os.environ.get('DEBUG')
```

## Tech Used
The website is based on **Django** for backend and **bootstrap, fontawesome and google fonts** for frontend.

## License
[MIT](https://choosealicense.com/licenses/mit/)
