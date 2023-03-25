import sqlite3
import os

def to_dict(t):
    ''' t is a tuple (item #, title, desc,completed)'''
    print('t='+str(t))
    todo = {'rowid':t[0], 'title':t[1], 'desc':t[2], 'completed':t[3]}
    return todo

class Transaction():
    '''<docstring>'''

    def __init__(self, data):
        self.data = data;
        self.run_query('''CREATE TABLE IF NOT EXISTS transactions
                     (amount real, category text, date text, description text)''',())

    def show_categories(self):
        '''returns the list of unique categories in the database'''
        categories = self.run_query('''SELECT DISTINCT category FROM transactions;''')
        return [cat[0] for cat in categories]

    def run_query(self, query, tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con = sqlite3.connect(os.getenv('HOME') + self.data)
        cur = con.cursor() 
        cur.execute(query,tuple)
        result = cur.fetchall()
        con.commit()
        con.close()
        return result
