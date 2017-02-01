# Going to implement Django's form authetication feature
from django.contrib.auth.models

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
		form = IdForm()
	return render(request, 'checkin/sign_in2.html', {'form': form})
