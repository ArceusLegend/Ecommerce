# Ecommerce
A Django project to build an online bookstore

# Set up
For this project to work properly, before starting the server, you will need to first create a virtual environment and then download all the assets listed in requirements.txt. Afterwards you'll need to make and run some migrations for Django to build a database (by default in SQLite3), make a .env file for any secret keys you don't want in the actual code, and then finally enable stripe for payments to work.

- **Creating a virtual environment**

   In your console, navigate to the folder where you installed the project. Run the folowing command:
   
   `python -m venv <path_to_venv>`
   
   `path_to_venv` can be either a relative or absolute path. Make sure NOT to use the angled brackets when writing the path. For example, `./venv` will create a new folder for your virtual environment on your current directory called venv. Please note that it may take a few minutes for the virtual envronment to be created, depending on how good the computer running the command is.
   
- **Running the virtual environment**

   Now that the venv is installed, you should see a folder called `Scripts` with an activation script inside. You can activate the venv by typing `./<path_to_venv>/Scripts/activate` in your console.

- **Download the required assets from requirements.txt**

  In requirements.txt you'll find a list of required assets and libraries that need to be downoaded first in order for the project to work correctly. You can install everything in that file to your current working environment (in this case the venv) by going to the console and writing `pip install -r requirements.txt`

- **Create migrations**

  Django uses what's called *models* to create a single, definitive source of information about your data. They contain the essential fields and behaviors of the data you’re storing, and generally map to a single database table.

  This project already contains the finished models that it needs, however you first need to create the migrations required to create the database in the first place. For that, go to your console and write `python -m manage.py makemigrations`. This will create the migrations required for a database to be created and for the models to map to said database. By default, the database created is an SQLite3 database.

- **Run the migrations**
  
  Finally, to apply the migration changes, go to your console and run the command `python -m manage.py migrate`. This will create a database for your data to be stored.

  **YOUR DATABASE MAY CONTAIN SENSITIVE INFORMATION, SO NEVER SHARE IT WITH ANYONE YOU DON'T TRUST**
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
- **Enable stripe**

  Payments are processed using Stripe. You will need to make an account on Stripe first by going [here](https://dashboard.stripe.com/register), in order to get your own API keys. Once your account is created, you will need to activate it, and then go to your dashboard. In the middle of the page, click on "API keys for developers".
  
  ![εικόνα](https://github.com/ArceusLegend/Ecommerce/assets/109414442/1a767a99-9156-40cc-a921-aa99aab07ca9)

  Now go to the project, and navigate to core/settings.py Scroll all the way to the bottom to find the `PUBLISHABLE_KEY`, `SECRET_KEY`, and `STRIPE_ENDPOINT_SECRET` constants. Replace these with your own keys; the publishable and secret keys can be found in the API keys tab:
  
  ![εικόνα](https://github.com/ArceusLegend/Ecommerce/assets/109414442/e08eb6f2-4c42-432d-ab05-9fa63084b2a6)

  You can then find the endpoint secret by going to the "Webhooks" tab, and then clicking on either button you want:

  ![εικόνα](https://github.com/ArceusLegend/Ecommerce/assets/109414442/938a13d3-c4c4-424f-846e-38f129f9bde5)

  Both buttons will take you to the same page, which will include a sample code block on the right side of your screen. Go to line 25, and copy the `endpoint_secret` key. This is your STRIPE_ENDPOINT_SECRET.
  
  Finally, activate stripe with `stripe listen --forward-to localhost:8000/payment/webhook/`.

  Note: the port number 8000 is the default port that Django uses to run the server. If you're using a different port number, you should replace 8000 with that instead. You can test that it works by going to the payment page and using the test card numbers in stripe.txt. *No auth* means stripe will simulate a successful payment without the need to authenticate the payment, *Auth* means Stripe will generate a pop up simulating an event that requires authentication to proceed, and *Error* means that stripe will simulate a failed authentication event.

# Run the server
Your setup is done! You can now activate the server by going to the console and using the command `python -m manage.py runserver`. If you want to add products to the store, you can go to 127.0.0.1:8000/admin, and manage your database from there. 
