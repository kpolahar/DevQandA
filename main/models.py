# ================================================== #
#                    Models File                     #
# ================================================== #

# -------------------- Imports --------------------- #
from django.db import models
from datetime import datetime


# ================================================== #
#                       Models                       #
# ================================================== #


# -------------------------------------------------- #
#                  Model Developer                   #
# -------------------------------------------------- #
class Developer(models.Model):
    '''
        A developer to be described to a potential
          new employer on a page within this application
          by means of a set of questions and answers
    '''
# --- Automatically Generated Library Attributes --- #
    created_on = models.DateTimeField(auto_now_add=True)

# -------------- Developer Attributes -------------- #
    first_name = models.CharField("First Name", blank=True, max_length=32)
    last_name = models.CharField("Last Name", blank=True, max_length=32)
    name = models.CharField("Name", blank=True, max_length=65)
    title = models.TextField("Title", blank=True, max_length=128)
    developer_id = models.CharField("Developer ID", default=datetime.now, help_text="Please give yourself a unique Developer ID, using 16 characters or fewer.", max_length=16, unique=True)


# -------------- Developer Meta Data --------------- #
    class Meta:
        ordering = ['developer_id']

# -------------- Developer Functions --------------- #
    def __str__(self):
        if ((self.name != "") and (self.title != "")):
            return self.name + ", " + self.title
        elif (self.name != ""):
            return self.name
        elif (self.name != ""):
            return self.developer_id
        else:
            return "Unknown"


# -------------------------------------------------- #
#                    Model QandA                     #
# -------------------------------------------------- #
class QandA(models.Model):
    '''
        A question which a developer who is looking
          for a new job may often get asked and to
          which they have prepared a response in
          preparation for their next job interview
    '''
# --- Automatically Generated Library Attributes --- #
    created_on = models.DateTimeField(auto_now_add=True)

# ---------------- QandA Attributes ---------------- #
    question = models.TextField("Question", blank=True, max_length=256)
    answer = models.TextField("Answer", blank=True, max_length=512)
    qanda_id = models.CharField("QandA ID", default=datetime.now, help_text="Please give this a unique QandA ID, using 16 characters or fewer.", max_length=16, unique=True)
    developer_id = models.CharField("Developer ID", blank=True, help_text="Please give your unique 16 character developer ID to ensure this QandA is saved to your developer profile.", max_length=16)

# ---------------- QandA Meta Data ----------------- #
    class Meta:
        ordering = ['created_on']

# ---------------- QandA Functions ----------------- #
    def __str__(self):
        if ((self.question != "") and (self.answer != "")):
            return "Q: " + self.question + "\nA: " + self.answer
        elif (self.question != ""):
            return "Q: " + self.question + "\nA: Unknown"
        else:
            return "Unknown"

    def printQ(self):
        return self.question

    def printA(self):
        return self.answer