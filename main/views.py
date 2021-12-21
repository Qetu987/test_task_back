from django.shortcuts import render
from .models import Subservice, Servis

# класс для отображения инф на странице
def index(request):
    # тянем все сервисы
    servises = Servis.objects.all()

    # модифицируем данные имен сервисов по соответствию тз
    for servis_index in range(len(servises)):
        subservises = Subservice.objects.filter(servises_id=servises[servis_index])
        over_price = sum(subservise.price for subservise in subservises)
        servises[servis_index].name = f'{servises[servis_index].name} ({len(subservises)}) ({over_price})'

    # тянем параметры запроса, если они есть то выполнимтся return нашего цикла, иначе нижний
    for key, value in request.GET.items():
        servise = Servis.objects.get(id=value)
        subservices = Subservice.objects.filter(servises_id=servise).order_by('-price', 'name')
        return render(request, 'index.html', {'servises': servises, 'subservices': subservices})
        
    # если нет параметров запроса, вернется этот ответ в котором на страницу передаются данные только о сервисах
    # так как данных о сабсервисах не передаются, то они просто не отобразятся на странице
    return render(request, 'index.html', {'servises': servises})
