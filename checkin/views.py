from .forms import NameForm, IdForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from client_storage import id_storage

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
			if post.id_text in id_storage.clients:
				messages.add_message(request, messages.INFO, 'That ID is already taken, please try again ')
				return HttpResponseRedirect('sign_up')
			else:
				messages.add_message(request, messages.INFO, 'Thank you your ID is ' + post.id_text)
				id_storage.clients.append(post.id_text)
				HttpResponseRedirect('sign_in')
		else:
			return HttpResponse('That text is invalid')
	else:
		form = IdForm()
	return render(request, 'checkin/base.html', {'form': form})
