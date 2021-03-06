"""drf_sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# initial one ---
# from django.conf.urls import url
# from django.contrib import admin

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]
# end ---

# from rest_framework.routers import DefaultRouter
# from retail.views import ChainViewSet, StoreViewSet, EmployeeViewSet

# router = DefaultRouter()
# router.register(prefix='chains', viewset=ChainViewSet)
# router.register(prefix='stores', viewset=StoreViewSet)
# router.register(prefix='employees', viewset=EmployeeViewSet)

# urlpatterns = router.urls

from django.conf.urls import include,url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from retail.views import ChainViewSet, StoreViewSet, EmployeeViewSet

router = DefaultRouter()
router.register(prefix='chains', viewset=ChainViewSet)
router.register(prefix='stores', viewset=StoreViewSet)
router.register(prefix='employees', viewset=EmployeeViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]