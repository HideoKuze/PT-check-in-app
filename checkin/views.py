from .forms import NameForm, IdForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from client_storage import insert
import mysql.connector
from mysql.connector import errorcode
from mysql.connector.errors import Error
import MySQLdb


def sign_in(request):
	#we need to handle all the data that was just typed, we'll add a condition for that
	if request.method == "POST":
		#here will construct the form with the POST data
		form = NameForm(request.POST)
		#the next part is to check that the information submitted is valid
		if form.is_valid():
			post = form.save()
			post.save()
			return HttpResponse(post.question_text)
		else:
			return HttpResponse("Form is invalid")
	else:
		form = NameForm()
	return render(request, 'checkin/base.html', {'form': form})

#this view will be the sign-up view, where new clients will be given new ID numbers for training

def sign_up(request):

	if request.method == "POST":
		form = IdForm(request.POST)
		if form.is_valid():
			post = form.save()
			post.save()
			ID = post.id_text
			#we'll call an external function that checks membership of the users input in the database
			try:
				insert(post.id_text)
				messages.add_message(request, messages.INFO, 'Thank you for signing up ')
				return HttpResponseRedirect('sign_up')
			except:
				if MySQLdb.Error(errno=1062):
					messages.add_message(request, messages.INFO, "Already taken") 
					return HttpResponseRedirect('sign_up')
				else:
					messages.add_message(request, messages.INFO, "Invalid input")
					return HttpResponseRedirect('sign_up')

			# if the user enters a number that is already in use raise an 'duplicate' error
			# Capture the exception here
		else:
			return HttpResponse('That text is invalid')
	else:
		form = IdForm()
	return render(request, 'checkin/base.html', {'form': form})
