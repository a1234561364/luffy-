
from django.urls import path,re_path,include
from . import views
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('',views.LoginView,'login')
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
