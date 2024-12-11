from django.shortcuts import render,redirect

# Create your views here.
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random,string
from django.utils import timezone


class ShortenURL(APIView):

    def makeshorturl(self):
        characters = string.ascii_letters + string.digits + "-_." + "~"
        
        while True:
            shorturl=''.join(random.choice(characters) for i in range(6))
            if not UrlModel.objects.filter(shorturl=shorturl).exists():
                break
        return shorturl

    def post(self,request):
        longurl=request.data.get('longUrl')
        if not longurl:
            return Response({
                "error":"long url is needed",
                "status":400
            })
        
        scheme=request.scheme
        host=request.get_host()
        
        try:
            urlexists=UrlModel.objects.get(longurl=longurl)

            return Response({
            "shortUrl":f"{scheme}://{host}/{urlexists.shorturl}"
        })
        except UrlModel.DoesNotExist:

            shorturl=self.makeshorturl()
            UrlModel.objects.create(longurl=longurl, shorturl=shorturl)
            return Response({
                "shortUrl":f"{scheme}://{host}/{shorturl}"
                })
        
        
class RedirectUrl(APIView):
    def get(self,request,shortUrl):

        try:
            urlexists=UrlModel.objects.get(shorturl=shortUrl)

            urlexists.hitcount+=1
            urlexists.hitcountperday+=1

            
            if urlexists.last_accessed is None or urlexists.last_accessed.date() != timezone.now().date():
                urlexists.hitcountperday=1

            urlexists.last_accessed=timezone.now()
            urlexists.save()

            if(urlexists.hitcountperday>20):
                return Response({
                    "error":"Wait till tommorow to access the url"
                })

            if urlexists.hitcount%10==0:
                return redirect('https://google.com')
            


            return redirect(urlexists.longurl)
        except UrlModel.DoesNotExist:
            return Response({"error":"No long url corresponding", "status":404})
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UrlModel

class UrlDetails(APIView):
    def get(self, request):
        url = request.query_params.get('url')
        
        if not url:
            return Response({"error": "URL parameter is required"}, status=400)

        try:
            temp = UrlModel.objects.get(longurl=url)

        except UrlModel.DoesNotExist:
            try:
                temp = UrlModel.objects.get(shorturl=url)
            except UrlModel.DoesNotExist:
                return Response({"error": "URL not found"}, status=404)

        return Response({
            "longUrl": temp.longurl,
            "shortUrl": temp.shorturl,
            "hitCount": temp.hitcount
        })


class totalurl(APIView):
    def get(self,request,number):
        temp=UrlModel.objects.all().order_by('-hitcount')[:number]

        data=[
            {
            "longUrl":t.longurl,
            "shortUrl":t.shorturl,
            "hitcount":t.hitcount
            } for t in temp
        ]

        return Response(data)