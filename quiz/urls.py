from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ExamsView, name='home'),
    path('exams/<int:pk>/', views.ExamsDetailView, name='exams_items'),
    path('result/<int:pk>/', views.result_exam, name='result_exam'),
    path('results/<int:pk>/', views.ResultsListView, name='results_list'),
    path('download/<str:path>/', views.download_page_view, name='download'),
    path('add_exam/', views.add_exam, name='add_exam'),
    path('add_quiz/<int:pk>/', views.add_quiz_view, name='add_quiz'),
    path('exam/update/<int:pk>', views.exam_update, name='exam_update'),
    path('exam/delete/<int:pk>', views.exam_delete, name='exam_delete'),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
