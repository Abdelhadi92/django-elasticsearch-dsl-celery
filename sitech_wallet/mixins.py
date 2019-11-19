from sitech_wallet.models import Wallet
from sitech_wallet.services import verifyWithdraw, deposit, forceWithdraw, forceTransfer


class HasWallet:

    # The input means in the system
    def deposit(self, amount, meta=None):
        return deposit(self.wallet, amount, meta)

    # Withdrawals from the system
    def withdraw(self, amount, meta=None, force=False):
        if not force:
            verifyWithdraw(self, amount)
        forceWithdraw(self.wallet, amount, meta)

    # Checks if you can withdraw funds
    def canWithdraw(self, amount, allow_zero=False):
        if allow_zero and amount == 0:
            return True

        return self.wallet.balance >= amount

    # A method that transfers funds from host to host
    def transfer(self, wallet, amount, meta=None, force=False):
        if not force:
            verifyWithdraw(self.wallet, amount)
        forceTransfer(self.wallet, wallet, amount, meta)

    # Get the Wallet
    @property
    def wallet(self):
         wallet = Wallet.objects.filter(holder_type=self._meta.label_lower, holder_id=self.id).first()
         if not wallet:
             wallet = Wallet(
                 holder_type=self._meta.label_lower,
                 holder_id=self.id,

             ).save()
         return wallet


