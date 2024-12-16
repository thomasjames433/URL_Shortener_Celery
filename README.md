# URL_Shortener_Celery
This a project that shortens long urls and redirects short urls to their corresponding long url. Made using django, django-rest-framework and Celery

## Features:
- Gets hitcount of each url
- Every 10th hit-count redirects to an advertisement page (for now google)
- A url cannot be accesed more than 20 times a day. This is made possible by using Django-Celery to make sure the daily-hit-counts are set to 0 at midnight


## Functionality

#### shorten
 POST- The given long url is converted to a short one

#### redirect/:<shortUrl
  GET- Redirects the short url (6 character code) to its corresponding long url

#### details/:?url= <enter the url>
  GET- Auto identifies and gets the detail of the long/short url. Note(give "?url=" after "details/:")

#### top/:<int:number>
  GET- Returns a json with the rank of top number times urls based on their hitcounts


## To run the library system:

#### 1. Clone the repository:
   `git clone "https://github.com/thomasjames433/Library-system.git](https://github.com/thomasjames433/URL_Shortener_Celery.git"`
#### 2. Navigate into the project directory:
   `cd URL_Shortener`
#### 3. Install dependencies:
   - `pip freeze > requirements.txt`
   - `python manage.py makemigrations`
   - `python manage.py migrate`  
   - `To createsuperuser: python manage.py createsuperuser`
#### 4. Run the system:
   `python manage.py runserver`

## Technologies Used
- Django
- Django-Rest-Framework
- Django- Celery


