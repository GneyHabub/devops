"""Test suits"""

import time
import main


def test_msctime():
    """Assert that the app actually works and returns different time every request."""

    time1 = main.msctime()
    time.sleep(1)
    time2 = main.msctime()
    assert time1 != time2, "Should return different data"

def test():
    """Run all tests."""

    test_msctime()

test()
