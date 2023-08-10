from config_reader import Readconfig
from page_objects.apple_store_page import AppleStorePage
from page_objects.main_page import MainPage
import pytest


@pytest.mark.smoke
def test_apple_news(create_driver):
    driver = create_driver
    main_page = MainPage(driver)
    apple_news_page = main_page.go_apple_news()
    apple_news_page.click_try_one_month()
    assert apple_news_page.ios_validate(), 'Transition has not been executed'


@pytest.mark.regression
def test_podcasts_transition(create_driver):
    driver = create_driver
    main_page = MainPage(driver)
    apple_podcasts_page = main_page.podcasts_transition()
    apple_podcasts_page.drop_down_click().go_by_link()
    assert apple_podcasts_page.url_assert() == driver.current_url, 'Transition has not been executed'


@pytest.mark.smoke
@pytest.mark.regression
def test_business_pdf(create_driver):
    driver = create_driver
    main_page = MainPage(driver)
    business_page = main_page.business_transition()
    business_page.enterprise_click().pdf_click()
    assert business_page.pdf_check(), 'PDF file has not been downloaded'


@pytest.mark.smoke
@pytest.mark.regression
def test_apple_gift(apple_store_navigate):
    r_name, r_email = Readconfig.get_recipient()
    s_name, s_email = Readconfig.get_sender()
    driver = apple_store_navigate
    apple_store_page = AppleStorePage(driver)
    apple_store_page.apple_gift_transition()
    gift_card_page = apple_store_page.click_buy()
    gift_card_page.click_mail().amount_select().field_active().set_r_name(r_name).field_active2().set_r_email(
        r_email).field_active3().set_s_name(s_name).field_active4().set_s_email(s_email).click_for_text().add_to_cart()
    assert gift_card_page.make_validate(), 'Apple gift card has not been added to the bag'


@pytest.mark.regression
def test_apple_vision_notify(create_driver):
    driver = create_driver
    main_page = MainPage(driver)
    apple_vision_page = main_page.apple_vision_transition()
    apple_vision_page.notify_me_click().input_click().set_email().submit_button_click()
    assert apple_vision_page.notify_validate(), 'Created mail occurred as appropriate'
