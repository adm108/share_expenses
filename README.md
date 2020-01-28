# share_expenses

## Description
Individual project. Financial management application writen in Django.

#### Assumptions:
- account creation (registraton and login),
- creating groups,
- creating expenses within a given group, sharing costs - balancing expenses, generating a financial report after archiving a group.



Page under construction. Home view (with header and footer) and registration and login views are available. 
#### How to see it?
##### 1. Clone repository:
```sh
$ git clone https://github.com/adm108/share_expenses.git
```
##### 2. Create virtual enviroment next to src folder (not inside) and activate it.
##### 3. Install all packages from requirements.txt file:
```sh
$ pip install -r requirements.txt
```
##### 4. Go to src folder and use manage.py to enter following commands. Generate SQL commands:
```sh
$ python manage.py makemigrations
```
##### 5. Execute SQL commands:
```sh
$ python manage.py migrate
```
##### 6. Create superuser (enter email, username and password):
```sh
$ python manage.py createsuperuser
```
##### 7. Inside src folder create "static_cdn" folder.
##### 8. Collect static files:
```sh
$ python manage.py collectstatic
```
##### 9. Run your local server to see home page and registration and login views.
```sh
$ python manage.py runserver
```
