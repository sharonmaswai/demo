from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ["name", "videofile", "audio"]
# class AudioForm(forms.ModelForm):
#     class Meta:
#         model= Video
#         fields= ["name", "audio"]        