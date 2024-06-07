from django.urls import path
from django.conf import settings  # new
from django.conf.urls.static import static  # new
from .views import global_views, worker_tasks_views, models_views

urlpatterns = [    
    path('', global_views.index, name="index"),
    path('about/', global_views.about, name="about"),
    path('signin/', global_views.signin, name="signin"),
    path('signup/', global_views.signup, name="signup"),
    path('logout/', global_views.signout, name="logout"),

    path('tasks/', worker_tasks_views.tasks, name="tasks"),

    path('task_overview/', models_views.task_overview, name="task_overview"),

    path('register_wash/', worker_tasks_views.register_wash, name='register_wash'),
    path('create_task/', worker_tasks_views.create_task, name='create_task'),

    path('download/', models_views.download_page, name='download_page'),
    path('download_pdf/', models_views.generate_pdf, name='generate_pdf'),
]  


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #new