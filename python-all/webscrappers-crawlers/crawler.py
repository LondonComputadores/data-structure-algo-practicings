from time import sleep


class FacebookCrawler:
    def __init__(self, driver):
        self.driver = driver

    def login_facebook(self, user_name, password):
        self.driver.get('https://www.facebook.com')
        sleep(0.5)

        user_name_field = self.driver.find_element_by_name('email')
        password_field = self.driver.find_element_by_name('pass')

        user_name_field.send_keys(user_name)
        sleep(0.5)
        password_field.send_keys(password)

        sleep(0.5)
        sign_in_button = self.driver.find_element_by_name('login')
        sign_in_button.click()
        sleep(1)

    def get_data_from_profiles(self, profiles):
        facebook_data = list()
        for profile in profiles:
            profile_data = self.get_cards_data_on_profile(profile)
            facebook_data.append(profile_data)
        return facebook_data

    def get_cards_data_on_profile(self, profile):
        metrics_profile = list()
        medias_profile = list()
        profile_name = profile.get('profile')
        self.__go_to_profile_page(profile_name)
        sleep(1)
        #CARDS LISTS
        cards = self.driver.find_elements_by_xpath(
            '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div[2]/div/div[2]/div[2]/div/div/div')
        if not cards:
            cards = self.driver.find_elements_by_xpath(
                '//div[@data-pagelet="ProfileTimeline"]/div')
        
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
                    'metrics': card_data.get('metrics'),
                    'account_code': profile.get('account_code'),
                    'profile_name': profile.get('profile')
                })
            if media and card_data:
                post_id = card_data.get('card_id')
                medias_profile.append({
                    'post_id': post_id,
                    'url': media.get('url'),
                    'name': f"facebook_{post_id}",
                    'type': 'jpg',
                    'from': 'Facebook',
                    'downloaded': False
                })
        return metrics_profile, medias_profile

    def __go_to_profile_page(self, profile_name):
        self.driver.get(
            f"https://www.facebook.com/{profile_name}/")
        sleep(2)

        # Insertion of the Scroll Down starting at 0 px to 300k px or to 900k px make no difference
        self.driver.execute_script('window.scrollBy(0,900000)', '')
        sleep(2)

    def __get_card_data(self, card):
        try:
            cards_id = card.find_element_by_xpath('.//div[1]')
            cards_likes = card.find_element_by_xpath('.//div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[1]/div/div[1]/div/span/div/span[1]').text.replace('K', '000')
            cards_comments = card.find_element_by_xpath('.//div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/span').text.split(' ')[0]
            cards_shares = card.find_element_by_xpath('.//div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/span').text.split(' ')[0]

            # likes = cards_likes.text.split(' ')[0]
            # comments = cards_comments.text.split(' ')[0]
            card_id = cards_id.get_attribute('class').split(' ')[1]
            return {
                'card_id': card_id,
                'metrics': {
                    'card_likes': cards_likes,
                    'card_comments': cards_comments,
                    'card_shares': cards_shares
                }
            }
        except Exception as error:
            print('Card do not have any metrics', error)

    def __get_card_media(self, card):
        try:
            cards_images = card.find_element_by_tag_name(
                'img')
            media = {
                'url': cards_images.get_attribute("src"),
                'type': 'jpg'
            }
            return media
        except Exception:
            print('Card do not have any media')
