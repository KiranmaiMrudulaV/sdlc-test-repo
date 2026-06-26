import inspect
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import auth


def test_login_uses_parameterized_queries():
    source = inspect.getsource(auth.login)
    assert 'f"' not in source and "f'" not in source, \
        "FAIL: login() uses f-string SQL queries — SQL injection vulnerability detected!"


def test_register_uses_parameterized_queries():
    source = inspect.getsource(auth.register)
    assert 'f"' not in source and "f'" not in source, \
        "FAIL: register() uses f-string SQL queries — SQL injection vulnerability detected!"


def test_get_user_data_uses_parameterized_queries():
    source = inspect.getsource(auth.get_user_data)
    assert 'f"' not in source and "f'" not in source, \
        "FAIL: get_user_data() uses f-string SQL queries — SQL injection vulnerability detected!"
