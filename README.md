# About DevQandA

The purpose of this project is for me to demonstrate my skills, coding style, and perhaps most importantly, my work process, to a potential employer and their development team, to help them determine whether or not I would be a good fit for their team and its needs.


# The Assignment

### User Story

As a developer looking for a job I would like an application that answers common questions I'm asked by hiring managers.

### Acceptance Criteria

 - The hiring manager should be able to obtain answers to the following questions about you:

   - What is your favorite programming language, and why?
   - Tabs or spaces, and why?
   - Do you have a Stack Overflow account?
   - What does JSON stand for?

 - There should be at least one easter-egg feature built into the application which should be accessible to the hiring manager, but they wouldn't know about it unless they read the source code.


# The Plan

Add the secret easter egg to make *the secret thing happen* when the user *does the secret thing*

### More Project Specific User Stories

I have broken this user story out into smaller ones more specific to the project as I have decided to tackle it

 - As a developer using this application, I need a web page which displays the profile I have created for myself in the database
 - As a developer using this application, I need a way to store my personal profile data in the database
 - As a developer using this application, I need a way to store a question I am commonly asked by a hiring manager and its corresponding answer in the database. It is important that this question be able to be linked back to my profile in some way, so that it can be displayed on my web page. - *It is possible that this should be split into two use cases. I am not positive. It is also possible that if I could find a way to word it better, it is perfectly fine as one use case.*
 - As a developer using this application, I would like to also be able to share my GitHub and LinkedIn profiles directly with a potential hiring manager from my developer profile, so that they can have direct access to any additional information about me which they may need.
 - As a potential hiring manager visiting this web page, I would like to be able to view a list of potential developers from the database so that I can have easy access to their individual profiles.
 - As a potential hiring manager visiting this web page, I would like to be able to view a the individual profile of a developer, so that I can review their lists of answers to commonly asked questions.


# To Run

###Prerequisites

This project is for the most part complete, for the purpose that it was given to me, though there is much polishing up yet which could be done.

I will do my best to post more thorough instructions on how to run the project even if you do not already have the prerequisites installed as soon as I have an opportunity to borrow a computer which does not already have them installed. All of the instructions I have managed to find by Googling seem to make the assumption that you are building the project yourself, and I wish to post more complete instructions for those who are taking this project which is already built and attempting to run it on a system which does not yet have the prerequisite software installed. Unfortunately, my only computer which did not has been loaned out to a friend who is taking a class on Linux system administration, and was thrilled to find I had a laptop with Ubuntu just lying around that she could borrow for a few weeks...

For the more tech savvy, the following instructions should hopefully suffice. If not, please do feel free to contact me for a chat to help you set it up. I would have hosted it on my website, but my site is down because I'm in the middle of changing hosting providers, partially because my current hosting service claimed to support Django, but only supported older versions of Django...

So. With no further ado...

Python 2.7 or later
Django 1.11.15 or later
Git

You may need to install pip to install one or both of these.
I will hopefully have more precise instructions for installing these posted later today.

### Running the Site

Assuming you have Python and Django installed, then to run this site locally on your machine:
 - Open your command prompt or terminal and navigate into the directory where you would like to clone the DevQandA repository
 - Run the following commands
 - git clone https://github.com/kpolahar/DevQandA.git
 - cd DevQandA
 - python manage.py makemigrations
 - python manage.py migrate
 - python manage.py runserver
 - Open your favorite browser and navigate to your localhost url
     - The terminal window will tell you what this is if you don't know it
     - If it is not 'http://127.0.0.1:8000/', you may need to open the 'settings.py' file and add your localhost to the data set 'ALLOWED_HOSTS'

### Adding New Data to the Database

If you would like to add additional developers or questions to the database, you can use the 'create_data.txt' file to determine the necessary lines of code needed to create a new model.

 - In a new terminal window, still in the DevQandA directory, run the following command
 - python manage.py shell
 - Once inside the python shell, run the following import
 - from main.models import *
 - You can then create any new Developer or QandA models to add to the database
 - These new developers will be visible from the list of developers on the site and will have their own developer page on the site
 - If you add an image file titled '[developer_id].png' to the images folder of the project files, it will automatically be displayed on the developer's portfolio page
 - If you add a new question, the 'developer_id' property of the question needs to be set to the 'developer_id' of the developer whose page the question should appear on
 - Make sure you save all developers and questions you add
 - If everything gets messed up, you can competely wipe the db.sqlite3 file and reset it from the 'create_data.txt' file - I've done that several times this weekend

 Please feel free to message me if you have any questions! ^_^

Thanks,
Kate