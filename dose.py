class Dose():
    """
    dose represent drug name, amount of drug and unit
    attributes:
    drug for the drug name
    amount
    mass_unit
    time_unit
    """
    
    def __init__(self, text):
        self.drug = text[0:text.find(' ')]
        self.amount = float(text[text.find(' ')+1:text.find(' ',text.find(' ') + 1)])
        self.mass_unit = text[text.find(' ', text.find(' ') + 1)+1:text.find('/')]
        self.time_unit = text[text.find('/') + 1:]
        
    def is_overdose(self, reference):
        """
        If the drug and units are the same, and the amount is less than or equal to the reference amount, return False.
        If the drug and units are not the same, then return None.
        Otherwise return True.
        Note, 'None' is a special kind of value that any variable can have.
        It means that the value of this variable is undefined.
        """
        if self.drug == reference.drug and self.mass_unit == reference.mass_unit and self.time_unit == reference.time_unit:
            if reference.amount >= self.amount:
                return False
            else:
                return True
        else:
            return None
