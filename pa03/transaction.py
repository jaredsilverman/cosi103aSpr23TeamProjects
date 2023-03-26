import sqlite3
import os

def to_dict(t):
    ''' t is a tuple (item #, amount, category, date, description)'''
    print('t='+str(t))
    todo = {'item':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    return todo

class Transaction():
    '''<docstring>'''

    def __init__(self, data):
        self.data = data
        self.run_query('''CREATE TABLE IF NOT EXISTS transactions
                     (amount real, category text, date text, description text)''',())
    
    def show(self):
        '''shows all transactions'''
        return self.run_query("SELECT * FROM transactions")
    
    def add(self, amount, category, date, description):
        '''adds transaction into the database'''
        self.run_query("INSERT INTO transactions (amount, category, date, description) VALUES (?, ?, ?, ?)",(amount, category, date, description))

    def delete(self, item):
        '''deletes a transaction from the database'''
        self.run_query("DELETE FROM transactions WHERE item=?", (item,))

    def summarize_by_date(self):
        '''summarize the transactions based on the dates'''
        return self.run_query("SELECT date, SUM(amount), COUNT(amount) FROM transactions GROUP BY date")
    
    def summarize_by_month(self):
        '''summarize the transactions based on the months'''
        return self.run_query("SELECT DATENAME(month,date), SUM(amount), COUNT(amount) FROM transactions GROUP BY DATENAME(month,Date)")
    
    def summarize_by_year(self):
        '''summarize the transactions based on the year'''
        return self.run_query("SELECT DATENAME(year ,date), SUM(amount), COUNT(amount) FROM transactions GROUP BY DATENAME(year,Date)")
    
    def summarize_by_category(self):
        '''summarize the transactions based on the category'''
        return self.run_query("SELECT category, SUM(amount), COUNT(amount) FROM transactions GROUP BY category")
    

    def run_query(self, query, tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con = sqlite3.connect(os.getenv('HOME') + self.data)
        cur = con.cursor() 
        cur.execute(query,tuple)
        result = cur.fetchall()
        con.commit()
        con.close()
        return [to_dict(t) for t in result]