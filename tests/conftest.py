import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield
    browser.config.hold_browser_open = True
