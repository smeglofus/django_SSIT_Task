from django.urls import path

from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]


""" SQL prikaz
SELECT
    t.time,
    SUM(CASE WHEN t.choice_id = 1 THEN t.vote_count ELSE 0 END) AS "Choice 1",
    SUM(CASE WHEN t.choice_id = 2 THEN t.vote_count ELSE 0 END) AS "Choice 2",
    SUM(CASE WHEN t.choice_id = 3 THEN t.vote_count ELSE 0 END) AS "Choice 3"
FROM polls_timechoice t
LEFT JOIN (
    SELECT id, choice_text FROM polls_choice
) c ON t.choice_id = c.id
GROUP BY t.time

"""