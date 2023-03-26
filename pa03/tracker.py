''' module docstring '''

import sys
from transaction import Transaction

def print_usage():
    ''' print an explanation of how to use this command '''
    print('''usage:
            0. quit
            1. show categories
            2. add category
            3. modify category
            4. show transactions
            5. add transaction
            6. delete transaction
            7. summarize transactions by date
            8. summarize transactions by month
            9. summarize transactions by year
            10. summarize transactions by category
            11. print this menu
            '''
            )

def print_transactions(transactions):
    ''' print the transactions '''
    if len(transactions) == 0:
        print('No transactions')
    else:
        print('\n')
        print("%-10s %-10s %-30s %-10s %-30s"
              %('item #', 'amount', 'category', 'date', 'description'))
        print('-'*40)
        for item in transactions:
            values = tuple(item.values()) #(rowid,title,desc,completed)
            print("%-10s %-10s %-30s %2d"%values)

def process_args(arglist):
    ''' examine args and make appropriate calls to Transaction'''
    transactions = Transaction('tracker.db')
    if arglist == [] or arglist[0] == "11" or (arglist[0] == "5" and len(arglist) != 5):
        print_usage()
    elif arglist[0] == "4":
        print_transactions(transactions.show())
    elif arglist[0] == "5":
        transactions.add(arglist[1], arglist[2], arglist[3], arglist[4])
    elif arglist[0] == "6":
        if len(arglist) != 2:
            print_usage()
        else:
            transactions.delete(arglist[1])
    elif arglist[0] == "7":
        print_transactions(transactions.summarize_by_date())
    elif arglist[0] == "8":
        print_transactions(transactions.summarize_by_month())
    elif arglist[0] == "9":
        print_transactions(transactions.summarize_by_year())
    elif arglist[0] == "10":
        print_transactions(transactions.summarize_by_category())
    else:
        print(arglist,"is not implemented")
        print_usage()

def toplevel():
    ''' read the command args and process them'''
    if len(sys.argv) == 1:
        # No arguments were passed
        print_usage()
        args = []
        while args != ['']:
            args = input("command> ").split(' ')
            if args[0] == "5":
                # join everyting after the name as a string
                args = ['add',args[1]," ".join(args[2:])]
            if args[0] != 0:
                process_args(args)
            print('-'*40+'\n'*3)
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*40+'\n'*3)

toplevel()
