import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: '--browser_name=chrome' or '--browser_name=firefox'")
    parser.addoption('--language', action='store', default='en',
                     help="Choose langiage: '--language=en' or '--language=ru'")


@pytest.fixture(scope="function")
def browser(request):
    # Language selection part
    user_language = request.config.getoption('language')
    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    firefox_options = FirefoxOptions()
    firefox_options.set_preference('intl.accept_languages', user_language)

    # Browser selection part
    browser_name = request.config.getoption('browser_name')
    browser = None
    if browser_name == 'chrome':
        print(f'...starting Chrome...')
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == 'firefox':
        print(f'...starting Firefox...')
        browser = webdriver.Firefox(options=firefox_options)
    else:
        raise pytest.UsageError('--browser_name should be Chrome or Firefox')

    yield browser
    print(f'...quitting browser...')
    browser.quit()
