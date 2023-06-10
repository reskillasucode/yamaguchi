from django.db import models

# Create your models here.
class Land(models.Model):
    title = models.CharField(max_length=100)
    address = models.TextField()
    size = models.FloatField()
    purchase_price = models.IntegerField()
    estimated_profit = models.IntegerField()
    cost = models.IntegerField()
    project_background = models.TextField()
    #applied_dateは営業担当者が案件申請をした日付が入ります
    applied_date = models.DateField(auto_now=True)
    #statusは案件の現状を示すものとし、申請中、承認、却下の3種類として下さい
    STATUS_CHOICE = ((0,'申請中'),(1, '承認'),(2, '却下'))
    status = models.IntegerField(choices=STATUS_CHOICE, default=0)
    def __str__(self):
        return self.title  


class LandReview(models.Model):
  comment = models.TextField()
  land = models.OneToOneField(
    Land,
    on_delete=models.CASCADE,
  )