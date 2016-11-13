from __future__ import unicode_literals

from django.db import models
from django import forms
from django.forms import ModelForm

# Create your models here.

class Question(models.Model):
	question_text = models.CharField("What is your ID?", max_length=200)
	#pub_date = models.DateTimeField('date published')

	id_text = models.CharField("Enter a new identification number", max_length=200, null=True)

	def __str__(self):
		return self.question_text 