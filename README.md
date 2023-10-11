# Ecommerce
A Django project to build an online bookstore

<a name = "set-up"/>

# Set up
For this project to work properly, before starting the server, you will need to first create a virtual environment and then download all the assets listed in requirements.txt. Afterwards you'll need to make and run some migrations for Django to build a database (by default in SQLite3), make a .env file for any secret keys you don't want in the actual code, and then finally enable stripe for payments to work.

<a name = "create-venv"/>

- **Creating a virtual environment**

   In your console, navigate to the folder where you installed the project. Run the folowing command:
   
   `python -m venv <path_to_venv>`
   
   `path_to_venv` can be either a relative or absolute path. Make sure NOT to use the angled brackets when writing the path. For example, `./venv` will create a new folder for your virtual environment on your current directory called venv. Please note that it may take a few minutes for the virtual envronment to be created, depending on how good the computer running the command is.

   <a name = "run-venv"/>
   
- **Running the virtual environment**

   Now that the venv is installed, you should see a folder called `Scripts` with an activation script inside. You can activate the venv by typing `./<path_to_venv>/Scripts/activate` in your console.

<a name = "requirements"/>

- **Download the required assets from requirements.txt**

  In requirements.txt you'll find a list of required assets and libraries that need to be downoaded first in order for the project to work correctly. You can install everything in that file to your current working environment (in this case the venv) by going to the console and writing `pip install -r requirements.txt`

<a name = "create-mig"/>

- **Create migrations**

  Django uses what's called *models* to create a single, definitive source of information about your data. They contain the essential fields and behaviors of the data you’re storing, and generally map to a single database table.

  This project already contains the finished models that it needs, however you first need to create the migrations required to create the database in the first place. For that, go to your console and write `python -m manage.py makemigrations`. This will create the migrations required for a database to be created and for the models to map to said database. By default, the database created is an SQLite3 database.

<a name = "run-mig"/>

- **Run the migrations**
  
  Finally, to apply the migration changes, go to your console and run the command `python -m manage.py migrate`. This will create a database for your data to be stored.

  **YOUR DATABASE MAY CONTAIN SENSITIVE INFORMATION, SO NEVER SHARE IT WITH ANYONE YOU DON'T TRUST**
  
<a name = "env"/>

- **Create .env file**

  You may find yourself using some secret keys throught development. Ideally you shouldn't use any of these keys in your code, and this is where environment variables come in. Go to the root directory of the project, and create a new file simply called .env. Here you can safely add any variables you want to be kept hidden from your code, like this:
  ```
  # You can also add comments like this
  SECRET1 = ... # Add your key here
  SECRET2 = ... # Add some other key
  ```
  Among the requirements, you'll find a package called python_dotenv, and this is what we'll use to import all the variables in the .env to to our script. Like this:
  
  ```
  from dotenv import load_dotenv

  load_dotenv()
  ```

  And like that, all the variables in the .env are available in the script. To use them, call the `os.getenv()` method, passing as a paramater the name of the variable as a string, like this:
  ```
  SECRET1 = os.getenv('SECRET1') # Pass SECRET1 from .env to this
  SECRET2 = os.getenv('SECRET2') # Pass SECRET2 from .env to this
  ```
<a name = "stripe"/>

- **Enable stripe**

  Payments are processed using Stripe. You will need to make an account on Stripe first by going [here](https://dashboard.stripe.com/register), in order to get your own API keys. Once your account is created, you will need to activate it, and then go to your dashboard. In the middle of the page, click on "API keys for developers".
  
  ![εικόνα](https://github.com/ArceusLegend/Ecommerce/assets/109414442/1a767a99-9156-40cc-a921-aa99aab07ca9)

  Now go to the project, and navigate to core/settings.py Scroll all the way to the bottom to find the `PUBLISHABLE_KEY`, `SECRET_KEY`, and `STRIPE_ENDPOINT_SECRET` constants. Replace these with your own keys; the publishable and secret keys can be found in the API keys tab:
  
  ![εικόνα](https://github.com/ArceusLegend/Ecommerce/assets/109414442/e08eb6f2-4c42-432d-ab05-9fa63084b2a6)

  You can then find the endpoint secret by going to the "Webhooks" tab, and then clicking on either button you want:

  ![εικόνα](https://github.com/ArceusLegend/Ecommerce/assets/109414442/938a13d3-c4c4-424f-846e-38f129f9bde5)

  Both buttons will take you to the same page, which will include a sample code block on the right side of your screen. Go to line 25, and copy the `endpoint_secret` key. This is your STRIPE_ENDPOINT_SECRET.
  
  Finally, activate stripe with `stripe listen --forward-to localhost:8000/payment/webhook/`.

  Note: the port number 8000 is the default port that Django uses to run the server. If you're using a different port number, you should replace 8000 with that instead. You can test that it works by going to the payment page and using the test card numbers in stripe.txt.
  - *No auth* means stripe will simulate a successful payment without the need to authenticate the payment,
  - *Auth* means Stripe will generate a pop up simulating an event that requires authentication to proceed
  - *Error* means that stripe will simulate a failed authentication event.

<a name = "runserver"/>

# Run the server

Your setup is done! If you want to use the project in development mode, you can simply go to the console and use the runserver command like this: `py manage.py runserver`, and look at it in your browser by going to 127.0.0.1:8000 (or whatewver port number you want to use instead of 8000). If you wish to deploy it, there are several steps you must take first to ensure that it runs smoothly in a production environment, so in the next section we'll look at first how to change your database engine if you don't want to use SQLite3 in production, and how to deploy the project.

<a name = "deploy"/>

# Deployment

To deploy the project in a production environment, you can go through the following steps, and consult the documentation [here](https://docs.djangoproject.com/en/4.2/howto/deployment/) if you want.

<a name = "secret-key"/>

1) **Secret key**

   When a Django project is initialized, you can find a randomized key assigned to a SECRET_KEY variable in settings.py. *DO NOT USE THIS ANYWHERE BESIDES PRODUCTION AND DO NOT COMMIT IT ANYWHERE IN SOURCE CONTROL*. It is imparative to keep this key a secret for security reasons. By default, in this project, it is set to an empty string, but you should go to your .env and set it to a large, randomized value. As an extra security measure, Django 4.1 introduced [Secret Key Fallbacks](https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-SECRET_KEY_FALLBACKS) to assist users who may want to introduce SECRET_KEY rotations.

<a name = "debug"/>

2) **Ensure that DEBUG is set to False**

   Enabling the DEBUG option is great for your development environment, but not so much for production. If there is an error somewhere that causes a traceback to occur, you are given a lot of potentially sensitive information about your code, and you certainly don't want that leaking to any unwanted parties. It is set to False by default in settings.py, but you can enable it again in your .env file.

<a name = "allowed-hosts"/>

3) **Allowed hosts**

   If `DEBUG` is set to `False`, Django can't run without at least one valid value in the `ALLOWED_HOSTS` list. This list is required to protect against CSRF attacks. In this project, the list has already got 'localhost' and '127.0.0.1' in it, but you can also add your own domain name as well.

   As an extra security feature, you can also set up the web server in front of Django to respond with a static error page or ignore requests for incorrect hosts instead of forwarding the request to Django. This way you’ll avoid spurious errors in your Django logs (or emails if you have error reporting configured that way).

<a name = "database"/>

4) **Database**
   
   When a project is initialized, Django uses SQLite by default. While not a bad choice for a development environment, some may prefer to use a different databse engine. PostgreSQL (generally considered the best suited for Django), MySQL, etc. The default database in SQLite3, however you can change that by going to your .env file, creating a varible called DATABASE_ENGINE, and assigning it either the string 'postgres' if you want to use PostgreSQL, or 'mysql'if you want to use MySQL.

   Note: If you are not using SQLite, there are some additional steps required to take.

   For non-SQLite databases, Django required additional parameters to connect to them. In this project I've defined several parameters for these. You can see the default values in settings.py, and you can change them in the .env file if you wish. There are additional parameters that can be passed that are all listed in the official documentation [here](https://docs.djangoproject.com/en/4.2/ref/settings/#databases). 
   
   Additionally, Django has built-in support for SQLite3, PostgreSQL, MySQL, and Oracle DB. If you don't want to use any of the above options, you can still use another fully-qualified database by setting the "ENGINE" option to a valid path (ie mypackage.backends.whatever).

   And as a bit of an extra tip, ensure that your database engine is the same in both production AND development. There may be issues translating changes in your development environment to your production one otherwise. And also, always backup your databases!

<a name = "email-settings"/>

5) **Email settings**

   This project sends emails during the registration process, containing a link that a user needs to click on to activate their account. Django sends these emails from webmaster@localhost and root@localhost by default, although some email service providers don't accept these emails. To use different sender addresses, modify the `DEFAULT_FROM_EMAIL` and `SERVER_EMAIL` settings to your liking

