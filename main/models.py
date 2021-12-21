from django.db import models
from django.db.models.base import Model

# омисываем модель сервисов, так как инкремент сам создается, его описывать не нужно
class Servis(models.Model):
    name = models.CharField(max_length=150, null=True)

    # строковое представление объекта
    def __str__(self):
        return f'{self.id}_{self.name}'


# описываем модель сабсервисов, инкремент создается автоматически
class Subservice(models.Model):
    servises_id = models.ForeignKey(Servis, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True)
    price = models.DecimalField(max_digits=15 ,decimal_places=2)
    date = models.DateTimeField(auto_now=True)

    # строковое представление объекта
    def __str__(self):
        return f'{self.id}_{self.name}'