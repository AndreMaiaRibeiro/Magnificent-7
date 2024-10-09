⚽ Magnificent 7 - Football Team Builder API (DRF)

Hey, Lead Engineer! I think I know that you know how to start this program, but here’s a quick tutorial just in case. 😄

## Setup Instructions

1. Clone the repo, because obviously that’s the first step.
2. Create and activate the virtual environment:
   
   On Windows:
   ```
   python -m venv env
   env\\Scripts\\activate
   ```

   On Mac/Linux:
   ```
   python3 -m venv env
   source env/bin/activate
   ```

3. Install the requirements:

   ```
   pip install -r requirements.txt
   ```

4. Create a **.env** file in the root directory and add the API URL:

   ```
   MAGNIFICENT_API='https://your-api-url-here'
   ```

5. Setup the database (yes, migrations are still necessary):

   ```
   cd magnificence_project

   python manage.py makemigrations
   python manage.py migrate
   ```

6. Populate the database by fetching the player data:

   ```
   python manage.py runserver
   ```

Go to the link: /api/magnificent-seven/
And boom 💥 – you’re ready to roll!

## Small Test?
In case you feel like running a test (because why not, right?):

   ```
   python manage.py test
   ```

That’s it! You now have the **Magnificent 7**. Hope this saves you some time, unless you're the kind of person who likes reading these. 😉

Cheers!