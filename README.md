# URL_Shortener_Celery
This a project that shortens long urls and redirects short urls to their corresponding long url. Made using django, django-rest-framework and celery, Uses Sqlite3 as a database

## Features:
- Gets hitcount of each url
- Every 10th hit-count redirects to an advertisement page (for now google)
- A url cannot be accesed more than 20 times a day. This is made possible by using Django-Celery to make sure the daily-hit-counts are set to 0 at midnight

