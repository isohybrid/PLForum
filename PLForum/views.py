from django.shortcuts import render_to_response

def show_page(request):
  return render_to_response('page.html')
def show_page2(request):
  return render_to_response('show.html')
def show_carousel(request):
  return render_to_response('carousel.html')
