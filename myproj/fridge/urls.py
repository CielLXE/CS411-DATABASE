from django.urls import path

from . import views

app_name = 'fridge'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:r_id>/', views.detail, name='detail'),
    path('content', views.content, name='content'),
    path('search', views.search, name = 'search'),

]

'''
# ex: /polls/5/
path('<int:question_id>/', views.detail, name='detail'),
# ex: /polls/5/results/
path('<int:question_id>/results/', views.results, name='results'),
# get argument and pass to view
# ex: /polls/5/vote/
path('<int:question_id>/vote/', views.vote, name='vote'),
'''