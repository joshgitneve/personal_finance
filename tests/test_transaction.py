from src.transaction import Transaction



def test_transaction_is_created():
    """
    module testing that the Transaction class is working
    """
    trans1 = Transaction(37.99, "shopping", "expense", "groceries", "27 Jan 2026")
    assert trans1.amount == 37.99
    assert trans1.category == "shopping"
    assert trans1.description == "groceries"
                     
def test_is_transaction_expense():
    
    trans2 = Transaction(50, "family", "transfer", "birthday money", "28 Jan 2026")
    trans3 = Transaction(4.89, "shopping", "expense", "groceries", "28 Jan 2026")
    assert trans2.is_expense() == False
    assert trans3.is_expense() == True

def test_is_transaction_income():

    trans4 = Transaction(3980, "salary", "income", "february income", "5 March 2026")
    trans5 = Transaction(2500, "shared", "transfer", "transfer to common account", "10 March 2026")
    assert trans4.is_income() == True
    assert trans5.is_income() == False

def test_transfer_is_neither_income_nor_expense():
    trans_transfer = Transaction(2500, "shared", "transfer", "transfer to common account", "10 March 2026")
    assert trans_transfer.is_income() == False
    assert trans_transfer.is_expense() == False

def test_transaction_summary__str__():
    trans6 = Transaction(3990, "salary", "income", "March income", "5 April 2026")
    assert str(trans6) == "5 April 2026 | salary | income | $3990.00 | March income"