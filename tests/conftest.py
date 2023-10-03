# file to collect all fixtures

import pytest
import psycopg2

# fixture used to create connection to database (and close it after test execution)
@pytest.fixture(scope='function')
def db_connection():
    connection = psycopg2.connect(
        database="***change_me***",
        user="***change_me***",
        password="***change_me***",
        host="127.0.0.1",  # localhost
        port="***change_me***"
    )
    yield connection

    # after test execution DB connection will be automatically closed
    connection.close()



