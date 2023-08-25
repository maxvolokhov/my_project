import json
import pytest
from utilities.config_obj import ConfigObject
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


@pytest.fixture(scope='session', autouse=True)
def env():
    with open('../../configurations/env1.json') as file:
        f_data = file.read()
        json_data = json.loads(f_data)
        return ConfigObject(**json_data)


def page_fixture(page_class, page_url_attr):
    @pytest.fixture()
    def navigate_to_page_fixture(env):
        driver = create_driver_factory(env.browser_id)
        driver.maximize_window()
        driver.get(getattr(env, page_url_attr))
        page_instance = page_class(driver)
        yield page_instance
        driver.quit()

    return navigate_to_page_fixture


navigate_to_main_page = page_fixture(MainPage, "base_url")
navigate_to_buy_section = page_fixture(BuyIphonePage, "buy_page_url")
navigate_to_cart = page_fixture(RetailPage, "item_in_cart_url")
macbook_page = page_fixture(MacbookPage, "macbook_url")
apple_watch_page = page_fixture(AppleWatchPage, "apple_watch_url")
air_tag_page = page_fixture(AirTagPage, "air_tag_url")
air_pods_navigate = page_fixture(AirPodsPage, "air_pods_url")
apple_tv_navigate = page_fixture(AppleTvPage, "apple_tv_url")
air_pods_case = page_fixture(AirPodsCasePage, "air_pods_case_url")
air_pods2 = page_fixture(AirPods2Page, "air_pods2_url")
apple_books_navigate = page_fixture(AppleBooksPage, "apple_books_url")
retail_page_navigate = page_fixture(RetailPage, "retail_page_url")
apple_store_navigate = page_fixture(AppleStorePage, "apple_store_url")
apple_home_pod_navigate = page_fixture(HomePodPage, "apple_home_pod_url")
