from django.db import models
 
class Account(models.Model):
    ACC_ID = models.AutoField(primary_key=True)
    ACC_FNAME = models.CharField(max_length=50)
    ACC_MNAME = models.CharField(max_length=50, blank=True, null=True)
    ACC_LNAME = models.CharField(max_length=50)
    ACC_USERNAME = models.CharField(max_length=50)
    ACC_EMAIL = models.EmailField(max_length=100)
    ACC_PASSWORD = models.CharField(max_length=150)
    ACC_GENDER = models.CharField(max_length=6, blank=True, null=True)
    ACC_SALT = models.CharField(max_length=100, blank=True, null=True)
    ACC_PROFILE = models.BinaryField(blank=True, null=True)
    ACC_DOB = models.DateField(blank=True, null=True)
    ACC_REGION = models.CharField(max_length=50, blank=True, null=True)
    ACC_PROVINCE = models.CharField(max_length=50, blank=True, null=True)
    ACC_STATUS = models.CharField(max_length=20, blank=True, null=True)
    ACC_TYPE = models.CharField(max_length=1, default='P')
    DATE_CREATED = models.DateTimeField(auto_now_add=True)
    DATE_UPDATED = models.DateTimeField(auto_now=True)

class Balance(models.Model):
    BLN_ID = models.AutoField(primary_key=True)
    BLN_AMOUNT = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    BLN_TOTAL = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ACC_ID = models.ForeignKey(Account, on_delete=models.CASCADE)

class Progress(models.Model):
    PRG_ID = models.AutoField(primary_key=True)
    PRG_HISTORY = models.CharField(max_length=20)
    PRG_QUEST = models.CharField(max_length=20)
    PRG_WINS = models.IntegerField(default=0)
    PRG_LOSSES = models.IntegerField(default=0)
    DATE_CREATED = models.DateTimeField(auto_now_add=True)
    DATE_UPDATED = models.DateTimeField(auto_now=True)
    ACC_ID = models.ForeignKey(Account, on_delete=models.CASCADE)

class Item(models.Model):
    ITEM_ID = models.AutoField(primary_key=True)
    ITEM_NAME = models.CharField(max_length=50)
    ITEM_SPRITE = models.BinaryField(blank=True, null=True)
    ITEM_HOLDER = models.CharField(max_length=20)
    ITEM_VALUE = models.DecimalField(max_digits=12, decimal_places=2)
    ITEM_TYPE = models.CharField(max_length=1)
    ITEM_STATUS = models.CharField(max_length=20, blank=True, null=True)
    DATE_CREATED = models.DateTimeField(auto_now_add=True)
    DATE_UPDATED = models.DateTimeField(auto_now=True)

class Inventory(models.Model):
    INV_ID = models.AutoField(primary_key=True)
    ACC_ID = models.ForeignKey(Account, on_delete=models.CASCADE)
    ITEM_ID = models.ForeignKey(Item, on_delete=models.CASCADE)

class Offer(models.Model):
    OFR_ID = models.AutoField(primary_key=True)
    OFR_NAME = models.CharField(max_length=50)
    OFR_VALUE = models.DecimalField(max_digits=12, decimal_places=2)
    OFR_PRICE = models.DecimalField(max_digits=12, decimal_places=2)
    OFR_SPRITE = models.BinaryField(blank=True, null=True)
    OFR_DESC = models.CharField(max_length=50, blank=True, null=True)
    OFR_STATUS = models.CharField(max_length=20, blank=True, null=True)
    DATE_CREATED = models.DateTimeField(auto_now_add=True)
    DATE_UPDATED = models.DateTimeField(auto_now=True)

class Notification(models.Model):
    NTF_ID = models.AutoField(primary_key=True)
    NTF_TITLE = models.CharField(max_length=20)
    NTF_MESSAGE = models.CharField(max_length=50)
    NTF_TYPE = models.CharField(max_length=1, default='G')
    DATE_CREATED = models.DateTimeField(auto_now_add=True)
    DATE_UPDATED = models.DateTimeField(auto_now=True)
    ACC_ID = models.ForeignKey(Account, on_delete=models.CASCADE)

class History(models.Model):
    HIS_ID = models.AutoField(primary_key=True)
    HIS_MODE = models.CharField(max_length=20, blank=True, null=True)
    HIS_TYPE = models.CharField(max_length=20, blank=True, null=True)
    DATE_CREATED = models.DateTimeField(auto_now_add=True)
    OFR_ID = models.ForeignKey(Offer, on_delete=models.CASCADE, blank=True, null=True)
    ITEM_ID = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)
    ACC_ID = models.ForeignKey(Account, on_delete=models.CASCADE)

class UserLog(models.Model):
    LOG_ID = models.AutoField(primary_key=True)
    LOG_TYPE = models.CharField(max_length=20)
    LOG_ORIGIN = models.CharField(max_length=20)
    LOG_DESCRIPTION = models.CharField(max_length=20)
    LOG_IP_ADDRESS = models.CharField(max_length=20, blank=True, null=True)
    DATE_CREATED = models.DateTimeField(auto_now_add=True)
    ACC_ID = models.ForeignKey(Account, on_delete=models.CASCADE)

class Feedback(models.Model):
    FDBK_ID = models.AutoField(primary_key=True)
    FDBK_TYPE = models.CharField(max_length=20)
    FDBK_TITLE = models.CharField(max_length=50)
    FDBK_MESSAGE = models.CharField(max_length=100)
    DATE_CREATED = models.DateTimeField(auto_now_add=True)
    ACC_ID = models.ForeignKey(Account, on_delete=models.CASCADE)
 