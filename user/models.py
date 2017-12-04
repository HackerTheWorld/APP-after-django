from django.db import models
from datetime import *

class login(models.Model):
    login_ID = models.AutoField(max_length=32,primary_key=True)
    username = models.CharField(max_length=50)
    headimg = models.FileField(upload_to="./uploadhead",null=True)
    password = models.CharField(max_length=50)
    user_id = models.IntegerField(max_length=32,null=True)
    token = models.CharField(max_length=255,null=True)
    class Meta:
        db_table = "login"

class user_info(models.Model):
    user_id = models.AutoField(max_length=32,primary_key=True)
    name = models.CharField(max_length=32,null=True)
    truename = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    carnumber = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    id_card = models.FileField(upload_to="./uploadperson",null=True)
    driver_id = models.FileField(upload_to="./uploaddriver",null=True)
    car_id = models.FileField(upload_to="./uploadcar",null=True)
    class Meta:
        db_table = "user_info"

class version(models.Model):
    versionid = models.AutoField(primary_key=True,default=0)
    version = models.CharField(max_length=10,default=0)
    url = models.CharField(max_length=255,null=True)
    class Meta:
        db_table = "version"

class order(models.Model):
    kuaidi_id = models.AutoField(primary_key=True,default=0)
    order_num = models.CharField(max_length=255,null=True)
    kuaidi_num = models.CharField(max_length=255,null=True)
    getorder_num = models.CharField(max_length=32,null=True)
    make_box_time = models.CharField(max_length=255,null=True)
    make_box_address = models.CharField(max_length=255,null=True)
    phone = models.CharField(max_length=11,null=True)
    person = models.CharField(max_length=255,null=True)
    number = models.FloatField(max_length=255,null=True)
    v =models.FloatField(max_length=32,null=True)
    weight = models.FloatField(max_length=255,null=True)
    voyage_id = models.IntegerField(max_length=255,null=True)
    type = models.IntegerField(max_length=1,default=0)
    take_user_id = models.IntegerField(max_length=32,null=True)
    class Meta:
        db_table = "older"

class voyage(models.Model):
    voyage_id =models.AutoField(primary_key=True,default=0)
    voyage_num = models.CharField(max_length=255,null=True)
    voyage_models = models.CharField(max_length=255,null=True)
    get_box_address = models.CharField(max_length=255,null=True)
    in_return_box = models.CharField(max_length=255,null=True)
    imgname = models.FileField(upload_to="./equipment",null=True)
    take_user_id = models.IntegerField(max_length=32, null=True)
    class Meta:
        db_table = "voyage"

