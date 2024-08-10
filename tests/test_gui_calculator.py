import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page_get(client):
    """Test GET request to home page"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Calculator" in response.data

def test_calculator_addition(client):
    """Test addition operation"""
    response = client.post('/', data={'expression': '2+3'})
    assert response.status_code == 200
    assert b'5' in response.data

def test_calculator_subtraction(client):
    """Test subtraction operation"""
    response = client.post('/', data={'expression': '5-2'})
    assert response.status_code == 200
    assert b'3' in response.data

def test_calculator_multiplication(client):
    """Test multiplication operation"""
    response = client.post('/', data={'expression': '3*4'})
    assert response.status_code == 200
    assert b'12' in response.data

def test_calculator_division(client):
    """Test division operation"""
    response = client.post('/', data={'expression': '8/2'})
    assert response.status_code == 200
    assert b'4.0' in response.data

def test_calculator_parentheses(client):
    """Test expression with parentheses"""
    response = client.post('/', data={'expression': '(2+3)*4'})
    assert response.status_code == 200
    assert b'20' in response.data

def test_calculator_invalid_expression(client):
    """Test handling of an invalid expression"""
    response = client.post('/', data={'expression': '2++/3'})
    assert response.status_code == 200
    assert b'Error' in response.data

def test_calculator_clear(client):
    """Test clearing the expression"""
    response = client.post('/', data={'expression': ''})
    assert response.status_code == 200
    assert b'' in response.data

def test_calculator_zero_division(client):
    """Test division by zero handling"""
    response = client.post('/', data={'expression': '5/0'})
    assert response.status_code == 200
    assert b'Error' in response.data
