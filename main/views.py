# ================================================== #
#                     Views File                     #
# ================================================== #

# -------------------- Imports --------------------- #
from django.shortcuts import get_object_or_404, render
from main import models


# ================================================== #
#                       Views                        #
# ================================================== #

# -------------------------------------------------- #
#                     View home                      #
# -------------------------------------------------- #
def home(request):
    ''' Displays the home view '''
    return render(request, 'main/home.html')


# -------------------------------------------------- #
#                  View developers                   #
# -------------------------------------------------- #
def developers(request):
    ''' Displays the developers view '''
    developers = models.Developer.objects.all()
    return render(request, 'main/developers.html', {'developers': developers})


# -------------------------------------------------- #
#                   View developer                   #
# -------------------------------------------------- #
def developer(request, developer_id):
    ''' Displays the developer details view '''
    developer = get_object_or_404(models.Developer, developer_id=developer_id)
    QandAs = models.QandA.objects.filter(developer_id=developer_id)
    return render(request, 'main/developer.html', {'developer': developer, 'QandAs': QandAs})