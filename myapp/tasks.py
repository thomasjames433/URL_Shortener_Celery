from celery import shared_task
from .models import UrlModel

@shared_task(bind=True)
def test_func(self):
    total=UrlModel.objects.all()
    for tot in total:
        tot.hitcountperday=0
        tot.save()
    return "Done"