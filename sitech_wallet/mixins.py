from sitech_wallet.models import Wallet
from sitech_wallet.services import verify_withdraw, deposit, force_withdraw, force_transfer


class HasWallet:

    # The input means in the system
    def deposit(self, amount, meta=None):
        return deposit(self.wallet, amount, meta)

    # Withdrawals from the system
    def withdraw(self, amount, meta=None, force=False):
        if not force:
            verify_withdraw(self, amount)
        force_withdraw(self.wallet, amount, meta)

    # Checks if you can withdraw funds
    def can_withdraw(self, amount, allow_zero=False):
        if allow_zero and amount == 0:
            return True

        return self.wallet.balance >= amount

    # A method that transfers funds from host to host
    def transfer(self, wallet, amount, meta=None, force=False):
        if not force:
            verify_withdraw(self.wallet, amount)
        force_transfer(self.wallet, wallet, amount, meta)

    # Get the Wallet
    @property
    def wallet(self):
         wallet = Wallet.objects.filter(holder=self).first()
         if not wallet:
             wallet = Wallet(holder=self).save()
         return wallet

    # Get the balance
    @property
    def balance(self):
        return self.wallet.balance


