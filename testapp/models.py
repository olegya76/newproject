from django.db import models

# Create your models here.

class Dolznost(models.Model):
    """Должность сотрудника"""
    dolznost_name = models.CharField(max_length=255, null = False, unique = True)
    oklad = models.FloatField(max_length = 10, null = False)

class Sotrudnik(models.Model):
    """Информация о сотруднике"""
    fam = models.CharField(max_length=255, null = False)
    name = models.CharField(max_length=255, null = False)
    otchestvo = models.CharField(max_length=255, null = False)
    kard_number = models.CharField(max_length=255, null = False)
    otdel = models.IntegerField(null = False)
    passport_number = models.CharField(max_length=255, null = False)
    id_dolznost = models.ForeignKey('Dolznost', on_delete = models.CASCADE, null = False)
    data_priom = models.DateField(null = False)

class Peredacha(models.Model):
    """Информация о передаче"""
    peredacha_name = models.CharField(max_length=255, null = False, unique = True)
    rek_stoim_for_min = models.FloatField(max_length = 10, null = False)
    rating = models.FloatField(max_length = 10, null = False)
    studiya = models.IntegerField(null = False)

class Reklama(models.Model):
    """Информация о  рекламодателе"""
    reklama_name = models.CharField(max_length=255, null = False, unique = True)
    rekvesit = models.CharField(max_length=255, null = False)
    mail = models.CharField(max_length=255, null = False)

class Efir(models.Model):
    """Ефир со временем начала и конца передачи"""
    start_efir = models.DateTimeField(null = False, unique = True)
    stop_efir = models.DateTimeField(null = False, unique = True)
    id_peredacha = models.ForeignKey('Peredacha', on_delete = models.CASCADE, null = False)

class Sotrudnik_in_efir(models.Model):
    """Сотрудник назначеный на определенный ефир"""
    id_sotrudnik = models.ForeignKey('Sotrudnik', on_delete=models.CASCADE, null=False)
    id_efir = models.ForeignKey('Efir', on_delete=models.CASCADE, null=False)

class Reklama_in_efir(models.Model):
    """Реклама которая должна быть во время передачи"""
    id_reklama = models.ForeignKey('Reklama', on_delete = models.CASCADE, null = False)
    id_efir = models.ForeignKey('Efir', on_delete = models.CASCADE, null = False)

# class Sotrudnik_in_efir(models.Model):
#     """Сотрудник назначеный на определенный ефир"""
#     # id = models.AutoField(primary_key=True)
#     id_sotrudnik = models.ForeignKey('Sotrudnik', on_delete = models.CASCADE, null = False)
#     id_efir = models.ForeignKey('Efir', on_delete = models.CASCADE, null = False)

# class Reklama_in_efir(models.Model):
#     """Реклама которая должна быть во время передачи"""
#     # id = models.AutoField(primary_key=True)
#     id_reklama = models.ForeignKey('Reklama', on_delete = models.CASCADE, null = False)
#     id_efir = models.ForeignKey('Efir', on_delete = models.CASCADE, null = False)
