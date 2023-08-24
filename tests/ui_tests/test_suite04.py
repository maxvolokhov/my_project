import pytest


@pytest.mark.regression
def test_apple_shop_search(create_driver_main_page, env):
    apple_store_name = env.search_input
    retail_page = create_driver_main_page.store_click()
    retail_page.set_apple_store(apple_store_name).select_from_list()
    assert retail_page.is_store_work_time_displayed(), 'Required apple store has not been selected'


@pytest.mark.smoke
def test_retail_apple_store(retail_page_navigate):
    retail_page_navigate.click_us_drop_down().select_austria()
    vienna_page = retail_page_navigate.austria_store_click()
    assert vienna_page.is_address_is_located(), 'Vienna apple sore has not been found'


@pytest.mark.smoke
@pytest.mark.regression
def test_apple_wallet(create_driver_main_page):
    apple_wallet_page = create_driver_main_page.go_to_wallet()
    apple_wallet_page.drop_down_click()
    support_apple_page = apple_wallet_page.learn_more_click()
    assert support_apple_page.is_text_displayed(), 'Redirect to requested page has not been executed'


@pytest.mark.smoke
def test_accessories_search(apple_store_navigate, env):
    search_input = env.accessories_name
    apple_store_navigate.accessories_click().insert_search_line(search_input, press_enter=True)
    assert apple_store_navigate.is_search_result_displayed(), 'Requested item does not exist'


@pytest.mark.regression
def test_apple_home_pod(apple_home_pod_navigate):
    apple_home_pod_navigate.add_homepod_to_bag()
    bag_page = apple_home_pod_navigate.check_your_bag()
    bag_page.click_quantity_check().click_quantity_value().blank_click()
    assert bag_page.is_final_price_displayed(), '10 items have not been selected'
