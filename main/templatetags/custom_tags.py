# ================================================== #
#                  Custom Tags File                  #
# ================================================== #

# -------------------- Imports --------------------- #
from django import template
from main import models


register = template.Library()


# ================================================== #
#                    General Tags                    #
# ================================================== #


# -------------------------------------------------- #
#                 Tag developers_url                 #
# -------------------------------------------------- #
@register.simple_tag()
def developers_url():
    '''
        Returns the developers url
    '''
    return '/developers/'



# -------------------------------------------------- #
#                 Tag developer_url                  #
# -------------------------------------------------- #
@register.simple_tag()
def developer_url(Developer):
    '''
        Returns a developer's url as a formatted string
    '''
    return '/developers/{}/'.format(Developer.developer_id)

# -------------------------------------------------- #
#              Tag developer_thumbnail               #
# -------------------------------------------------- #
@register.inclusion_tag('main/developer_thumbnail.html')
def developer_thumbnails():
    '''
        Renders a template for displaying a thumbnail
        link to the correct developer details page
    '''
    developers = models.Developer.objects.all().filter()
    return {'developers': developers}



# ================================================== #
#                 External Link Tags                 #
# ================================================== #

# -------------------------------------------------- #
#                     Tag github                     #
# -------------------------------------------------- #
@register.inclusion_tag('main/external_link.html')
def github(Developer):
    '''
        Renders a template for displaying a link
        to a developer's github profile
    '''
    return {
             'icon': '../../static/images/github-logo.svg',
             'link': 'http://www.github.com/{}'.format(Developer.github),
             'label': 'View my source code on GitHub'
           }

# -------------------------------------------------- #
#                    Tag linkedin                    #
# -------------------------------------------------- #
@register.inclusion_tag('main/external_link.html')
def linkedin(Developer):
    '''
        Renders a template for displaying a link to
        a developer's linkedin profile
    '''
    return {
             'icon': '../../static/images/linkedin-logo.svg',
             'link': 'http://www.linkedin.com/in/{}'.format(Developer.linkedin),
             'label': 'Connect with me on LinkedIn'
           }