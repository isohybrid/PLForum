from django.shortcuts import render_to_response

def show_page(request):
  return render_to_response('page.html')
