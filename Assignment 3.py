from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f"₹{amount} paid using Credit Card.")


class DebitCardPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f"₹{amount} paid using Debit Card.")


class UPIPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f"₹{amount} paid using UPI.")


class NetBankingPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f"₹{amount} paid using Net Banking.")


class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def pay(self, amount):
        self._strategy.process_payment(amount)


def main():
    amount = float(input("Enter payment amount: "))

    print("\nSelect Payment Method")
    print("1. Credit Card")
    print("2. Debit Card")
    print("3. UPI")
    print("4. Net Banking")

    choice = int(input("Enter your choice: "))

    strategies = {
        1: CreditCardPayment(),
        2: DebitCardPayment(),
        3: UPIPayment(),
        4: NetBankingPayment()
    }

    strategy = strategies.get(choice)

    if strategy:
        processor = PaymentProcessor(strategy)
        processor.pay(amount)
    else:
        print("Invalid Payment Method!")


if __name__ == "__main__":
    main()
