# ================================================== #
#                   Root Urls File                   #
# ================================================== #

# -------------------- Imports --------------------- #
from django.conf.urls import url, include
from django.contrib import admin
from main import views


# ------------ Developers URL Patterns ------------- #
developers_patterns = [
                      # url developer
                      # 'ROOT/developer/{{ developer_id }}/'
                      # redirects to the developer view
                      url(
                           r'(?P<developer_id>[0-9A-Za-z\-]+)/$',
                           views.developer,
                           name='developer'
                         ),
                      # url developers
                      # 'ROOT/developers/'
                      # redirects to the developers view
                      url(
                           r'^$',
                           views.developers,
                           name='developers'
                         )
                    ]

# --------------- Main URL Patterns ---------------- #
main_patterns = [
                  # url namespace developers
                  # 'ROOT/developers/'
                  # includes all url patterns from developers
                  url(
                       r'^developers/',
                       include(
                                developers_patterns,
                                namespace='developers'
                              )
                     ),
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