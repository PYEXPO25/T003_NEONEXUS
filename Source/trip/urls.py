from django.urls import path  # type: ignore
from .views import home, Routepage, AllHiddenSpots, login_view, logout_view

urlpatterns = [
    path('home/', home, name='home'),
    path('route/', Routepage, name='route'),
    path('hide/', AllHiddenSpots, name='hidden_spots'),
    path('login/', login_view, name='login'),  # Corrected to `login_view`
    path('logout/', logout_view, name='logout'),
]
