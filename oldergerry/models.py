from django.db import models

class market_user_pub(models.Model):
    id =  models.AutoField(max_length=11,primary_key=True)
    username = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    net_tel = models.CharField(max_length=100)
    truename = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    post_date = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "market_user_pub"

class market_user_get(models.Model):
    id = models.AutoField(max_length=11,primary_key=True)
    order_id = models.IntegerField()
    user_id = models.IntegerField()
    company = models.CharField(max_length=255,null=True)
    status = models.CharField(max_length=100,null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    company_id = models.CharField(max_length=200,null=True)

    class Meta:
        db_table = "market_user_get"


