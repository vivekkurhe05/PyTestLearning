import pytest
# Test case code must be written inside a method
# Method name must be started with test
# In this file, fixture will execute before and after ever test method

actual_result="Hello"

@pytest.fixture()
def setup():
    print("This will execute before test execution")
    yield
    print("Close DB connection after executing test cases")

# syntax - @pytest.mark.UserdefinedName
@pytest.mark.TopPriority
def test_tc_010_business_template_testing(setup):
    print("This is our test case code")
    assert "Testing" == "Hello"

# syntax - @pytest.mark.UserdefinedName
@pytest.mark.TopPriority
def test_tc_011_mbp_testing(setup):
    print("This is our test case code")
    assert actual_result != "Testing", "This two values must not be the same"