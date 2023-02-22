from django .urls import path
from . import views
from .views import TaskList,TaskCreate,TaskUpdate,TaskDelete,TaskDetailView,Home

urlpatterns =[
   path('', views.Home, name="home"),
   path('login/', views.login_user, name='login'),
   path('logout/', views.logout_user, name='logout'),
   path('register/', views.register_user, name='register'),
   # path('edit_profile/', views.edit_profile, name='edit_profile'),
   path('change_password/', views.change_password, name='change_password'),
   path('task-list/',TaskList.as_view(), name='task1'),
   path('task-create/',TaskCreate.as_view(), name='task-create'),
   path('task-update/<int:pk>/',TaskUpdate.as_view(), name='task-update'),
   path('task-delete/<int:pk>/',TaskDelete.as_view(), name='task-delete'),
   path('task-detail/<int:pk>/',TaskDetailView.as_view(), name='task-detail')
 ]