import pytest

from config_reader import Readconfig
from utilities.driver_factory import create_driver_factory


@pytest.fixture()
def create_driver():
    driver = create_driver_factory(Readconfig.get_browser_id())
    driver.maximize_window()
    driver.get(Readconfig.get_base_url())
    yield driver
    driver.quit()


@pytest.fixture()
def navigate_to_buy_section():
    driver = create_driver_factory(Readconfig.get_browser_id())
    driver.maximize_window()
    driver.get(Readconfig.get_buy_page())
    yield driver
    driver.quit()


@pytest.fixture()
def navigate_to_cart():
    driver = create_driver_factory(Readconfig.get_browser_id())
    driver.maximize_window()
    driver.get(Readconfig.get_cart_page())
    yield driver
    driver.quit()


@pytest.fixture()
def macbook_page():
    driver = create_driver_factory(Readconfig.get_browser_id())
    driver.maximize_window()
    driver.get(Readconfig.get_macbook_url())
    yield driver
    driver.quit()


@pytest.fixture()
def apple_watch_page():
    driver = create_driver_factory(Readconfig.get_browser_id())
    driver.maximize_window()
    driver.get(Readconfig.get_apple_watch_url())
    yield driver
    driver.quit()


@pytest.fixture()
def air_tag_page():
    driver = create_driver_factory(Readconfig.get_browser_id())
    driver.maximize_window()
    driver.get(Readconfig.get_air_tag_url())
    yield driver
    driver.quit()


@pytest.fixture()
def air_pods_navigate():
    driver = create_driver_factory(Readconfig.get_browser_id())
    driver.maximize_window()
    driver.get(Readconfig.get_air_pods_url())
    yield driver
    driver.quit()


@pytest.fixture()
def apple_tv_navigate():
    driver = create_driver_factory(Readconfig.get_browser_id())
    driver.maximize_window()
    driver.get(Readconfig.get_apple_tv_url())
    yield driver
    driver.quit()


@pytest.fixture()
def air_pods_case():
    driver = create_driver_factory(Readconfig.get_browser_id())
    driver.maximize_window()
    driver.get(Readconfig.get_air_pods_case_url())
    yield driver
    driver.quit()


@pytest.fixture()
def air_pods2():
    driver = create_driver_factory(Readconfig.get_browser_id())
    driver.maximize_window()
    driver.get(Readconfig.get_air_pods2_url())
    yield driver
    driver.quit()


@pytest.fixture()
def apple_books_navigate():
    driver = create_driver_factory(Readconfig.get_browser_id())
    driver.maximize_window()
    driver.get(Readconfig.get_books_url())
    yield driver
    driver.quit()


@pytest.fixture()
def retail_page_navigate():
    driver = create_driver_factory(Readconfig.get_browser_id())
    driver.maximize_window()
    driver.get(Readconfig.get_retail_page())
    yield driver
    driver.quit()


@pytest.fixture()
def apple_store_navigate():
    driver = create_driver_factory(Readconfig.get_browser_id())
    driver.maximize_window()
    driver.get(Readconfig.get_apple_store())
    yield driver
    driver.quit()


@pytest.fixture()
def apple_home_pod_navigate():
    driver = create_driver_factory(Readconfig.get_browser_id())
    driver.maximize_window()
    driver.get(Readconfig.get_home_pod())
    yield driver
    driver.quit()
