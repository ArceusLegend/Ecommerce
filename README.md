# Ecommerce
A Django project to build an online bookstore. Built with Django, Bootstrap, and JQuery

# Quick-Start
Pre-requisites:

- Python >= 3.10

It's highly advised to use a virtual environment for this project (e.g. with `python -m venv ./venv`)

To set-up and deploy the Django project with default (development) configurations:

- Install Python requirements
    ```
    pip install -r requirements.txt
    ```
- Create an .env file by copying the template provided (see later sections
    ```
    cp .env.template .env
    ```
- Run migrations to create the database
    ```
    python manage.py migrate
    ```
- Start the dev server
    ```
    python manage.py runserver 0.0.0.0:8000
    ```
    *Make sure you add 0.0.0.0 or any other host you use to the `ALLOWED_HOSTS` list if you want to use that host, otherwise just use localhost or 127.0.0.1

Note that the .env file contains settings for setting-up Stripe and different
options for Databases (see later sections for more information)

# Set up
For this project to work properly, before starting the server, you will need to first create a virtual environment and then download all the assets listed in requirements.txt. Afterwards you'll need to run some migrations for Django to build a database (by default in SQLite3), make a .env file for any secret keys you don't want in the actual code, and then finally enable Stripe for payments to work. Optionally, you can also relocate the media folder.

- **Creating a virtual environment**

   In your console, navigate to the folder where you installed the project. Run the folowing command: `python -m venv <path_to_venv>`
   
   `path_to_venv` can be either a relative or absolute path. Make sure NOT to use the angled brackets when writing the path. For example, `./venv` will create a new folder for your virtual environment on your current directory called venv. Please note that it may take a few minutes for the virtual envronment to be created, depending on how good the computer running the command is.
   
- **Running the virtual environment**

   Now that the venv is installed, you should see a folder called `Scripts` with an activation script inside. You can activate the venv by typing `/<path_to_venv>/Scripts/activate` in your console.

- **Download the required assets from requirements.txt**

  In requirements.txt you'll find a list of required assets and libraries that need to be downoaded first in order for the project to work correctly. You can install everything in that file to your current working environment (in this case the venv) by going to the console and writing `pip install -r requirements.txt`

- **Create .env file**

  You may find yourself using some secret keys throught development. Ideally you shouldn't use any of these keys in your code, and this is where environment variables come in handy. You will need to make a .env file on the same level as manage.py. This project uses python-dotenv to import any variables you create there into settings.py, and you can access them with the `os.getenv()` method.

- **The Django secret key**

  The first envvar you should add is the Django secret key in settings.py. By default, it'll be an empty string and the project will NOT work if it isn't changed. The envvar should be called 'SECRET_KEY_D' to help distinguish it from other secret key variables, but it can be called whatever you want, as long as you change what variable the `getenv()` method looks for to match the new envvar name. For security purposes, the value should be a large, randomized value (for example 'django-insecure-sdawqe1-qfdacq3f(&8878&!_=&78)'

- **Select a database engine**

  The second envvar you should add is the name of the database engine you want. Django has integrated support for SQLite, PostgreSQL, MySQL, and Oracle. The default database in this project is SQLite, but it also supports PostgreSQL and MySQL. You can switch to either option by creating an envvar called `DATABASE_ENGINE`, and assigning it either 'postgres' to use PostgreSQL, or 'mysql' to use MySQL. If you want to add another option, you can use any fully-qualified package path in settings.py by following the documentation [here](https://docs.djangoproject.com/en/4.2/ref/settings/#databases). 

  It is recommended to use the same database engine for both development and production modes. Additionally, since your database may contain sensitive information like passwords, addresses, and billing information, avoid sharing in version control and with parties that you don't fully trust.

- **Migrations**

  Django uses what's called *models* to create a single, definitive source of information about your data. They contain the essential fields and behaviors of the data you’re storing, and generally map to a single database table.

  This project already contains the finished models that it needs, as well as the migration files to make a new database. Simply go to your console and use the command `python -m manage.py migrate`, and Django will make a new Database for you in whatever engine you chose.

- **Enable stripe**

  Payments are processed using Stripe. You will need to make an account on Stripe first by going [here](https://dashboard.stripe.com/register), in order to get your own API keys. Once your account is created, you will need to activate it, and then go to your dashboard. In the middle of the page, click on "API keys for developers".
  
  ![Image of stripe dashboard page](https://github.com/ArceusLegend/Ecommerce/assets/109414442/1a767a99-9156-40cc-a921-aa99aab07ca9)

  Now go to the project, and navigate to core/settings.py Scroll all the way to the bottom to find the `PUBLISHABLE_KEY`, `SECRET_KEY`, and `STRIPE_ENDPOINT_SECRET` constants. Replace these with your own keys; the publishable and secret keys can be found in the API keys tab:
  
  ![Image of API Keys tab in developer page](https://github.com/ArceusLegend/Ecommerce/assets/109414442/e08eb6f2-4c42-432d-ab05-9fa63084b2a6)

  You can then find the endpoint secret by going to the "Webhooks" tab, and then clicking on either button you want:

  ![Image of clickable buttons in the Webhooks tabs](https://github.com/ArceusLegend/Ecommerce/assets/109414442/938a13d3-c4c4-424f-846e-38f129f9bde5)

  Both buttons will take you to the same page, which will include a sample code block on the right side of your screen. Go to line 25, and copy the `endpoint_secret` key. This is your STRIPE_ENDPOINT_SECRET.

  You will want to store these keys in your .env as well. The publishable key envvar should be called 'PUBLISHABLE_KEY', the secret should be 'SECRET_KEY_S', and the webhook endpoint secret key should be 'STRIPE ENDPOITN SECRET'.
  
  Finally, activate stripe with `stripe listen --forward-to localhost:8000/payment/webhook/`.

  Note: the port number 8000 is the default port that Django uses to run the server. If you're using a different port number, you should replace 8000 with that instead. You can test that it works by going to the payment page and using the test card numbers in stripe.txt.
  - *No auth* means stripe will simulate a successful payment without the need to authenticate the payment
  - *Auth* means Stripe will generate a pop up simulating an event that requires authentication to proceed
  - *Error* means that stripe will simulate a failed authentication event.
  - For the purposes of testing with these values, the expiration date can be any valid future date, and the CVC and T.K. values can be any random integer

   Stripe will record all the relevant events for you, and you can see them on your browser by navigating to the stripe website, and then going to your dashboard and clicking on the 'Events' tab.

- **OPTIONAL: Media folder**

  As this project doesn't support user uploaded media files, the media folder is located within the static folder. If, for whatever reason, youy want to change the location of the media folder, you should also go to settings.py and change `MEDIA_URL` and `MEDIA_ROOT` to reflect this change, as these are what Django uses to locate your image files.

# Run the server

Your setup is done! If you want to use the project in development mode, you can simply go to the console and use the runserver command like this: `python -m manage.py runserver`, and look at it in your browser by going to 127.0.0.1:8000 (or whatewver port number you want to use instead of 8000). If you wish to deploy it, there are several steps you must take first to ensure that it runs smoothly in a production environment, so in the next section we'll look at first how to change your database engine if you don't want to use SQLite3 in production, and how to deploy the project.

# Deployment

To deploy the project in a production environment, you can go through the following steps, and consult the documentation [here](https://docs.djangoproject.com/en/4.2/howto/deployment/) if you want.

1) **Secret key**

   When a Django project is initialized, you can find a randomized key assigned to a SECRET_KEY variable in settings.py. *DO NOT USE THIS ANYWHERE BESIDES PRODUCTION AND DO NOT COMMIT IT ANYWHERE IN SOURCE CONTROL*. It is imparative to keep this key a secret for security reasons. It should be a large,randomized value, as described above. As an extra security measure, Django 4.1 introduced [Secret Key Fallbacks](https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-SECRET_KEY_FALLBACKS) to assist users who may want to introduce SECRET_KEY rotations.
   
2) **Ensure that DEBUG is set to False**

   Enabling the DEBUG option is great for your development environment, but not so much for production. If there is an error somewhere that causes a traceback to occur, you are given a lot of potentially sensitive information about your code, and you certainly don't want that leaking to any unwanted parties. It is set to False by default in settings.py, but you can enable it again in your .env file.

3) **Allowed hosts**

   If `DEBUG` is set to `False`, Django can't run without at least one valid value in the `ALLOWED_HOSTS` list. This list is required to protect against CSRF attacks. In this project, the list has already got 'localhost' and '127.0.0.1' in it, but you can also add your own domain name as well.

   As an extra security feature, you can also set up the web server in front of Django to respond with a static error page or ignore requests for incorrect hosts instead of forwarding the request to Django. This way you’ll avoid spurious errors in your Django logs (or emails if you have error reporting configured that way).

4) **Email settings**

   This project sends emails during the registration process, containing a link that a user needs to click on to activate their account. Django sends these emails from webmaster@localhost and root@localhost by default, although some email service providers don't accept these emails. To use different sender addresses, modify the `DEFAULT_FROM_EMAIL` and `SERVER_EMAIL` settings to your liking

5) **Final steps**

   There are several other items in the official documentation linked at the start of this section that you should go through to ensure that your project is ready for deployment - the ones mentioned here are, in my opinion, the most important ones for this type of project. Once you're done going through the checklist, you have but a couple more steps to deploy the project to production.

   - Run `python -m manage.py collectstatic` in the console. As Django doesn't serve static files in production, you will need to copy them all and put them in a new folder for your web server to access them instead. This is what `collectstatic` does automatically, and you can change the destination in the `STATIC_ROOT` variable in settings.py. By default, it'll be a new folder called 'assets' in the root directory of your project
  
   - Select a deployment method. Django currently supports two interfaces: [WSGI](https://wsgi.readthedocs.io/en/latest/) and [ASGI](https://asgi.readthedocs.io/en/latest/). A quick and easy method to deploy this project is Gunicorn but, as this project was built on a windows machine, it uses Waitress instead, which is also a quick and easy to use method of deployment. Simply go to serve.py the project's root directory, and run the script. Waitress is now hosting your project! Do note, that as this a WSGI interface, you will have to kill the server by pressing CTRL+C in the terminal that Waitress is running from and then run the script again to reflect any changes within the code on your production environment.
  
   - If you are using a Unix machine, and you want to use Gunicorn, you can simply run the command `pip install gunicorn` on your console, and then use the command `gunicorn myproject.wsgi` from the same directory as manage.py. This will start one process running one thread listening on 127.0.0.1:8000. You can read the [deployment documentation](https://docs.gunicorn.org/en/latest/deploy.html) for extra details.
  
   - Other viable options with the WSGI include Apache combined with whichever module allows Django to be deployed with Apache, like uWSGI and mod-wsgi.

# Conclusion

This project has every basic feature that an online commerce application has; a cart, browsing filters, payment, and user functions (registration, login/out, and account deletion). In the future there may be a wishlist function, a search bar, better UI, and possibly PayPal support. 
