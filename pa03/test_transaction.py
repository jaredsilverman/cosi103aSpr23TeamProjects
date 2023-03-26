from transaction import Transaction
import pytest

@pytest.fixture
def database():
    database = Transaction("/tracker.db")
    yield database

def test_add_transaction(database):
    database.add(10.0, 'Food', '2023-03-26', 'sandwich')
    assert database.show() == [{'item':1, 'amount':10.0, 'category':"Food",'date':'2023-03-26', 'description':'sandwich'}]

def test_delete_transaction(database):
    database.add(10.0, 'Food', '2023-03-26', 'sandwich')
    database.delete(1)
    assert database.show() == []

def test_summarize_by_date(database):
    database.add(10.0, 'Food', '2023-03-26', 'sandwich')
    database.add(40.0, 'Utilities', '2023-03-26', 'plumbing')
    assert database.summarize_by_date() == [{"date":"2023-03-26", 'transactions':1, 'total':"50"}]

def test_summarize_by_month(database):
    database.add(10.0, 'Food', '2023-03-26', 'sandwich')
    database.add(40.0, 'Utilities', '2023-03-26', 'plumbing')
    assert database.summarize_by_month() ==  [{"date":"03", 'transactions':2, 'total':"50"}]

def test_summarize_by_year(database):
    database.add(10.0, 'Food', '2023-03-26', 'sandwich')
    database.add(40.0, 'Utilities', '2023-03-26', 'plumbing')
    assert database.summarize_by_year() ==  [{"date":"2023", 'transactions':2, 'total':"50"}]

def test_summarize_by_category(database):
    database.add(10.0, 'Food', '2023-03-26', 'sandwich')
    database.add(40.0, 'Utilities', '2023-03-26', 'plumbing')
    assert database.summarize_by_category() == [{"category":"Food", 'transactions':1, 'total':"10"}, 
                                                {"category":"Utilities", 'transactions':1, 'total':"40"}]

