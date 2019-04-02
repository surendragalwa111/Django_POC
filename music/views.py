from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Song

# Create your views here.

def index(request):
  all_songs = Song.objects.all()
  # template = loader.get_template('music/index.html')
  context= {
    'all_songs': all_songs,
  }
  # return HttpResponse(template.render(context, request))
  return render(request, 'music/index.html', context)

def detail(request, album_id):
  # try:
  #   song = Song.objects.get(pk= album_id)
  # except Song.DoesNotExist:
  #   raise Http404("Song does not exist")
  song = get_object_or_404(Song, pk=album_id)

  return render(request,'music/detail.html', {'song' : song})

def favourite(request, album_id):
  song = get_object_or_404(Song, pk=album_id)
  try:
    selected_album=song.album_set.get(pk=request.POST['album'])
  except (KeyError, Song.DoesNotExist):
    return render(request, 'music/detail.html', {
      'song': song,
      'error_message': 'You did not select a valid song'
    })
  else:
    selected_album.is_favourite = True
    selected_album.save()
    return render(request, 'music/detail.html', {
      'song': song
    })