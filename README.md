A very basic explanation of python test.

Files taken into consideration:

    math_func.py
        Main python execution
    
    test_math_func.py
        Test file
    
    data.json
        data storage in form of json


Explanation:

math_func.py file basically reads data from data.json and parses accordingly.

test_math_func.py contains test cases to check of data corresponding to each entry is correct. It has a decorator i.e., the pytest.fixture to initialize and teardown db connection.

data.json has two entries.