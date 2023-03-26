This app allows the user to keep track of their finances through a database in SQL

Scripts

Pylint:

PS C:\Users\gmbab\cosi103aSpr23TeamProjects\pa03> pylint tracker.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

PS C:\Users\gmbab\cosi103aSpr23TeamProjects\pa03> pylint transaction.py     

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

Pytest:

PS C:\Users\gmbab\cosi103aSpr23TeamProjects\pa03> pytest test_transaction.py
======================================================================= test session starts ========================================================================
platform win32 -- Python 3.9.12, pytest-7.1.1, pluggy-1.0.0
rootdir: C:\Users\gmbab\cosi103aSpr23TeamProjects\pa03
plugins: anyio-3.5.0
collected 7 items

test_transaction.py .......                                                                                                                                   [100%]

======================================================================== 7 passed in 0.42s ========================================================================= 


Tracker.py:

PS C:\Users\gmbab\cosi103aSpr23TeamProjects\pa03> python tracker.py 
usage:
            q: quit
            show: show all transactions
            add (amount) (category) (date) (description): add new transaction
            delete (rowid): delete transaction
            by_date: summarize transactions by date
            by_month: summarize transactions by month
            by_year: summarize transactions by year
            by_cat: summarize transactions by category
            help: show this menu

command> add 10 food 2023-02-01 hamburger
--------------------------------------------------------------------------------



command> show


item #     amount     category             date       description
--------------------------------------------------------------------------------
1          10.00      food                 2023-02-01 hamburger
--------------------------------------------------------------------------------



command> add 20 transportation 2023-02-04 car
--------------------------------------------------------------------------------



command> by_month    


month      transactions total
--------------------------------------------------------------------------------
02         2            30.00
--------------------------------------------------------------------------------



command> by_cat     


category   transactions total
--------------------------------------------------------------------------------
food       1            10.00
transportation 1            20.00
--------------------------------------------------------------------------------



command> q
