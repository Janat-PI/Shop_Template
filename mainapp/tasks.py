from django.shortcuts import render
from django.views import View

from mainapp.mixins import CartMixin
from mainapp.models import Category, LatestProducts
from shop.celery_ import app
from celery import shared_task, Task, Celery
from django.db import models

