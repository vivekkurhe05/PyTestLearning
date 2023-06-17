import pytest
# Test case code must be written inside a method
# Method name must be started with test

# syntax - @pytest.mark.UserdefinedName
@pytest.mark.Smoke
@pytest.mark.Regression
def test_tc_006_remember_me_testing():
    print("This is our test case code")

# syntax - @pytest.mark.UserdefinedName
@pytest.mark.Sanity
@pytest.mark.Regression
def test_tc_007_payment_testing():
    print("This is our test case code")