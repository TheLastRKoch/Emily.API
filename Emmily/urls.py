from django.conf.urls import url
from django.contrib import admin
from django.urls import path

import  wordlist_skill.api_views
import  wordlist_skill.views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/wordlist/', wordlist_skill.api_views.WordList.as_view()),
    path('api/v1/wordlist/new', wordlist_skill.api_views.WordCreation.as_view()),
    path('api/v1/wordlist/<int:id>', wordlist_skill.api_views.WordRetriveUpdateDestroy.as_view()),

    url('',wordlist_skill.views.index)
]
