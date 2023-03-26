''' module docstring '''

import sys
from transaction import Transaction

def print_usage():
    ''' print an explanation of how to use this command '''
    print('''usage:
            q: quit
            show: show all transactions
            add (amount) (category) (date) (description): add new transaction
            delete (rowid): delete transaction
            by_date: summarize transactions by date
            by_month: summarize transactions by month
            by_year: summarize transactions by year
            by_cat: summarize transactions by category
            help: show this menu
            '''
            )

def print_transactions(transactions):
    ''' print the transactions '''
    if len(transactions) == 0:
        print('No transactions')
    else:
        print('\n')
        print("%-10s %-10s %-20s %-10s %-30s"
              %('item #', 'amount', 'category', 'date', 'description'))
        print('-'*80)
        for item in transactions:
            values = tuple(item.values())
            print("%-10s %-10.2f %-20s %-10s %-30s"%values)

def print_summary(groups, name):
    ''' print the output for a summarize function '''
    if len(groups) == 0:
        print('No transactions')
    else:
        print('\n')
        print("%-10s %-12s %-10s"
              %(name, 'transactions', 'total'))
        print('-'*80)
        for item in groups:
            values = tuple(item.values()) #(rowid,title,desc,completed)
            print("%-10s %-12d %-10.2f"%values)

def process_args(arglist):
    ''' examine args and make appropriate calls to Transaction'''
    transactions = Transaction('/tracker.db')
    if arglist == [] or arglist[0] == "help" or (arglist[0] == "add" and len(arglist) != 5):
        print_usage()
    elif arglist[0] == "show":
        print_transactions(transactions.show())
    elif arglist[0] == "add":
        transactions.add(arglist[1], arglist[2], arglist[3], arglist[4])
    elif arglist[0] == "delete":
        if len(arglist) != 2:
            print_usage()
        else:
            transactions.delete(arglist[1])
    elif arglist[0] == "by_date":
        print_summary(transactions.summarize_by_date(), "date")
    elif arglist[0] == "by_month":
        print_summary(transactions.summarize_by_month(), "month")
    elif arglist[0] == "by_year":
        print_summary(transactions.summarize_by_year(), "year")
    elif arglist[0] == "by_cat":
        print_summary(transactions.summarize_by_category(), "category")
    else:
        print(arglist, "is not implemented")
        print_usage()

def toplevel():
    ''' read the command args and process them'''
    if len(sys.argv) == 1:
        # No arguments were passed
        print_usage()
        args = []
        while args != ['q']:
            args = input("command> ").split(' ')
            if args[0] == "add":
                # join the description as a string
                args = [args[0], args[1], args[2], args[3], "".join(args[4:])]
            process_args(args)
            print('-'*80+'\n'*3)
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*80+'\n'*3)

toplevel()
