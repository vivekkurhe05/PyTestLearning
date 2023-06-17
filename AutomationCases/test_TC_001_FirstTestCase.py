import pytest
# Test case code must be written inside a method
# Method name must be started with test

a=101

@pytest.mark.skip("Skipping this test because feature is no longer supported")
def test_tc_001_login_logout_testing():
    print("This is our test case code")

# Decorator
@pytest.mark.skip
def test_tc_003_login_logout_invalid_credentials():
    print("This is my testcase 3")

# conditionally skip execution of test case
@pytest.mark.skipif(a>100,reason="Skip if a's value is goes beyond 100")
def test_tc_004_verify_title():
    print("This is my testcase 4")

'''
-v -> Verbose mode means display test case names with status Passed or Failed
-s -> To display the print statement in output console
'''