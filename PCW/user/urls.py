from django.urls import path
from .views import sign_up, SignIn, Logout

urlpatterns = [
    path('sign-in', SignIn.as_view(), name='sign-in'),
    path('logout', Logout.as_view(), name='logout'),
    path('sign-up', sign_up, name='sign-up'),

]
