from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ImageForm
from .models import Image
import pytesseract
import cv2

# Create your views here.
def index(request):
    print(request.POST, request.FILES)
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image')
    else:
        form = ImageForm()

    return render(request,"reader/index.html",{'form':form})

def view_image(request):
    img = Image.objects.all().last()
    text = process_image(img.image.url)
    sound = "base.mp3"
    sound = procces_sound(text)
    return render(request,"reader/image.html",{'img':img, "text":text, "sound":sound})

def process_image(img_path):
    from pathlib import Path
    from django.conf import settings
    path_to_image = str(settings.BASE_DIR) + img_path
    #Point tessaract_cmd to tessaract.exe
    #Open image with cv2
    img = cv2.imread(path_to_image)
    HSV_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(HSV_img)
    thresh = cv2.threshold(v, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    #Extract text from image
    text = pytesseract.image_to_string(thresh, config="--psm 11")
    # Page Segmentation Mode value set to 11, i.e. Sparsing as much text as possible
    return text

def procces_sound(text):
    from pathlib import Path
    from django.conf import settings
    path_to_speech= str(settings.BASE_DIR) + "/" + 'base.mp3'
    from gtts import gTTS
    obj = gTTS(text=text,slow=False)
    obj.save("media/base.mp3")
    return path_to_speech
    

    
