<<<<<<< HEAD
from django.conf.urls import url
from IT import views as DemoViews

urlpatterns = [
    url(r'^$', DemoViews.index),
    url(r'^json$', DemoViews.jsonTest)
=======
from django.conf.urls import url
from IT import views as DemoViews
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', DemoViews.index),
    url(r'^json$', DemoViews.jsonTest),
    url(r'^admin', TemplateView.as_view(template_name='IT/Admin/index.html'))
>>>>>>> b6ed3cb0427fc3b30fe2f4b569908246cfec5690
]