from sitech_wallet import exceptions
from sitech_wallet.models import Transaction


def checkAmount(amount):
    if amount < 0:
        raise exceptions.AmountInvalid()


def verifyWithdraw(holder, amount):
    if not holder.canWithdraw(amount):
        raise exceptions.InsufficientFunds()


def deposit(wallet, amount, meta=None):
    checkAmount(amount)

    wallet.balance += amount
    wallet.save()

    transaction = Transaction(
        type=Transaction.TYPE_WITHDRAW,
        amount=amount,
        from_wallet=wallet,
        meta=meta
    ).save()
    return transaction


def forceWithdraw(wallet, amount, meta=None):
    checkAmount(amount)

    wallet.balance -= amount
    wallet.save()

    transaction = Transaction(
        type=Transaction.TYPE_WITHDRAW,
        amount=amount,
        from_wallet=wallet,
        meta=meta
    ).save()
    return transaction


def forceTransfer(from_wallet, to_wallet, amount, meta=None):
    checkAmount(amount)

    from_wallet.balance -= amount
    from_wallet.save()
    withdraw = Transaction(
        type=Transaction.TYPE_WITHDRAW,
        amount=amount,
        from_wallet=from_wallet,
        to_wallet=to_wallet,
        meta=meta
    ).save()

    to_wallet.balance += amount
    to_wallet.save()
    deposit = Transaction(
        type=Transaction.TYPE_DEPOSIT,
        amount=amount,
        from_wallet=to_wallet,
        to_wallet=from_wallet,
        meta=meta
    ).save()

    return [withdraw, deposit]
