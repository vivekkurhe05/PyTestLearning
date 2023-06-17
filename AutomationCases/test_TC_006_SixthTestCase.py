import pytest
# Test case code must be written inside a method
# Method name must be started with test
# In this file, fixture will execute only once before and after all test methods

actual_result="Hello"

@pytest.fixture(scope="module")
def setup():
    print("This will execute before all test methods")
    yield
    print("Close DB connection after executing all test methods")

# syntax - @pytest.mark.UserdefinedName
@pytest.mark.TopPriority
def test_tc_012_business_template_testing(setup):
    print("This is our test case code")
    assert "Testing" == "Hello"

# syntax - @pytest.mark.UserdefinedName
@pytest.mark.TopPriority
def test_tc_013_mbp_testing(setup):
    print("This is our test case code")
    assert actual_result != "Testing", "This two values must not be the same"