from math_func import StudentDb
import pytest

# db = None


@pytest.fixture(scope='module')
def db():
    print('setup Pass')
    db = StudentDb()
    db.connect('data.json')
    yield db
    db.close()
    print('closs Pass')
    # return 'test'


# def teardown_module(module):
#     db.close()


def test_stud_one(db):
    stud_one = db.getData('StudentOne')
    assert stud_one['id'] == 1
    assert stud_one['name'] == 'StudentOne'
    assert stud_one['result'] == 'pass'

def test_stud_two(db):
    db = StudentDb()
    db.connect('data.json')
    stud_two = db.getData('StudentTwo')
    assert stud_two['id'] == 2
    assert stud_two['name'] == 'StudentTwo'
    assert stud_two['result'] == 'Fail'
