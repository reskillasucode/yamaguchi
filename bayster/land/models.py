from user.models import User
from django.db import models
from user.models import User

# Create your models here.

class Land(models.Model):
  title = models.CharField(max_length = 40)
  address = models.TextField()
  size = models.FloatField()
  purchase_price = models.IntegerField()
  estimated_profit = models.IntegerField()
  cost = models.IntegerField()
  project_background = models.TextField()
  applied_date = models.DateField(auto_now=True)
  STATUS_CHOICE = ((0,'申請中'),(1, '承認'),(2, '却下'))
  status = models.IntegerField(choices=STATUS_CHOICE, default=0)
  user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

  def __str__(self):
    return self.title


class LandReview(models.Model):
  comment = models.TextField()
  land = models.OneToOneField(
    Land,
    on_delete=models.CASCADE,
  )

  def __str__(self):
    return self.land.title
  
  #code 16
  class Review(models.Model):

    def save(self, *args, **kwargs):
        send_mail(
            '案件の評価結果',
            '評価結果: {}'.format(self.result),  # 評価結果を指定
            'from@example.com',
            ['to@example.com'],  # 送信先のメールアドレスを指定
            fail_silently=False,
        )
        super().save(*args, **kwargs)