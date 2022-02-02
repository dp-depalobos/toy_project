import pytest

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Models.item import ItemModel

NAME = 'Sandals'
ID = 1

@pytest.fixture
def flask_app_mock():
    """Flask application set up."""
    app_mock = Flask(__name__)
    app_mock.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app_mock.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    db = SQLAlchemy(app_mock)
    db.init_app(app_mock)
    return app_mock

@pytest.fixture
def mock_item():
    item = ItemModel(name='Sandals', price=100)
    return item

@pytest.fixture
def mock_get_sqlalchemy(mocker):
    mock = mocker.patch('flask_sqlalchemy._QueryProperty.__get__').return_value = mocker.Mock()
    return mock

def test_get_record_from_name_item_invalid_input(flask_app_mock, mock_get_sqlalchemy, mock_item):
    with flask_app_mock.app_context():
        mock_get_sqlalchemy.filter_by.return_value.first.return_value = mock_item
        response = ItemModel.find_by_name(ID)
        assert response is None

def test_get_record_from_name_item_not_found(flask_app_mock, mock_get_sqlalchemy, mock_item):
    with flask_app_mock.app_context():
        mock_get_sqlalchemy.filter_by.return_value.first.return_value = None
        response = ItemModel.find_by_name(mock_item.name)
        assert response is None

def test_get_record_from_name_item_found(flask_app_mock, mock_get_sqlalchemy, mock_item):
    with flask_app_mock.app_context():
        mock_get_sqlalchemy.filter_by.return_value.first.return_value = mock_item
        response = ItemModel.find_by_name(mock_item.name)
        assert (response.name == 'Sandals') & (response.price == 100)

def test_get_record_from_id_item_invalid_input(flask_app_mock, mock_get_sqlalchemy, mock_item):
    with flask_app_mock.app_context():
        mock_get_sqlalchemy.filter_by.return_value.first.return_value = mock_item
        response = ItemModel.find_by_id(NAME)
        assert response is None

def test_get_record_from_id_item_not_found(flask_app_mock, mock_get_sqlalchemy, mock_item):
    with flask_app_mock.app_context():
        mock_get_sqlalchemy.filter_by.return_value.first.return_value = None
        response = ItemModel.find_by_id(mock_item.name)
        assert response is None

def test_get_record_from_id_item_found(flask_app_mock, mock_get_sqlalchemy, mock_item):
    with flask_app_mock.app_context():
        mock_get_sqlalchemy.filter_by.return_value.first.return_value = mock_item
        response = ItemModel.find_by_id(ID)
        assert (response.name == 'Sandals') & (response.price == 100)

def test_json(mock_item):
    assert {'name':'Sandals', 'price':100} == mock_item.json()

def test_get_price(mock_item):
    assert 100 == mock_item.get_price()