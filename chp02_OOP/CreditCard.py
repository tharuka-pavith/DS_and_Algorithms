class CreditCard:
    '''A consumer Credit Card'''
    
    def __init__(self, customer: str, bank: str, acnt: str, limit: int = 10_000):
        '''Create a new credit card instance
            
            Initial balance is zero. '''
        if (type(acnt) != str):
            raise TypeError('Invalid data type')
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0
        
    def get_customer(self):
        '''Returns customer'''
        return self._customer
    
    def get_bank(self):
        '''Returns bank'''
        return self._bank
    
    def get_acnt(self):
        '''Returns account number'''
        return self._acnt
    
    def get_limit(self):
        '''Returns credit limit'''
        return self._limit
    
    def get_balance(self):
        '''Returns account balance'''
        return self._balance
    
    def __str__(self) -> str:
        '''Returns string representation of Credit Card'''
        
        str = f'''
                Customer name : {self._customer}
                Bank name     : {self._bank}
                Account Number: {self._acnt}
                Account limit : {self._limit}
                '''
        
        return str
    

if __name__ == '__main__':
    
    cc = CreditCard('Tharuka', 'NSB', '2342093443568754' , 10_000);
    
    print(cc)