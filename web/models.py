from django.db import models

# Create your models here.
class LandingPage(models.Model):
    title = models.CharField(max_length=200)
    featured_image = models.FileField(upload_to="landingpage/featured/")


    def __str__(self):
        return self.title


class WhatWeDealWith(models.Model):
    title = models.CharField(max_length=128)
    featured_image = models.FileField(upload_to="dealwith/featured/")

    def __str__(self):
        return self.title


class FeaturedBrand(models.Model):
    title = models.CharField(max_length=128)
    featured_image = models.FileField(upload_to="brands/featured/")

    def __str__(self):
        return self.title