# ================================================== #
#                   Root Urls File                   #
# ================================================== #

# -------------------- Imports --------------------- #
from django.conf.urls import url, include
from django.contrib import admin
from main import views

# --------------- Main URL Patterns ---------------- #
main_patterns = [
                  # url home
                  # 'ROOT/'
                  # redirects to the home view
                  url(
                       r'^$',
                       views.home,
                       name='home'
                     ),
                ]

# --------------- Root URL Patterns ---------------- #
urlpatterns = [
                # url admin
                # 'ROOT/admin/'
                # redirects to the django admin view
                url(
                     r'^admin/',
                     include(admin.site.urls),
                     name='admin'
                   ),
                # url namespace main
                # 'ROOT/'
                # includes all url patterns from main_patterns
                url(
                     r'',
                     include(
                              main_patterns,
                              namespace='main'
                            )
                   ),
              ]