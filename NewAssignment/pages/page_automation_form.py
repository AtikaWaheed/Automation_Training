from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class GoogleFormSubmission(object):
    time_to_wait = 10

    def __init__(self, driver):
        """
        instantiate driver
        """
        self.driver = driver
        self.url = "https://docs.google.com/forms/d/e/1FAIpQLSfSGh4qzssK1gnZ6JEUe1D4E3lmGCelVD0VZgdHs_y7K_U7rA/viewform"

    def visit(self):
        self.driver.get(self.url)

    def login(self, username, password):
        user = WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="email"]'))
        )
        user.send_keys(username)
        time.sleep(5)
        user.send_keys(Keys.RETURN)
        time.sleep(5)
        passcode = WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]'))
        )
        passcode.send_keys(password)
        passcode.send_keys(Keys.RETURN)
        username = WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.freebirdFormviewerViewHeaderEmailAddress'))
        ).text
        return username

    def sign_in_button(self):
        self.driver.find_element_by_css_selector('.freebirdFormviewerViewMelbaSignInMsg').click()

    def sign_in_popup(self):
        self.driver.find_element_by_css_selector('#quantumwizdialogariabyid0').send_keys(Keys.ENTER)

    def click_next_button(self):
        buttons = WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '.quantumWizButtonPaperbuttonLabel.exportLabel'))
        )
        buttons[-1].click()
        time.sleep(2)

    def questions_headings(self):
        all_headings = WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '.freebirdFormviewerViewItemsItemItemTitle.freebirdCustomFont'))
        )
        return all_headings

    def error_with_empty(self, id):
        return self.driver.find_elements_by_css_selector('.freebirdFormviewerViewItemsItemItem')[
            id].find_element_by_css_selector('.freebirdFormviewerViewItemsItemErrorMessage').text

    def error_with_wrong_value(self, id):
        value = self.driver.find_elements_by_css_selector('.freebirdFormviewerViewItemsItemItem')[
            id].find_element_by_css_selector('.quantumWizTextinputPaperinputInputArea > input')
        value.send_keys('@')

    def enter_correct_values(self, **kwargs):
        value = self.driver.find_elements_by_css_selector('.freebirdFormviewerViewItemsTextTextItem')[
            kwargs.get('id')].find_element_by_css_selector('.quantumWizTextinputPaperinputInputArea > input')
        value.send_keys(Keys.BACKSPACE)
        value.send_keys(kwargs.get('values'))

    def status_of_page(self):
        return WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.freebirdFormviewerViewNavigationPercentComplete'))
        ).text

    """def firebug_selenium(self, **kwargs):
        self.driver.find_elements_by_css_selector('.freebirdFormviewerViewItemsItemItem')[
            kwargs.get('id')].find_element_by_css_selector('[data-value="Inspecting Elements"]').click()

    def type_of_locator(self, **kwargs):
        self.driver.find_elements_by_css_selector('.freebirdFormviewerViewItemsItemItem')[
            kwargs.get('id')].find_element_by_css_selector('[data-value="Password"]').click()"""

    def locator_and_firebug(self, **kwargs):
        """
        Page #2 all questions
        """
        self.driver.find_elements_by_css_selector('.freebirdFormviewerViewItemsItemItem')[
            kwargs.get('id')].find_element_by_css_selector('[data-value="{key_word}"]'.format(key_word=kwargs.get('values'))).click()

    def choose_answers(self, **kwargs):
        """
        question_id is index of (question)item divs
        """
        answers = self.driver.find_elements_by_css_selector('.freebirdFormviewerViewItemsItemItem')[
            kwargs.get('id')].find_elements_by_css_selector('.docssharedWizToggleLabeledLabelText')
        answers[2].click()
        answers[3].click()

    def capital_answers(self, **kwargs):
        self.driver.find_elements_by_css_selector('.freebirdFormviewerViewItemsItemItem')[
            kwargs.get('id')].find_element_by_css_selector('.quantumWizMenuPaperselectContent').click()
        try:
            self.driver.find_element_by_css_selector('.exportSelectPopup [data-value="Islamabad"]').click()
        except NoSuchElementException:
            self.driver.find_element_by_css_selector('.exportSelectPopup [data-value="Lahore"]').click()

    def upload_files(self, **kwargs):
        self.driver.find_elements_by_css_selector('.freebirdFormviewerViewItemsItemItem')[
            kwargs.get('id')].find_element_by_css_selector('.quantumWizButtonPaperbuttonLabel').click()
        time.sleep(5)
        if id == 0:
            frame = self.driver.find_element_by_css_selector('iframe.picker-frame')
            self.driver.switch_to.frame(frame)
        else:
            frame = self.driver.find_element_by_css_selector('.picker.modal-dialog.picker-dialog:nth-last-child(2) .picker-frame')
            time.sleep(5)
            self.driver.switch_to.frame(frame)
        self.driver.find_element_by_css_selector('#\:6 > div').click()
        time.sleep(4)
        self.driver.find_element_by_css_selector('div[aria-label="Files and folders list view."] > div').click()
        time.sleep(4)
        self.driver.find_element_by_css_selector('#picker\:ap\:2').click()
        time.sleep(4)
        self.driver.switch_to.default_content()

    def scale_numbr(self, **kwargs):
        self.driver.find_elements_by_css_selector('.freebirdFormviewerViewItemsItemItem')[
            kwargs.get('id')].find_elements_by_css_selector('.quantumWizTogglePaperradioOffRadio.exportOuterCircle')[2].click()

    def choice_grid(self, **kwargs):
        rows = self.driver.find_elements_by_css_selector('.freebirdFormviewerViewItemsItemItem')[
            kwargs.get('id')].find_elements_by_css_selector('.freebirdFormviewerViewItemsGridRowGroup')
        rows[0].find_elements_by_css_selector('label')[2].click()
        rows[1].find_elements_by_css_selector('label')[2].click()
        rows[2].find_elements_by_css_selector('label')[2].click()

    def enter_date(self, **kwargs):
        mon = self.driver.find_element_by_css_selector("input[aria-label='Month']")
        mon.send_keys(Keys.BACKSPACE)
        mon.send_keys(kwargs.get('values'))
        self.driver.find_element_by_css_selector("input[aria-label='Day of the month']").send_keys(kwargs.get('value1'))

    def enter_time(self, **kwargs):
        hr = self.driver.find_element_by_css_selector("input[aria-label='Hour']")
        hr.send_keys(Keys.BACKSPACE)
        hr.send_keys(kwargs.get('values'))
        mn = self.driver.find_element_by_css_selector("input[aria-label='Minute']")
        mn.send_keys(Keys.BACKSPACE)
        mn.send_keys(kwargs.get('value1'))

    def confirmation_message(self):
        return WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.freebirdFormviewerViewResponseConfirmationMessage'))
        ).text

    def view_score(self):
        self.driver.find_element_by_css_selector(".quantumWizButtonPaperbuttonLabel.exportLabel").click()
        time.sleep(2)
        window = self.driver.window_handles[-1]
        self.driver.switch_to.window(window)

    def total_score(self):
        return self.driver.find_element_by_css_selector(".freebirdFormviewerViewHeaderGradeFraction").text

    def grading_question_list(self, ind, count):
        txt = self.driver.find_elements_by_css_selector(".freebirdFormviewerViewItemList")[
            ind].find_elements_by_css_selector('.freebirdFormviewerViewItemsItemItem')[
            count].find_element_by_css_selector('.freebirdFormviewerViewItemsItemItemTitle').text
        return txt

    def correct_input(self, ind, count):
        return self.driver.find_elements_by_css_selector(".freebirdFormviewerViewItemList")[
            ind].find_elements_by_css_selector('.freebirdFormviewerViewItemsItemItem')[
            count].find_elements_by_css_selector('.freebirdFormviewerViewItemsItemGradingGradingBox .docssharedWizToggleLabeledPrimaryText > span')

    def edit_response(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.find_element_by_css_selector('.freebirdFormviewerViewResponseLinksContainer > a:nth-child(2)').click()
        time.sleep(2)

    def first_uncheck_all_options(self, ind):
        checked_options = self.driver.find_elements_by_css_selector('.freebirdFormviewerViewItemsItemItem')[
            ind].find_elements_by_css_selector('.isChecked[aria-checked="true"]')
        print 'length of checked' + str(len(checked_options))
        for option in checked_options:
            option.click()
            time.sleep(2)

    def correct_inputs(self, ind, values):
        self.driver.find_elements_by_css_selector('.freebirdFormviewerViewItemsItemItem')[
            ind].find_element_by_css_selector('.docssharedWizToggleLabeledControl[aria-label="{hard_cord}"]'.format
                                                       (hard_cord=values)).click()

    def multiple_inputs(self, values):
        self.driver.find_element_by_css_selector('.freebirdFormviewerViewItemList [aria-label="{hard_cord}"][aria-checked="false"]'.format
                                                 (hard_cord=values)).click()

    def view_submit_form(self):
        self.driver.find_element_by_css_selector(".quantumWizButtonPaperbuttonLabel.exportLabel").click()
        time.sleep(2)
        window = self.driver.window_handles[-2]
        self.driver.switch_to.window(window)












