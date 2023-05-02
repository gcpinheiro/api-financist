from django.db import models
from apps.users.models import UserModel

# Create your models here.

class FinancialAccount(models.Model):
    id_account = models.AutoField(primary_key=True)
    id_users = models.ForeignKey(UserModel, on_delete=models.CASCADE, db_column='id_users')
    name_purchase = models.CharField(max_length=50)
    purchase_date = models.DateTimeField()
    payment_date = models.DateTimeField()
    installment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    number_installments = models.IntegerField()
    current_payment_installments = models.IntegerField()
    type_purchase = models.CharField(max_length=20)
    purchase_category = models.CharField(max_length=20)
    total_purchase = models.DecimalField(max_digits=10, decimal_places=2)

    
    class Meta:
      managed = False
      db_table = 'financial_account'