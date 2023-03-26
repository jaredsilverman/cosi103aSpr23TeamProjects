from transaction import Transaction
import pytest

@pytest.fixture
def database():
    database = Transaction("/tracker.db")
    yield database

def test_show(database):
    assert database.show() == []

def test_add(database):
    database.add(11.0, 'Food', '2023-03-26', 'sandwich')
    assert database.show() == [{'item':1, 'amount':11.0, 'category':"Food", 'date':'2023-03-26', 'description':'sandwich'}]
    database.delete(1)

def test_delete(database):
    database.add(12.0, 'Food', '2023-03-26', 'sandwich')
    database.delete(1)
    assert database.show() == []

def test_summarize_by_date(database):
    database.add(13.0, 'Food', '2023-03-26', 'sandwich')
    database.add(44.0, 'Utilities', '2023-03-26', 'plumbing')
    assert database.summarize_by_date() == [{"date":"2023-03-26", 'transactions':2, 'total':57.0}]
    database.delete(1)
    database.delete(2)

def test_summarize_by_month(database):
    database.add(14.0, 'Food', '2023-03-26', 'sandwich')
    database.add(45.0, 'Utilities', '2023-03-26', 'plumbing')
    assert database.summarize_by_month() ==  [{"month":"03", 'transactions':2, 'total':59.0}]
    database.delete(1)
    database.delete(2)


def test_summarize_by_year(database):
    database.add(15.0, 'Food', '2023-03-26', 'sandwich')
    database.add(46.0, 'Utilities', '2023-03-26', 'plumbing')
    assert database.summarize_by_year() ==  [{"year":"2023", 'transactions':2, 'total':61.0}]
    database.delete(1)
    database.delete(2)

def test_summarize_by_category(database):
    database.add(16.0, 'Food', '2023-03-26', 'sandwich')
    database.add(47.0, 'Utilities', '2023-03-26', 'plumbing')
    assert database.summarize_by_category() == [{"category":"Food", 'transactions':1, 'total':16.0}, 
                                                {"category":"Utilities", 'transactions':1, 'total':47.0}]
    database.delete(1)
    database.delete(2)
