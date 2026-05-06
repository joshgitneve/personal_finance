"""
Module for handling financial transactions.
"""
class Transaction:
    """
    Represents a financial transaction with amount, category, nature, description, and date.
    
    Attributes:
        amount (float): The transaction amount.
        category (str): The category of the transaction.
        nature (str): The nature, e.g., 'expense' or 'income'.
        description (str): A description of the transaction.
        date (str): The date of the transaction.
    """
    def __init__(self, amount, category, nature, description, date):
        self.amount = amount
        self.category = category
        self.nature = nature
        self.description = description
        self.date = date

    def is_expense(self):
        """
        Checks if the transaction is an expense.
        
        Returns:
        bool: True if nature is 'expense', False otherwise.
        """
        return self.nature == "expense"

    def is_income(self):
        """
        Checks if the transaction is income.
        
        Returns:
        bool: True if nature is 'income', False otherwise.
        """
        return self.nature == "income"
    
    def __str__(self):
        return f"{self.date} | {self.category} | {self.nature} | ${self.amount:.2f} | {self.description}"