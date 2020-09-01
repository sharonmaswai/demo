from django.shortcuts import render
from django.http  import HttpResponse
from .models import Video
from .forms import VideoForm



# Create your views here.
def index(request):
    return render(request, 'index.html')


def video_upload(request):

    # lastvideo= Video.objects.all()

    # # videofile= lastvideo.videofile
    


    form= VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    
    form = VideoForm(request.POST, request.FILES)
              
    
      
    return render(request, 'videos.html', {'form':form})

# def audio_upload(request):

#     # lastvideo= Video.objects.all()

#     # # videofile= lastvideo.videofile
    


#     form= AudioForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()

    
#     form = AudioForm(request.POST, request.FILES)
              
    
      
#     return render(request, 'audio.html', {'form':form})    
def show_video(request):
    videos= Video.objects.all()
   
    score=4.37
    

    return render(request, 'vid.html', {'score':score, 'videos':videos}) 
   



