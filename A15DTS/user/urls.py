from django.urls import path , include

from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('forgot/', forgot, name='forgot'),
    path('personal/', personal,  name = 'personal'),
    path('logout/', logout, name = 'logout'),
    # path('home/', include('main.urls')),
    # path('author/', AuthorView.as_view(), name='author'),
]
