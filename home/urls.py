from django.urls import path
from home import views

urlpatterns = [
    path('', views.home),
    path('template1/<str:nombre>/<str:apellido>', views.template1),
    path('template2/<str:nombre>/<str:apellido>', views.template2),
    path('template3/<str:nombre>/<str:apellido>', views.template3),
    path('test/', views.probando),
    path("autos/crear/<str:marca>/<str:modelo>/", views.crear_auto)
]