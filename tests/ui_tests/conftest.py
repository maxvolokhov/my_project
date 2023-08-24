import json
import pytest
from config_obj import ConfigObject
from page_objects.air_pods2 import AirPods2Page
from page_objects.air_pods_case_page import AirPodsCasePage
from page_objects.air_tag_page import AirTagPage
from page_objects.airpods_page import AirPodsPage
from page_objects.apple_books_page import AppleBooksPage
from page_objects.apple_store_page import AppleStorePage
from page_objects.apple_tv_page import AppleTvPage
from page_objects.apple_watch_page import AppleWatchPage
from page_objects.buy_iphone_page import BuyIphonePage
from page_objects.home_pod_page import HomePodPage
from page_objects.macbook_page import MacbookPage
from page_objects.main_page import MainPage
from page_objects.retail_page import RetailPage
from utilities.driver_factory import create_driver_factory


@pytest.fixture()
def create_driver_main_page(env):
    driver = create_driver_factory(env.browser_id)
    driver.maximize_window()
    driver.get(env.base_url)
    main_page_instance = MainPage(driver)
    yield main_page_instance
    driver.quit()


@pytest.fixture()
def navigate_to_buy_section(env):
    driver = create_driver_factory(env.browser_id)
    driver.maximize_window()
    driver.get(env.buy_page_url)
    buy_iphone_page_instance = BuyIphonePage(driver)
    yield buy_iphone_page_instance
    driver.quit()


@pytest.fixture()
def navigate_to_cart(env):
    driver = create_driver_factory(env.browser_id)
    driver.maximize_window()
    driver.get(env.item_in_cart_url)
    yield driver
    driver.quit()


@pytest.fixture()
def macbook_page(env):
    driver = create_driver_factory(env.browser_id)
    driver.maximize_window()
    driver.get(env.macbook_url)
    macbook_page_instance = MacbookPage(driver)
    yield macbook_page_instance
    driver.quit()


@pytest.fixture()
def apple_watch_page(env):
    driver = create_driver_factory(env.browser_id)
    driver.maximize_window()
    driver.get(env.apple_watch_url)
    apple_watch_instance = AppleWatchPage(driver)
    yield apple_watch_instance
    driver.quit()


@pytest.fixture()
def air_tag_page(env):
    driver = create_driver_factory(env.browser_id)
    driver.maximize_window()
    driver.get(env.air_tag_url)
    air_tag_page_instance = AirTagPage(driver)
    yield air_tag_page_instance
    driver.quit()


@pytest.fixture()
def air_pods_navigate(env):
    driver = create_driver_factory(env.browser_id)
    driver.maximize_window()
    driver.get(env.air_pods_url)
    air_pods_instance = AirPodsPage(driver)
    yield air_pods_instance
    driver.quit()


@pytest.fixture()
def apple_tv_navigate(env):
    driver = create_driver_factory(env.browser_id)
    driver.maximize_window()
    driver.get(env.apple_tv_url)
    apple_tv_instance = AppleTvPage(driver)
    yield apple_tv_instance
    driver.quit()


@pytest.fixture()
def air_pods_case(env):
    driver = create_driver_factory(env.browser_id)
    driver.maximize_window()
    driver.get(env.air_pods_case_url)
    air_pods_case_instance = AirPodsCasePage(driver)
    yield air_pods_case_instance
    driver.quit()


@pytest.fixture()
def air_pods2(env):
    driver = create_driver_factory(env.browser_id)
    driver.maximize_window()
    driver.get(env.air_pods2_url)
    air_pods2_instance = AirPods2Page(driver)
    yield air_pods2_instance
    driver.quit()


@pytest.fixture()
def apple_books_navigate(env):
    driver = create_driver_factory(env.browser_id)
    driver.maximize_window()
    driver.get(env.books_url)
    apple_books_instance = AppleBooksPage(driver)
    yield apple_books_instance
    driver.quit()


@pytest.fixture()
def retail_page_navigate(env):
    driver = create_driver_factory(env.browser_id)
    driver.maximize_window()
    driver.get(env.retail_page)
    retail_page_instance = RetailPage(driver)
    yield retail_page_instance
    driver.quit()


@pytest.fixture()
def apple_store_navigate(env):
    driver = create_driver_factory(env.browser_id)
    driver.maximize_window()
    driver.get(env.apple_store_url)
    apple_store_page_instance = AppleStorePage(driver)
    yield apple_store_page_instance
    driver.quit()


@pytest.fixture()
def apple_home_pod_navigate(env):
    driver = create_driver_factory(env.browser_id)
    driver.maximize_window()
    driver.get(env.home_pod)
    home_pod_instance = HomePodPage(driver)
    yield home_pod_instance
    driver.quit()


@pytest.fixture(scope='session', autouse=True)
def env():
    with open('../../configurations/env1.json') as file:
        f_data = file.read()
        json_data = json.loads(f_data)
        return ConfigObject(**json_data)
