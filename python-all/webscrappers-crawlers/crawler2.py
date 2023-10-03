from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class InstagramCrawler:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)


    def login_instagram(self, user_name, password):
        self.driver.get('https://www.instagram.com/accounts/login/')
        sleep(2)

        self.wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))

        username_field = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        password_field = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')

        username_field.send_keys(user_name)
        sleep(2)
        password_field.send_keys(password)

        sleep(2)
        sign_in_button = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[3]/button/div')
        sign_in_button.click()
        sleep(2)

    def get_data_from_profiles(self, profiles):
        instagram_data = list()
        for profile in profiles:
            profile_data = self.get_cards_data_on_profile(profile)
            instagram_data.append(profile_data)
        return instagram_data

    def get_cards_data_on_profile(self, profile):
        metrics_profile = list()
        medias_profile = list()
        profile_name = profile.get('profile')
        self.__go_to_profile_page(profile_name)
        cards = list()
        sections = self.driver.find_elements_by_xpath(
            '//article/div/div/div')
        for section in sections:
            cards.extend(section.find_elements_by_xpath(
            './div'))
        print(f"CARDS FOUND --- {len(cards)}")
        cards_count = len(cards)
        if not cards_count:
            print(f"CARDS FOUND --- {cards_count}")
            html = self.driver.execute_script("return document.body.outerHTML;")
            print(html)
        for card in cards:
            card_data = self.__get_card_data(card)
            if card_data:
                metrics_profile.append({
                    'post_id': card_data.get('card_id'),
                    'text': card_data.get('card_text'),
                    'metrics': card_data.get('metrics'),
                    'account_code': profile.get('account_code'),
                    'profile_name': profile.get('profile')
                })
                media = self.__get_card_media(card)
                if media:
                    post_id = card_data.get('card_id')
                    medias_profile.append({
                        'post_id': post_id,
                        'url': media.get('url'),
                        'name': f"instagram_{post_id}",
                        'type': 'jpg',
                        'from': 'Instagram',
                        'downloaded': False
                    })
        return metrics_profile, medias_profile

    def __go_to_profile_page(self, profile_name):
        sleep(2.5)
        self.driver.get(
            f"https://www.instagram.com/{profile_name}/")
        sleep(0.5)

        # Insertion of the Scroll Down starting at 0 px to 300k px or to 900k px make no difference
        self.driver.execute_script('window.scrollBy(0,900000)', '')
        sleep(1.5)

    def __get_card_data(self, card):
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(card).perform()
            cards_id = card.find_element_by_xpath('./a')
            cards_likes = card.find_element_by_xpath(
                './a/div/ul/li[1]/span').text.replace('k', '000')
            cards_comments = card.find_element_by_xpath(
                './a/div/ul/li[2]/span').text
            card_id = cards_id.get_attribute("href").split('/')[4]
            return {
                'card_id': card_id,
                'card_text': '',
                'metrics': {
                    'card_likes': cards_likes,
                    'card_comments': cards_comments,
                }
            }
        except Exception as error:
            print(error)
            print('Card do not have any metrics')

    def __get_card_media(self, card):
        try:
            cards_images = card.find_element_by_xpath(
                './a/div[1]/div/img')
            media = {
                'url': cards_images.get_attribute("src"),
                'type': 'jpg'
            }
            return media
        except Exception:
            print('Card do not have any media')
