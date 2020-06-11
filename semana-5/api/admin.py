from django.contrib import admin
from api.models import *

models = [User, Agent, Event, Group, GroupUser]

admin.site.register(models)
