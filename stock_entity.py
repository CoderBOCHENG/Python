class stock:

    def __init__(self, index, ticker, name):
        self.name = name
        self.ticker = ticker
        self.index = index

    def get_ticker_value(self):
        return self.ticker.split(".")[0]

    def get_market(self):
        str = self.ticker.split(".")[1]
        if str == 'sh':
            return "SHANGHAI"
        else:
            return "SHENZHEN"

    def __str__(self):
        return f'Stock(id={self.index}, ticker={self.ticker}, name={self.name})'

    def __repr__(self):
        return f'Stock(id={self.index}, ticker={self.ticker}, name={self.name})'




# TEST CODE -------------------------------------

if __name__ == "__main__":

    t1 = (0, '600519.sh', '贵州茅台')
    s1 = stock(*t1)
    print(s1.index)
    print(s1.ticker)
    print(s1.name)
    print(s1.get_ticker_value())
    print(s1.get_market())

    print(s1)

    l = []
    l.append(s1)
    print(l)


'''
IMPORTANCE!! ------------------------------------
1) magic method __str__(self):
   This method returns a str value
   The method will be invoked when you print out the class object
   Without the method, printing out the object directly shows rubbish str in the console
   
2) magic method __repr__(self):
   This method returns a str value
   The method will be invoked when you print out a list of class object
   Without the method, printing out the object directly shows rubbish str in the console
'''
