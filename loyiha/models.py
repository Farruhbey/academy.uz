from django.db import models

class Talabalar(models.Model):
    ismi = models.CharField(max_length = 1000)
    familiyasi = models.CharField(max_length = 1000)
    malumoti = models.CharField(max_length = 1000)
    holati = models.CharField(max_length = 1000)
    
    yoshi = models.IntegerField(null=True)
    biladigan_dasturlash_tili = models.CharField(max_length = 100, null=True)
    rasmi = models.ImageField()
    darajasi = models.CharField(max_length = 1000)
    
    

    def __str__(self) -> str:
        return f'{self.ismi} {self.familiyasi} '

class Loyiha(models.Model):
    nomi = models.CharField(max_length = 400)
    sisilka = models.CharField(max_length = 400)
    rasmi = models.ImageField()
    talaba = models.ForeignKey(Talabalar, related_name="loyihalar", on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.nomi

class Eng_yaxshi(models.Model):
    darajasi = models.CharField(max_length = 100)
    loyihasi = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.loyihasi
       

      
# Create your models here.
