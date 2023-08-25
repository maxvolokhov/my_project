import pytest


@pytest.mark.smoke
def test_apple_news(navigate_to_main_page):
    apple_news_page = navigate_to_main_page.go_apple_news()
    apple_news_page.click_try_one_month()
    assert apple_news_page.expected_text_return in apple_news_page.is_ios_consists(), 'Transition has not been executed'


@pytest.mark.regression
def test_podcasts_transition(navigate_to_main_page):
    apple_podcasts_page = navigate_to_main_page.podcasts_transition()
    apple_podcasts_page.drop_down_click().go_by_link()
    assert apple_podcasts_page.url_located == navigate_to_main_page._driver.current_url, '''Transition has not 
    been executed'''


@pytest.mark.smoke
@pytest.mark.regression
def test_business_pdf(navigate_to_main_page):
    business_page = navigate_to_main_page.business_transition()
    business_page.enterprise_click().pdf_click()
    assert business_page.is_pdf_displayed(), 'PDF file has not been downloaded'


@pytest.mark.smoke
@pytest.mark.regression
def test_apple_gift(apple_store_navigate, env):
    r_name, r_email = env.recipient_name, env.recipient_email
    s_name, s_email = env.sender_name, env.sender_email
    apple_store_navigate.apple_gift_transition()
    gift_card_page = apple_store_navigate.click_buy()
    gift_card_page.click_mail().amount_select().field_active().set_r_name(r_name).field_active2().set_r_email(
        r_email).field_active3().set_s_name(s_name).field_active4().set_s_email(s_email).click_for_text().add_to_cart()
    assert gift_card_page.expected_text_return in gift_card_page.is_item_got(), '''Apple gift card has not been added 
    to the bag'''


@pytest.mark.regression
def test_apple_vision_notify(navigate_to_main_page):
    apple_vision_page = navigate_to_main_page.apple_vision_transition()
    apple_vision_page.notify_me_click().make_input_field_active_click().set_email().submit_button_click()
    assert apple_vision_page.expected_text_return in apple_vision_page.is_notify_got(), '''Created mail occurred as 
    appropriate'''
