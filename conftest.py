import pytest
import time
from utils.driver_factory import get_driver

@pytest.fixture
def driver(request):
    driver = get_driver()
    yield driver

    # Take screenshot only if test failed
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        driver.save_screenshot(f"reports/failure_{int(time.time())}.png")

    driver.quit()


# This hook is REQUIRED for failure detection
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)