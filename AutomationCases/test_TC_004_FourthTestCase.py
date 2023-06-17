import pytest
# Test case code must be written inside a method
# Method name must be started with test

actual_result="Testing"

# syntax - @pytest.mark.UserdefinedName
@pytest.mark.TopPriority
def test_tc_008_business_template_testing():
    print("This is our test case code")
    assert actual_result == "Hello"

# syntax - @pytest.mark.UserdefinedName
@pytest.mark.TopPriority
def test_tc_009_mbp_testing():
    print("This is our test case code")
    assert actual_result != "Testing", "This two values must not be the same"