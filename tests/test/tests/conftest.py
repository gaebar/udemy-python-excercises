from pytest import fixture
from selenium import webdriver

@fixture(params=[webdriver.Chrome])
def browser(request):
    driver= webdriver.Chrome('/Applications/chromedriver')
    driver = request.param
    drvr = driver()
    yield drvr
    drvr.quit()

