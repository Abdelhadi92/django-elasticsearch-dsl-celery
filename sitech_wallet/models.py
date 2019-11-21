from django.db import models
from jsonfield import JSONField
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Wallet(models.Model):
    holder_type = models.ForeignKey(ContentType, verbose_name='Holder Type', on_delete=models.CASCADE)
    holder_id = models.PositiveIntegerField('Holder Id', db_index=True)
    holder = GenericForeignKey('holder_type', 'holder_id')
    balance = models.DecimalField(default=0, max_digits=8, decimal_places=3, verbose_name='Balance')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Updated At')


class Transaction(models.Model):
    TYPE_DEPOSIT = 1
    TYPE_WITHDRAW = 2
    type = models.IntegerField(verbose_name='Type', choices=[(TYPE_DEPOSIT, 'deposit'), (TYPE_WITHDRAW, 'withdraw')], db_index=True)
    from_wallet = models.ForeignKey(Wallet, related_name='from_wallet', on_delete=models.CASCADE, null=True)
    to_wallet = models.ForeignKey(Wallet, related_name='to_wallet', on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=3, verbose_name='Amount')
    meta = JSONField(null=True, verbose_name='Meta')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Updated At')
