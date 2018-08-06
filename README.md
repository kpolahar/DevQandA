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

### Prerequisites

This project is for the most part complete, for the purpose that it was given to me, though there is much polishing up yet which could be done.

Git
Python 2.7 or later
Pip (upgrade from default installed with Python is recommended)
7Zip (or a similar program, to extract the Django files)
Django 1.11.15 or later

##### To Install Git

Git provides an excellent guide on getting started and installing Git on their site, which can be found [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

##### To Install Python

You only need Python 2.7 or later to run this project. I have not tried running it with Python 3.X or later yet, and I am not positive if it is compatible or not. I will attempt to find out for sure when I have time and post an update here.

I found a handly little guide for installing Python 2.7 on Google's Open Online Education site. It includes detailed instructions for ensuring that the Python executable is added to the Path. This guide can be found [here](https://edu.google.com/openonline/course-builder/docs/1.10/set-up-course-builder/check-for-python.html).

##### To Upgrade Pip

Assuming you have Python installed, it is recommended that you upgrade pip before attempting to use it to install Django.

 - On Linux or macOS
     pip install -U pip
 - On Windows
     python -m pip install -U pip

For more help with pip, see their documentation [here](https://pip.pypa.io/en/stable/installing/#upgrading-pip).

##### To Install Django

Once you have Python installed and pip up to date, you'll want to install Django. Again, you'll notice we're not working with the latest version of Django. I'll try to come back and see if this plays nicely with the latest version later. For now, here are instructions for installing version 1.11.15, which is sufficient to run this program locally on your machine.

 - Click [here](https://www.djangoproject.com/download/1.11.15/tarball/) to download the file 'Django-1.11.15.tar.gz'
 - You will probably need to click [here](https://www.7-zip.org/) to install 7Zip to extract the files after it downloads
 - For those as easily confused as myself, you may need to extract the files twice, once for the gz layer, and once for the tar layer
 - Rename the 'dist' folder to 'Django' and move it to your program files folder
 - In the commmand line, navigate to the program files folder and run the following command
 - python -m pip install -e django/

You should now have everything you need installed to run the site. If you have any issues, please feel free to email me at *kpolahar@gmail.com*.


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