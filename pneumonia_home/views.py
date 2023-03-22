from django.shortcuts import render
from django.http import HttpResponse
import imageio
from PIL import Image
from . import MLmodel, model_covid


def index(request, home=None):
    if home :
        context = {}
        if request.method == 'POST':
            if request.FILES['images']:
                image = imageio.imread(request.FILES.get('images'))
                inp = Image.open(request.FILES.get('images'))
                result_pneumonia = MLmodel.model_call(inp)
                result_covid = model_covid.model_call(inp)
                # print(result_covid, 'result_covid')
                context['result'] = result_pneumonia
                if result_pneumonia == 'Positive':
                    context['result'] = 'Pneumonia Positive'
                    context['image_url'] = '../static/PNEUMONIA_RESULT.jpg'
                else:
                    if result_covid > 0.5:
                        context['result'] = 'Covid Positive'
                        context['image_url'] = '../static/covid_result.jpeg'
                    else:
                        context['result'] = 'Normal'
                        context['image_url'] = '../static/Normal_result_GIF.gif'
                # print(result_pneumonia)
                # print(inp)
                print("Yes It had files")
            print(request.POST)
        return render(request, 'main.html', context)
    else:
        return render(request, 'index1.html')

# Create your views here.
