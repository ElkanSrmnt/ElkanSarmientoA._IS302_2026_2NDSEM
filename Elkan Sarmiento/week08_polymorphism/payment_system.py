class Payment_eas:
    def pay_eas(self_eas):
        print("Processing payment")


class CashPayment_eas(Payment_eas):
    def pay_eas(self_eas):
        print("Payment made using cash")


class CardPayment_eas(Payment_eas):
    def pay_eas(self_eas):
        print("Payment made using credit card")


payments_eas = [CashPayment_eas(), CardPayment_eas()]
for p_eas in payments_eas:
    p_eas.pay_eas()