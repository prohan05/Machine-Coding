class BillController(object):
    def __init__(self, billService):
        self.billService = billService

    def add_bill(self, id, groupId, amount, contribution, paidBy):
        return self.billService.add_bill(id, groupId, amount, contribution, paidBy)

    def getUserBalance(self, userId):
        balance = 0
        for billId in self.billService.billDetails:
            bill = self.billService.billDetails.get(billId)
            if userId in bill.getContribution():
                balance = balance - bill.getContribution().get(userId)
            if userId in bill.getPaidBy():
                balance = balance + bill.getPaidBy().get(userId)
        return balance
