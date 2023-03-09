from django.shortcuts import render
from django.http import HttpResponse
import imageio
from PIL import Image
from . import MLmodel, model_covid


def index(request):
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
            else:
                if result_covid > 0.5:
                    context['result'] = 'Covid Positive'
                else:
                    context['result'] = 'Normal'
            # print(result_pneumonia)
            # print(inp)
            print("Yes It had files")
        print(request.POST)
    return render(request, 'main.html', context)

# Create your views here.
