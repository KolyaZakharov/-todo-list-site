 # it is a project for tracking and managing tasks
 
to run the project locally do the following steps:
- git clone https://github.com/KolyaZakharov/-todo-list-site.git
- cd todo_list
- python -m venv venv
- venv\Scripts\activate
- pip install -r requirements.txt
- copy .env.sample -> .env and populate with all required data
  (SECRET_KEY - It's a django secret key used for hashing
etc.)
- python manage.py migrate
## for login :
**Login:** `admin`

**Password**   `admin`