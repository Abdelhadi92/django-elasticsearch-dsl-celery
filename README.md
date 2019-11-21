
# Sitech Django Wallet


## Installation

1. Run the [pip](https://pip.pypa.io/en/stable/) command to install the latest version:
```bash
 pip install git+https://github.com/sitmena/sitech-django-wallet.git@v0.1
```

2. Add `sitech_wallet` to your `INSTALLED_APPS` in settings.py:
```bash
 INSTALLED_APPS = (
    ...
    'sitech_wallet',
 )
```
3. Run the migration command:
```bash
 python manage.py migrate
```
<br>

## Usage
Add the  `HasWallet`  maixin to your model.

```python
from django.db import models
from sitech_wallet import HasWallet

class Profile(models.Model, HasWallet):  
	phone = models.CharField(max_length=255, verbose_name='Phone')
	address = models.TextField(max_length=512,verbose_name='Address')
```	

Then you can easily make transactions from your model.
```python
profile = Profile.objects.get(pk=1)
profile.wallet.balance // 0
  
profile.deposit(100)
profile.wallet.balance // 100

profile.withdraw(20)
profile.wallet.balance // 80
```	

**Remember ,** you may use the `sitech_wallet.HasWallet` mixin on any of your models. You are not limited to only including it on your `Profile`model.
