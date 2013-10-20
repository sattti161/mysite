from django.db import models

class Transactions(models.Model):
    user_id = models.IntegerField()
    item = models.CharField(max_length = 200) # user_id + firstTime Update time stamp ----> Item
    quantity = models.IntegerField()
    lent_borrowed_flag = models.BooleanField() # true - lent, false - borrowed
    person = models.CharField(max_length = 200) 
    date_init = models.DateTimeField() # when lent
    date_due = models.DateTimeField() # when lent 
    status = models.BooleanField() # pending the return or not
    
class UserEmail(models.Model):
    email_id = models.CharField(primary_key=True, max_length = 200)
    password = models.CharField(max_length = 200)
    user_id = models.IntegerField()

class UserDetails():
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length = 200)
    default_remainder = models.BooleanField() # 0 - message, 1 - email
    

class UserLents(models.Model):
    user_id = models.IntegerField() #----> UserDetails
    item = models.CharField(max_length = 200) # user_id + firstTime Update time stamp ----> Item
    lent_to = models.CharField(max_length = 200) 
    date_lent = models.DateTimeField() # when lent 
    status = models.BooleanField() # pending the return or not
   

class UserBorrows(models.Model):
    user_id = models.IntegerField() #----> UserDetails
    item_id = models.CharField(max_length = 200) # user_id + firstTime Update time stamp ----> Item  
    borrowed_from = models.CharField(max_length = 200) 
    date_borrowed = models.DateTimeField() # when lent
    status = models.BooleanField() # pending the return or not   


class Item(models.Model):
    item_id = models.CharField(primary_key=True, max_length = 200) # user_id + firstTime Update time stamp ----> Item
    item_name = models.CharField(max_length = 200)
    item_description = models.CharField(max_length = 500)
    quantity = models.IntegerField()         