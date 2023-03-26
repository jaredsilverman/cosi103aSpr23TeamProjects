''' docstring '''

import sqlite3
import os

def to_dict(tup):
    ''' tup is a tuple (item #, amount, category, date, description)'''
    print(tup)
    transaction = {'item':tup[0], 'amount':tup[1], 'category':tup[2],
                   'date':tup[3], 'description':tup[4]}
    return transaction

def summarize_dict(tup, group):
    ''' tup is a tuple (group, transactions, total)'''
    grouped = {group:tup[0], 'transactions':tup[1], 'total':tup[2]}
    return grouped

class Transaction():
    def __init__(self, data):
        self.data = data
        self.run_query("""CREATE TABLE IF NOT EXISTS transactions
                     (amount real, category text, date date, description text);""",())

    def show(self):
        '''shows all transactions'''
        result = self.run_query("SELECT rowid, * FROM transactions;", ())
        return [to_dict(t) for t in result]

    def add(self, amount, category, date, description):
        '''adds transaction into the database'''
        self.run_query("""INSERT INTO transactions (amount, category, date, description)
                       VALUES (?, ?, ?, ?);""",
                       (amount, category, date, description))

    def delete(self, item):
        '''deletes a transaction from the database'''
        result = self.run_query("DELETE FROM transactions WHERE rowid=?;", (item,))
        return [to_dict(t) for t in result]

    def summarize_by_date(self):
        '''summarize the transactions based on the dates'''
        result = self.run_query("""SELECT date, COUNT(amount) AS transactions,
                              SUM(amount) AS total FROM transactions GROUP BY date;""", ())
        return [summarize_dict(t, "date") for t in result]

    def summarize_by_month(self):
        '''summarize the transactions based on the months'''
        result = self.run_query("""SELECT DATENAME(month, date) AS month,
                              COUNT(amount) AS transactions, SUM(amount) AS total
                              FROM transactions GROUP BY month;""", ())
        return [summarize_dict(t, "month") for t in result]

    def summarize_by_year(self):
        '''summarize the transactions based on the year'''
        result = self.run_query("""SELECT DATENAME(year, date) AS year,
                              COUNT(amount) AS transactions, SUM(amount) AS total
                              FROM transactions GROUP BY year;""", ())
        return [summarize_dict(t, "year") for t in result]

    def summarize_by_category(self):
        '''summarize the transactions based on the category'''
        result = self.run_query("""SELECT category, COUNT(amount) AS transactions,
                              SUM(amount) AS total FROM transactions GROUP BY category;""", ())
        return [summarize_dict(t, "category") for t in result]

    def run_query(self, query, tup):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con = sqlite3.connect(os.getenv('HOME') + self.data)
        cur = con.cursor()
        cur.execute(query,tup)
        result = cur.fetchall()
        con.commit()
        con.close()
        return result
