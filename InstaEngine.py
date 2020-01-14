# necessary imports for the class
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from time import sleep
import random
import re

calib_factor_for_scroll_up = 650
driver = webdriver.Firefox()
driver.get("http:\\www.instagram.com")


class InstaAuto:
    '''
    Class to provide all the necessary functions for the automation of instagram
    '''

    def __init__(self):
        self.comments = ["nice one", "well said", "beautiful", "admirable", "I am impressed by this post",
                         "forget to survive now", "I see", '(y)', 'cant say anything', 'i needed this post. :P']

    def on_screen_visible_post_selector(self):
        '''
        method to return the multiplier that gives the visible post for the page.
        :return: None
        '''
        current_scroll_position = self.driver.execute_script("return window.pageYOffset")
        loaded_page_size_length = self.driver.execute_script("return document.body.parentNode.scrollHeight")
        print("=================================\nCurrent Position: ", current_scroll_position)
        print("Current Length:  ", loaded_page_size_length)
        print("Ratio:  ", current_scroll_position / float(loaded_page_size_length))

        return current_scroll_position / float(loaded_page_size_length)

    def human_effect_delay(self):
        '''
        Method to produce a random delay.
        :return: None
        '''
        sleep(random.randint(2, 5))

    def comment_generator(self):
        return self.comments[random.randint(0, len(comments))]

    def keyboard_input_human_imitator(self, string_to_be_sent, element):
        '''
        Method  to send the string to the element in human effect. (Similar to typing manner)
        :param string_to_be_sent: String to send to the element
        :param element: Element which accepts the string passed
        :return: None
        '''
        letters = list(string_to_be_sent)
        for letter in letters:
            element.send_keys(letter)
            sleep(random.random() / 3)

    def scroll_down(self, pixel=10, time_lag=2, iteration=1):
        '''
         Method to scroll down the screen.
        :param pixel: The pixel of loaded page you want to scroll down
        :param time_lag: The wait time in each consecutive scroll effect (default is 2 sec)
        :param iteration: The number of times the scroll effect to follow (default is 1)
        :return: None
        '''
        addpixel = pixel
        while iteration:
            script_scroll_down = "window.scrollTo(0, document.documentElement.scrollTop +" + str(
                int(addpixel + 1)) + ");"
            current_scroll_position = driver.execute_script("return document.documentElement.scrollTop")
            # print("Current Position while scrolling down: ", current_scroll_position)
            driver.execute_script(script_scroll_down)
            sleep(time_lag)
            iteration -= 1

    def scroll_up(self, pixel=10, time_lag=2, iteration=1):
        '''
         Method to scroll up the screen.
        :param pixel: The pixel of loaded page you want to scroll up
        :param time_lag: The wait time in each consecutive scroll effect (default is 2 sec)
        :param iteration: The number of times the scroll effect to follow (default is 1)
        :return: None
        '''
        addpixel = pixel
        while iteration:
            if driver.execute_script(
                    "return document.documentElement.scrollTop ") - addpixel + calib_factor_for_scroll_up > 0:
                script_scroll_up = "window.scrollTo(0, document.documentElement.scrollTop -" + str(
                    int(addpixel + 1)) + ");"
                current_scroll_position = driver.execute_script("return window.pageYOffset")
                # print("Current Position while scrolling up: ", current_scroll_position)
                driver.execute_script(script_scroll_up)
                sleep(time_lag)
            else:
                script_scroll_up = "window.scrollTo(0, 0);"
                driver.execute_script(script_scroll_up)
            iteration -= 1

    def page_loader(self, page_size_length_to_load_in_unit_iteration=500, iteration=2, scroll_unit_time=2,
                    scroll_unit_in_pixel=10, scroll_in_iteration=1):
        '''
        Method which is a page preprocessor, basically loads the page to certain length specified by arguments.
        :param page_size_length_to_load_in_unit_iteration: Page size to load in per iteration. The size is in pixel dim.
        :param iteration: Number of times the page loads (increases the length by scrolling down).
        :param scroll_unit_time: Scroll effect unit time.
        :param scroll_unit_in_pixel: Pixel to move in single scroll effect.
        :param scroll_in_iteration: Number of times the scroll effect should take.
        :return: None
        '''
        driver.set_page_load_timeout(15)
        new_post_click("instagram")
        i = 1
        while i <= iteration:
            while driver.execute_script(
                    "return document.documentElement.scrollTop ") < page_size_length_to_load_in_unit_iteration * i:
                scroll_down(scroll_unit_in_pixel, scroll_unit_time, scroll_in_iteration)
            i += 1
        while driver.execute_script(
                "return document.documentElement.scrollTop ") > 0:
            scroll_up(scroll_unit_in_pixel, scroll_unit_time / 5, scroll_in_iteration)
        print("[success]Page Loaded.")
        sleep(random.randint(5, 10))

    def login_instagram(self, username, password,
                        login_page='https://www.instagram.com/accounts/login/?source=auth_switcher',
                        human_effect=True):
        '''
        Method to login in instagram by opening 'https://www.instagram.com/accounts/login/?source=auth_switcher' page.
        The page set is default and can be changed to different by modifying the value of "login_page" argument.
        :param username: The instagram username of the user/client.
        :param password: The password required for login corresponding to specified username.
        :param login_page: The login page address in format of 'https://www.instagram.com/.../.../...'
        :param human_effect: If the value is true. It makes whole process delayed by random time intervals. (Recommended)
        :return: None
        '''
        random.seed(datetime.now().second)
        driver.get(login_page)
        print("Please Wait")
        if human_effect:
            self.human_effect_delay()
        else:
            sleep(2)
        usrnm = driver.find_element_by_name("username")
        usrnm.clear()
        if human_effect:
            self.human_effect_delay()
        else:
            sleep(2)
        self.keyboard_input_human_imitator(username, usrnm)
        passwd = driver.find_element_by_name("password")
        if human_effect:
            self.human_effect_delay()
        else:
            sleep(2)
        passwd.clear()
        self.keyboard_input_human_imitator(password, passwd)
        if human_effect:
            self.human_effect_delay()
        else:
            self.sleep(2)
        passwd.send_keys(Keys.TAB)
        if human_effect:
            self.human_effect_delay()
        else:
            sleep(2)
        driver.switch_to.active_element.send_keys(Keys.TAB)
        driver.switch_to.active_element.click()
        print("Trying to login with specified credentials. Please wait( it can take a 30 seconds)")
        sleep(random.randint(10, 25))
        if driver.current_url == "https://www.instagram.com/" or driver.current_url == "http://www.instagram.com/":
            print("[success]Logged In Successfully")

        else:
            print("[failure]Certain Problem occurred")
            print("::::::::::::::::::::::::::Error Page Source Code (start)::::::::::::::::::::::::::::\n\n")
            print(driver.page_source)
            print("\n\n::::::::::::::::::::::::::Error Page Source Code (end)::::::::::::::::::::::::::::")

    def button_clicker(self, text_on_button, regular_expression=False, single_click=True, do_random=False):
        '''
        Method to perform a click action on the loaded page.
        :param do_random:
        :param single_click:
        :param regular_expression: text_on_button is a regular expression if this parameter is true.
        :param text_on_button: Text on the button you want to click
        :return: None
        '''
        buttons = driver.find_elements_by_tag_name("button")
        sure = 1
        for button in buttons:
            # print("button found:", button.text)
            if regular_expression:
                if re.search(text_on_button, button.text) and sure:
                    try:
                        button.click()
                        print("[success]button clicked: ", button.text)
                    except:
                        print("[failure]cant click. some problem. Attempted on: ", button.text)
                    if single_click:
                        break
                    else:
                        self.human_effect_delay()

            else:
                if (button.text == text_on_button) and sure:
                    try:
                        button.click()
                        print("[success]button clicked: ", button.text)
                    except:
                        print("[failure]cant click. some problem")
                    if single_click:
                        break
                    else:
                        sleep(random.randint(2, 6))
            if do_random:
                sure = (random.randint(2, 1000) % 2)

    def link_clicker(self, text_on_link, regular_expression=False, single_click=True, do_random=False):
        '''
        Method to perform a click action on the loaded page.
        :param do_random:
        :param single_click:
        :param regular_expression: text_on_button is a regular expression if this parameter is true.
        :param text_on_link: Text on the link you want to click
        :return: None
        '''
        links = driver.find_elements_by_tag_name("a")
        sure = 1
        for link in links:
            # print("link found: ", link.text)
            if regular_expression:
                if re.search(text_on_link, link.text) and sure:
                    try:
                        link.click()
                        print("[success]link clicked clicked: ", link.text)
                    except:
                        print("[failure]cant click the link: ", link.text)
                    if single_click:
                        break
                    else:
                        sleep(random.randint(2, 6))

            else:
                if (link.text == text_on_link) and sure:
                    try:
                        link.click()
                        print("[success]link clicked clicked: ", link.text)
                    except:
                        print("[failure]cant click. some problem")
                    if single_click:
                        break
                    else:
                        sleep(random.randint(2, 6))
            if do_random:
                sure = (random.randint(2, 1000) % 2)

    def all_link_grabber(self, text_on_link, regular_expression=False):
        '''
        Method to collect all the links with given text on the loaded page.
        :param regular_expression: text_on_link is a regular expression if this parameter is true.
        :param text_on_link: Text on the link you want to grab
        :return: None
        '''
        links = driver.find_elements_by_tag_name("a")
        links_with_text = []
        for link in links:
            if regular_expression:
                if re.search(text_on_link, link.text):
                    try:
                        links_with_text.append(link)
                    except:
                        print("[failure]cant get the a link: ", link.text)
            else:
                if link.text == text_on_link:
                    try:
                        links_with_text.append(link)
                    except:
                        print("[failure]cant get the a link: ", link.text)
        return links_with_text

    def all_button_grabber(self, text_on_button, regular_expression=False):
        '''
        Method to collect all the buttons with given text on the loaded page.
        :param regular_expression: text_on_button is a regular expression if this parameter is true.
        :param text_on_button: Text on the button you want to grab
        :return: None
        '''
        buttons = driver.find_elements_by_tag_name("button")
        buttons_with_text = []
        for button in buttons:
            if regular_expression:
                if re.search(text_on_button, button.text):
                    try:
                        buttons_with_text.append(button)
                    except:
                        print("[failure]cant get the a button: ", button.text)
            else:
                if button.text == text_on_button:
                    try:
                        buttons_with_text.append(button)
                    except:
                        print("[failure]cant get the a button: ", button.text)
        return buttons_with_text

    def turn_on_notification(self, website="instagram"):
        '''
         Method to turn on and off desktop notification, in case popped up.
        :param website: The website to get notification from, e.g. instagram, facebook...
        :return: None
        '''
        if website == "instagram":
            self.button_clicker("Not Now")

    def post_likers_click(self, website="instagram"):
        '''
         Method to get likers overlay of a post.
        :param website: The website to get notification from, e.g. instagram, facebook...
        :return: None
        '''
        if website == "instagram":
            self.button_clicker("^[0-9].*likes$", regular_expression=True)
            self.human_effect_delay()
            try:
                driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
            except:
                print("[failure]cant close the overlay. There may be no overlay.")

    def insta_follow_engine_go(self, single_user=False):
        '''
        Method to click all the follow buttons randomly. It is not necessary that it clicks all the follow buttons.
        :param single_user: keep it true if you there is only one user.
        :return: None
        '''
        self.button_clicker("Follow", regular_expression=False, single_click=single_user, do_random=True)

    def scroll_to(self, pos, step=1):
        pxl = (pos - driver.execute_script("return document.documentElement.scrollTop ")) / step
        if pxl >= 0:
            while driver.execute_script("return document.documentElement.scrollTop ") < pos:
                print(
                    "*************************************************************************scroll down test succesee")
                sleep(1)
                scroll_down(pixel=pxl, time_lag=random.randint(25, 50) / 1000, iteration=step)
                if pxl <= 2:
                    break
        else:
            while driver.execute_script("return document.documentElement.scrollTop ") > pos:
                print(
                    "*************************************************************************scroll up test succesee")
                sleep(1)
                scroll_up(pixel=-pxl, time_lag=random.randint(35, 60) / 1000, iteration=step)
                if (-pxl) <= 2:
                    break

    def new_post_click(self, website="instagram"):
        '''
         Method to get new posts in case the page is not loading and asks for refresh or new post.
        :param website: The website to get notification from, e.g. instagram, facebook...
        :return: None
        '''
        if website == "instagram":
            self.button_clicker("New Posts")

    def insta_post_specific_actions(self, number_of_actions=5):
        '''
        Methode basically called inside insta_view_all_comments_clicker. and performs some randomly picked
        actions like 'liking', 'commenting', and 'bookmarking' the posts opened.
        works in post level depth only.
        :return: None
        '''
        action_distribution_proba = [3, 2, 2, 2, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 1]
        action_randomizer = random.randint(1, 14)
        potential_user_in_comment_text = driver.find_elements_by_tag_name("a")
        user_in_comment_text = []
        for user in potential_user_in_comment_text:
            if re.search("^@([0-9a-zA-Z_ ]+)", user.text):
                user_in_comment_text.append(user)
                print("user found in text: ", user.text)
        repeater = number_of_actions
        while repeater:
            print(action_distribution_proba)
            print(action_distribution_proba[action_randomizer])
            arrow_down = random.randint(1, 5)
            while arrow_down:
                try:
                    driver.find_element_by_xpath(
                        "/html/body/div[1]/section/main/div/div/article/div[2]/div[1]/ul").send_keys(Keys.ARROW_DOWN)
                except:
                    print("[failure]cant execute arrow down scroll effect on the division")
                arrow_down -= 1
            arrow_up = random.randint(1, 5)
            while arrow_up:
                if action_randomizer % 2:
                    try:
                        driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/div/article/div[2]/div[1]/ul").send_keys(
                            Keys.ARROW_UP)
                    except:
                        print("[failure]cant execute arrow up scroll effect on the division")
                arrow_up -= 1
            self.human_effect_delay()
            # this segment is to click at like
            if action_distribution_proba[action_randomizer] == 1:
                for i in range(len(action_distribution_proba)):
                    if action_distribution_proba[i] == 1:
                        action_distribution_proba[i] = 4
                try:
                    driver.find_element_by_xpath(
                        "/html/body/div[1]/section/main/div/div/article/div[2]/section[1]/span[1]/button").click()
                except:
                    print("[failure]post is not liked. Failed in xpath")
            # this segment is to comment something
            elif action_distribution_proba[action_randomizer] == 2:
                for i in range(len(action_distribution_proba)):
                    if action_distribution_proba[i] == 2:
                        action_distribution_proba[i] = 4
                        break
                try:
                    comment_field = driver.find_element_by_xpath(
                        "/html/body/div[1]/section/main/div/div/article/div[2]/section[3]/div/form/textarea")
                    try:
                        comment_field.click()
                    except:
                        print("[failure]unable to click at the comment field")
                    self.keyboard_input_human_imitator(comment_generator(), comment_field)
                    self.button_clicker("Post")

                except:
                    print("[failure]comment was not successful.")
            # this segment is to bookmark the post
            elif action_distribution_proba[action_randomizer] == 3:
                for i in range(len(action_distribution_proba)):
                    if action_distribution_proba[i] == 3:
                        action_distribution_proba[i] += 1
                try:
                    driver.find_element_by_xpath(
                        "/html/body/div[1]/section/main/div/div/article/div[2]/section[1]/span[3]/button").click()
                except:
                    print("[failure]post is not bookmarked.")
            elif action_distribution_proba[action_randomizer] == 4:
                level_url = driver.current_url
                try:
                    user_to_follow = user_in_comment_text[random.randint(0, len(user_in_comment_text))]
                    user_to_follow.click()
                    print("user profile opening: user handle-->> ", user_to_follow.text)
                except:
                    print("[failure]user link is not working by click.")
                sleep(2)
                self.human_effect_delay()
                try:
                    self.insta_follow_engine_go(single_user=True)
                except:
                    print("[failure]post is not bookmarked.")
                self.human_effect_delay()
                self.scroll_down(random.randint(50, 200), 0.2, 2)
                if level_url != driver.current_url:
                    driver.back()
            action_randomizer = random.randint(1, 14)
            repeater -= 1
        else:
            pass
        driver.back()

    def insta_view_all_comments_clicker(self):
        '''
        Method to click on the view all comments given usually at the bottom of the post.
        this methode may increase the page active depth by one.
        :return: None
        '''
        self.link_clicker("^View.*comments$", regular_expression=True)
        sleep(8)
        self.insta_post_specific_actions()

    def search_comment_fields_on_homepage(self):
        '''
        Method which returns the list of the comment field elements.
        :return: List of comment field element
        '''
        articles = driver.find_elements_by_xpath("//article")
        size_of_articles = len(articles)
        comment_field = []
        for i in range(size_of_articles):
            xpath = "//article[" + str(i + 1) + "]/div[2]/section[3]/div/form/textarea"
            try:
                element = driver.find_element_by_xpath(xpath)
                comment_field.append(element)
            except:
                print("[failure]Missed an comment field to locate")
        return comment_field

    def search_love_icon_on_homepage(self):
        '''
        Method which returns the list of love icon elements.
        :return: List of love icon element
        '''
        articles = driver.find_elements_by_xpath("//article")
        size_of_articles = len(articles)
        Love_icons = []
        for i in range(size_of_articles):
            xpath = "//article[" + str(i + 1) + "]/div[2]/section[1]/span[1]/button"
            try:
                element = driver.find_element_by_xpath(xpath)
                Love_icons.append(element)
            except:
                print("[failure]Missed an love icon to locate")
        return Love_icons

    def homepage_like_post_engine_go(self, website="instagram", human_effect=True):
        '''
        Method to like a post or article in website
        :param website: The website to get posts or articles from, e.g. instagram, facebook...
        :param human_effect: If the value is true. It makes whole process delayed by random time intervals. (Recommended)
        :return: None
        '''
        if website == "instagram":
            total_heart_count = 0
            while 1:
                choice = random.randint(1, 3)
                articles = driver.find_elements_by_xpath("//article")
                iterator = random.randint(1, len(articles))
                print("Length of articles list: ", len(articles))
                print("+++++++++++++++++++++++++++\n Accessing element in articles: position being accessed: : ",
                      iterator, "\n+++++++++++++++++++++++++++++")
                # print(round(on_screen_visible_post_selector() * len(articles)))
                xpath = "//article[" + str(iterator) + "]/div[2]/section[1]/span[1]/button"
                if 1:
                    try:
                        ele = driver.find_element_by_xpath(xpath)
                        scroll_posi = ele.location
                        print(" Heart icon Located in the page Y Position: ", scroll_posi['y'])
                        self.scroll_to(scroll_posi['y'], step=60)
                        self.human_effect_delay()
                        ele.click()
                        total_heart_count += 1
                        print("heart icon clicked. Total clicked: ", total_heart_count)
                    except:
                        print("[failure]Heart icon was not recognised with like button")
                    if human_effect:
                        sleep(random.randint(2, 8))
                    else:
                        sleep(2)
                if choice == 2:
                    self.insta_follow_engine_go()
                if choice == 3:
                    self.insta_view_all_comments_clicker()

                self.scroll_down(random.randint(10, 35), random.randint(30, 50) / 1000, random.randint(10, 25))
                sleep(random.randint(2, 8))

    def insta_strategy_one(self):
        choice = random.randint(1, 7)
        # choice = 5

        if choice == 1:
            """
            The choice 1 is to follow the users at homepage without following any link. 
            """
            print("Follow users choice")
            self.insta_follow_engine_go()

        if choice == 2:
            """
            The choice 2 is to comment on the randomly selected comment field on homepage without following any link.
            """
            print("Comment choice")
            comment_fields_on_home_page = self.search_comment_fields_on_homepage()
            if len(comment_fields_on_home_page) > 0:
                selected_comment_field = comment_fields_on_home_page[
                    random.randint(0, len(comment_fields_on_home_page) - 1)]
                try:
                    self.scroll_to(selected_comment_field.location['y'] - calib_factor_for_scroll_up, step=50)
                except:
                    print("[failure]Getting Location of a comment field failed.")
                try:
                    self.human_effect_delay()
                    selected_comment_field.click()
                except:
                    print("[failure]unable to click at the comment field")
                try:
                    self.keyboard_input_human_imitator(comment_generator(), selected_comment_field)
                except:
                    print("Cant Comment [X]")
                sleep(2)
                try:
                    selected_comment_field.send_keys(Keys.ENTER)
                except:
                    print("Cant press enter key [X]")

            else:
                print("There is nothing in comment field list")

        if choice == 3:
            """
            The choice 3 is to like on the randomly selected post on homepage without following any link.
            """
            print("like post of users choice")
            love_icon_on_home_page = self.search_love_icon_on_homepage()
            if len(love_icon_on_home_page) > 0:
                selected_love_icon = love_icon_on_home_page[
                    random.randint(0, len(love_icon_on_home_page) - 1)]
                try:
                    self.scroll_to(selected_love_icon.location['y'] - calib_factor_for_scroll_up, step=50)
                except:
                    print("[failure]Getting Location of a love icon failed.")
                try:
                    selected_love_icon.click()
                except:
                    print("[failure]unable to click at the love icon")
            else:
                print("There is nothing in love icon list")

        if choice == 4:
            """
            The choice 4 is to click on the view all comments randomly and then do post specific things like comment, follow users etc
            """
            print("view all comments choice")
            view_all_comments_links_on_home_page = self.all_link_grabber("^View.*comments$", regular_expression=True)
            if len(view_all_comments_links_on_home_page) > 0:
                selected_view_all_comment = view_all_comments_links_on_home_page[
                    random.randint(0, len(view_all_comments_links_on_home_page) - 1)]
                try:
                    self.scroll_to(selected_view_all_comment.location['y'] - calib_factor_for_scroll_up, step=50)
                except:
                    print("[failure]Getting Location of a view all comments failed.")
                try:
                    selected_view_all_comment.click()
                    sleep(8)
                    self.insta_post_specific_actions(number_of_actions=5)

                except:
                    print("[failure]unable to click at the link to viwe all comments")
            else:
                print("There is nothing in love icon list")

        if choice == 5:
            """
            The choice 5 is to click on the all likes button and then follow random users.
            """
            print("view all likes choice")
            all_like_buttons_on_home_page = self.all_button_grabber("^[0-9].*likes$", regular_expression=True)
            if len(all_like_buttons_on_home_page) > 0:
                selected_all_likes_button = all_like_buttons_on_home_page[
                    random.randint(0, len(all_like_buttons_on_home_page) - 1)]
                try:
                    self.scroll_to(selected_all_likes_button.location['y'] - calib_factor_for_scroll_up, step=50)
                except:
                    print("[failure]Getting Location of a all likes failed.")
                try:
                    selected_all_likes_button.click()
                    self.human_effect_delay()
                    self.insta_follow_engine_go()
                    try:
                        driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
                    except:
                        print("[failure]cant close the overlay. There may be no overlay.")
                except:
                    print("[failure]unable to click at the link to all likes")
            else:
                print("There is nothing in all likes list")

        if choice == 6:
            """The choice 6 is to refresh"""
            print("refresh choice")
            driver.refresh()

        if choice == 7:
            """This choice is to follow any random user mentioned on homepage"""
            print("Follow users profile by opening choice")
            users = self.all_link_grabber("^@([0-9a-zA-Z_ ]+)", regular_expression=True)
            if len(users) > 0:
                selected_user = users[
                    random.randint(0, len(users) - 1)]
                try:
                    self.scroll_to(selected_user.location['y'] - calib_factor_for_scroll_up, step=50)
                except:
                    print("[failure]Getting Location of a user.")
                try:
                    sleep(random.random())
                    selected_user.click()
                    self.human_effect_delay()
                    self.insta_follow_engine_go()
                    driver.back()
                except:
                    print("[failure]unable to click at the link to user")
            else:
                print("There is nothing in user list")

    def logOut(self):
        driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/a").click()
        sleep(2)
        self.human_effect_delay()
        driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div/button").click()
        self.human_effect_delay()
        self.button_clicker("Log Out")
        self.human_effect_delay()
        sleep(4)
        self.link_clicker("Log in")
        self.human_effect_delay()

    def insta_auto_start(self, password, username, action_limit):
        self.login_instagram(username, password, human_effect=True)
        self.turn_on_notification("instagram")
        sleep(8)
        loop_iter = 0
        No_actions = 0
        while 1:

            if No_actions == action_limit:
                self.logOut()
                break
            try:
                self.insta_strategy_one()
                No_actions += 1
            except:
                print("Unexpected Error")
            self.scroll_down(random.randint(10, 35), random.randint(30, 50) / 1000, random.randint(10, 25))
            sleep(random.randint(2, 8))
            loop_iter += 1
            print("Iteration: ", loop_iter)


if __name__ == "__main__":
    obj = InstaAuto()
    obj.insta_auto_start("passward", "username", 5)
