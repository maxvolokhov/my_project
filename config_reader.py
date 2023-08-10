import configparser

config = configparser.RawConfigParser()
config.read('../../configurations/app_config.ini')


class Readconfig:

    @staticmethod
    def get_base_url():
        return config.get('app_data', 'base_url')

    @staticmethod
    def get_browser_id():
        return config.get('browser_data', 'browser_id')

    @staticmethod
    def get_creds():
        return config.get('credentials', 'apple_id'), config.get('credentials', 'password')

    @staticmethod
    def get_buy_page():
        return config.get('buy_page', 'buy_page_url')

    @staticmethod
    def get_cart_page():
        return config.get('cart_page', 'item_in_cart_url')

    @staticmethod
    def search_input_get():
        return config.get('search_line', 'search_input')

    @staticmethod
    def get_macbook_url():
        return config.get('macbook_page', 'macbook_url')

    @staticmethod
    def get_apple_watch_url():
        return config.get('apple_watch', 'apple_watch_url')

    @staticmethod
    def get_air_tag_url():
        return config.get('air_tag', 'air_tag_url')

    @staticmethod
    def get_air_pods_url():
        return config.get('air_pods', 'air_pods_url')

    @staticmethod
    def get_apple_tv_url():
        return config.get('apple_tv', 'apple_tv_url')

    @staticmethod
    def get_air_pods_case_url():
        return config.get('air_pods_case', 'air_pods_case_url')

    @staticmethod
    def get_air_pods2_url():
        return config.get('air_pods2', 'air_pods2_url')

    @staticmethod
    def get_books_url():
        return config.get('apple_books', 'apple_books_url')

    @staticmethod
    def get_search_input():
        return config.get('search_store', 'store_name')

    @staticmethod
    def get_retail_page():
        return config.get('retail_page', 'retail_page_url')

    @staticmethod
    def get_apple_store():
        return config.get('apple_store', 'apple_store_url')

    @staticmethod
    def get_accessories_search():
        return config.get('search_accessories', 'accessories_name')

    @staticmethod
    def get_home_pod():
        return config.get('apple_home_pod', 'apple_home_pod_url')

    @staticmethod
    def get_recipient():
        return config.get('recipient', 'recipient_name'), config.get('recipient', 'recipient_email')

    @staticmethod
    def get_sender():
        return config.get('sender', 'sender_name'), config.get('sender', 'sender_email')
