from time import sleep


class LinkedinCrawler:
    def __init__(self, driver):
        self.driver = driver

    def login_linkedin(self, user_name, password):
        self.driver.get('https://www.linkedin.com')
        sleep(0.5)

        username_field = self.driver.find_element_by_class_name('input__input')
        password_field = self.driver.find_element_by_name('session_password')

        username_field.send_keys(user_name)
        sleep(0.5)
        password_field.send_keys(password)

        sleep(0.5)
        sign_in_button = self.driver.find_element_by_xpath(
            '//*[@type="submit"]')
        sign_in_button.click()
        sleep(0.5)

    def get_data_from_profiles(self, profiles):
        linkedin_data = list()
        for profile in profiles:
            profile_data = self.get_cards_data_on_profile(profile)
            linkedin_data.append(profile_data)
        return linkedin_data

    def get_cards_data_on_profile(self, profile):
        metrics_profile = list()
        medias_profile = list()
        profile_name = profile.get('profile')
        self.__go_to_profile_page(profile_name)
        cards = self.driver.find_elements_by_xpath(
            '//div[@class="feed-container-theme"]/div/div')
        print(f"CARDS FOUND --- {len(cards)}")
        cards_count = len(cards)
        if not cards_count:
            print(f"CARDS FOUND --- {cards_count}")
            html = self.driver.execute_script("return document.body.outerHTML;")
            print(html)
        for card in cards:
            card_data = self.__get_card_data(card)
            media = self.__get_card_media(card)
            if card_data:
                metrics_profile.append({
                    'post_id': card_data.get('card_id'),
                    'text': card_data.get('card_text'),
                    'metrics': card_data.get('metrics'),
                    'account_code': profile.get('account_code'),
                    'profile_name': profile.get('profile')
                })
            if media and card_data:
                post_id = card_data.get('card_id')
                medias_profile.append({
                    'post_id': post_id,
                    'url': media.get('url'),
                    'name': f"linkedin_{post_id}",
                    'type': 'jpg',
                    'from': 'Linkedin',
                    'downloaded': False
                })
        return metrics_profile, medias_profile

    def __go_to_profile_page(self, profile_name):
        self.driver.get(
            f"https://www.linkedin.com/company/{profile_name}/posts/?feedView=all")
        sleep(0.5)

        # Insertion of the Scroll Down starting at 0 px to 300k px or to 900k px make no difference
        self.driver.execute_script('window.scrollBy(0,900000)', '')
        sleep(2)

    def __get_card_data(self, card):
        try:
            cards_id = card.find_element_by_xpath('.//div[1]')
            cards_likes = card.find_element_by_xpath(
                './/div/div/div[@class="social-details-social-activity update-v2-social-activity"]/ul/li[1]/button/span')
            cards_comments = card.find_element_by_xpath(
                './/div/div/div[@class="social-details-social-activity update-v2-social-activity"]/ul/li[2]/button/span')
            cards_text = card.find_element_by_xpath(
                './/div/div[@class="feed-shared-update-v2__description-wrapper ember-view"]')
            likes = cards_likes.text.split(' ')[0]
            comments = cards_comments.text.split(' ')[0]
            card_id = cards_id.get_attribute("data-urn").split(':')[3]
            text = cards_text.text
            return {
                'card_id': card_id,
                'card_text': text,
                'metrics': {
                    'card_likes': likes,
                    'card_comments': comments,
                }
            }
        except Exception as error:
            print(f'Card do not have any metrics {error}')

    def __get_card_media(self, card):
        try:
            cards_images = card.find_element_by_xpath(
                './/div/div/div[@class="feed-shared-update-v2__content feed-shared-image feed-shared-image--single-image ember-view"]/div/div/button/div/div/img')
            media = {
                'url': cards_images.get_attribute("src"),
                'type': 'jpg'
            }
            return media
        except Exception:
            print('Card do not have any media')
