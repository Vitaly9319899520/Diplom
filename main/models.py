from django.db import models


class AboutPage(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        db_table = 'about'
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.title

class AboutDelivery(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        db_table = 'delivery'
        verbose_name = 'Оплата и доставка'
        verbose_name_plural = 'Оплата и доставка'

    def __str__(self):
        return self.title

class AboutContact(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()


    def __str__(self):
        return self.title
