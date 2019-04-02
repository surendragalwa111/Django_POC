Step-1 create your project
  run command:-
    
    django-admin startproject projectname

Step-2
   Go to your project directory
   run command:-
    
    python manage.py startapp app_name

Step-3
   Create model in models.py file
   import model in apps.py file in the same app_name
   register this app in main settings.py INSTALLED_APP 

Step-4 
  Run commad:-
    
    python manage.py makemigerations appname

Step-5
  Database API/ to manipulate models in terminal
  run command:-
    
    python manage.py shell

  run following command to check all data of a model
     model_name.objects.all()

Step-6 
  Admin interface, create super user
  Run following command:-
    python manage.py createsuperuser

    username: admin
    email: admin@admin.com
    password: sigma@123
  
  Now you can browse /admin  route

Step-7
  Register model on admin page
  Go to admin.py in your app
  import, register your models with following code:-
    
    admin.site.register(model_name)
  