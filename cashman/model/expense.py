from marshmallow import post_load

from cashman.model.transaction import Transaction, TransactionSchema

from cashman.model.transaction_type import TransactionType

class Expense(Transaction):

	def __init__(self, description, amount):
		#Force the expense to be a negative value to make computations easier
		super(Expense, self).__init__(description, -abs(amount), TransactionType.EXPENSE)

	def __repr__(self):

		return '<Expense(name={self.description!r})>'.format(self=self)

class ExpenseSchema(TransactionSchema):

	@post_load

	def make_expense(self, data, **kwargs):

		return Expense(**data)


