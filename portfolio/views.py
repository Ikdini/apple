from django.http import HttpResponse
import mimetypes, os
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

from .forms import ContactForm

# Create your views here.
def index(request):
  # checking if a POST request was made.
  if request.method == "POST":
    # creating a form instance and populating it with data from the request.
    form = ContactForm(request.POST)
    # checking whether populated data is valid.
    if form.is_valid():
      # cleaning the data into subject and body variables.
      subject = f"Email from Portfolio: {form.cleaned_data['subject']}"
      body = {
        "name": form.cleaned_data["name"],
        "email_address": form.cleaned_data["email_address"],
        "message": form.cleaned_data["message"]
      }

      # creating the message to be sent.
      message = f"Name: {body['name']}\nEmail: {body['email_address']}\n\n{body['message']}"

      # sending the email.
      try:
        send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.RECIPIENT_ADDRESS])
      except BadHeaderError:
        return HttpResponse('Invalid header found.')

      # redirecting to the home page with a success message. 
      form = ContactForm()
      return render(request, "portfolio/index.html", {
        "message": "Email Sent Successfully",
        "form": form
      })
    # if the data is not valid, return the form with error message.
    else:
      return render(request, "portfolio/index.html", {
        "message": "Error!!!!! Email Not Sent",
        "form": form
      })
  # default view of the page.
  form = ContactForm()
  return render(request, "portfolio/index.html", {"form": form})

def download_resume(request):
  current_path = os.path.dirname(__file__)
  filename = "Ifeoluwapo_Oluwande_Resume.pdf"
  fl_path = os.path.join(current_path, "static/portfolio/others/") + filename

  fl = open(fl_path, 'rb')
  mime_type, _ = mimetypes.guess_type(fl_path)
  response = HttpResponse(fl, content_type=mime_type)
  response['Content-Disposition'] = "attachment; filename=%s" % filename
  return response