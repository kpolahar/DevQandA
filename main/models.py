# ================================================== #
#                    Models File                     #
# ================================================== #

# -------------------- Imports --------------------- #
from django.db import models


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
    name = models.CharField("Name", max_length=64)
    title = models.TextField("Title", max_length=128)


# -------------- Developer Meta Data --------------- #
    class Meta:
        ordering = ['created_on']

# -------------- Developer Functions --------------- #
    def __str__(self):
        if ((self.name != "") and (self.title != "")):
            return self.name + ", " + self.title
        elif (self.name != ""):
            return self.name
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
    question = models.TextField("Question", max_length=256)
    answer = models.TextField("Answer", max_length=512)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)

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