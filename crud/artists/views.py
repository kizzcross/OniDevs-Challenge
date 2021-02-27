from django.shortcuts import render, redirect
from .forms import MusicForm
from .models import *

# Create your views here.

def music_list(request):
    context = {'music_list': Music.objects.all()}
    return render(request, "music_register/music_list.html", context)



def music_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = MusicForm()
        else:
            music = Music.objects.get(pk=id)
            form = MusicForm(instance=music)
        return render(request, "music_register/music_form.html", {'form': form})
    else:
        if id == 0:
            form = MusicForm(request.POST)
        else:
            music = Music.objects.get(pk=id)
            form = MusicForm(request.POST,instance= music)
        if form.is_valid():
            form.save()
        return redirect('/list')


def music_delete(request,id):
    music = Music.objects.get(pk=id)
    music.delete()
    return redirect('/list')


