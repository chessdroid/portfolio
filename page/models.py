from django.db import models


class About(models.Model):
	name = models.CharField(verbose_name="Имя", max_length=128)
	surname = models.CharField(verbose_name="Фамилия", max_length=128)
	job = models.CharField(verbose_name="Профессия", max_length=128, blank=True)
	desc =  models.TextField(verbose_name="Описание")
	image = models.ImageField(verbose_name='Изображение', max_length=512, upload_to='news/medium', blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'О себе'
		verbose_name_plural = "О себе"


class Project(models.Model):
	title = models.CharField(verbose_name="Название", max_length=128)
	image = models.ImageField(verbose_name='Изображение', max_length=512, upload_to='news/medium', blank=True)
	desc =  models.CharField(verbose_name="Описание", max_length=128)
	pdf_file = models.FileField(upload_to='news/medium', blank=True)
	
	def __str__(self):
		return self.title
	
	class Meta:
		verbose_name = 'Проекты'
		verbose_name_plural = "Проекты"