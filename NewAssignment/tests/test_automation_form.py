import unittest
from selenium import webdriver
import os
from NewAssignment.pages import page_automation_form
from selenium.common.exceptions import NoSuchElementException
import csv

dict = {
        'CNIC': {'correct_input': 'enter_correct_values', 'wrong_pattern_error': 'Must match pattern',
                 'empty_error': 'This is a required question', 'func_to_call_for_wrong_char': 'error_with_wrong_value',
                 'func_to_call_for_empty_field': 'error_with_empty',
                 'value_as_an_arg': '3333333333333'},
        'Phone_Number': {'correct_input': 'enter_correct_values', 'wrong_pattern_error': 'Must match pattern',
                         'func_to_call_for_wrong_char': 'error_with_wrong_value',
                         'empty_error': 'This is a required question',
                         'func_to_call_for_empty_field': 'error_with_empty', 'value_as_an_arg': '33333333333'},
        'Name': {'correct_input': 'enter_correct_values', 'empty_error': 'This is a required question',
                 'func_to_call_for_empty_field': 'error_with_empty',
                 'value_as_an_arg': 'Atika'},
        'Email': {'correct_input': 'enter_correct_values', 'wrong_pattern_error': 'Must be a valid email address',
                  'empty_error': 'This is a required question', 'func_to_call_for_wrong_char': 'error_with_wrong_value',
                  'func_to_call_for_empty_field': 'error_with_empty', 'value_as_an_arg': 'a@a.com'},
        'Select_the_name_which_is_NOT_a_type_of_the_locater': {'func_to_call_for_empty_field': 'error_with_empty',
                                                               'empty_error': 'This is a required question',
                                                               'correct_input': 'locator_and_firebug',
                                                               'value_as_an_arg': 'ID'},
        'Use_of_Firebug_in_Selenium': {'func_to_call_for_empty_field': 'error_with_empty',
                                       'empty_error': 'This is a required question',
                                       'correct_input': 'locator_and_firebug',
                                       'value_as_an_arg': 'Programming'},
        'Select_the_correct_answers': {'func_to_call_for_empty_field': 'error_with_empty',
                                       'empty_error': 'This is a required question',
                                       'correct_input': 'choose_answers'},
        'Select_the_two_numbers_that_are_not_prime.': {'func_to_call_for_empty_field': 'error_with_empty',
                                                       'empty_error': 'This is a required question',
                                                       'correct_input': 'choose_answers'},
        'Capital_of_Pakistan': {'func_to_call_for_empty_field': 'error_with_empty',
                                'empty_error': 'This is a required question',
                                'correct_input': 'capital_answers'},
        'Capital_of_Punjab': {'func_to_call_for_empty_field': 'error_with_empty',
                              'empty_error': 'This is a required question',
                              'correct_input': 'capital_answers'},
        'Upload_pdf_file': {'func_to_call_for_empty_field': 'error_with_empty',
                            'empty_error': 'This is a required question',
                            'correct_input': 'upload_files'},
        'Upload_Image_File': {'func_to_call_for_empty_field': 'error_with_empty',
                              'empty_error': 'This is a required question',
                              'correct_input': 'upload_files'},
        'On_a_scale_of_1_to_five_how_hard_this_assignment_is': {'func_to_call_for_empty_field': 'error_with_empty',
                                                                'empty_error': 'This is a required question',
                                                                'correct_input': 'scale_numbr'},
        'How_satisfied_are_you_with_the_following': {'func_to_call_for_empty_field': 'error_with_empty',
                                                     'empty_error': 'This question requires one response per row',
                                                     'correct_input': 'choice_grid'},
        'Select_your_proficiency_in_following': {'func_to_call_for_empty_field': 'error_with_empty',
                                                 'empty_error': 'This question requires at least one response per row',
                                                 'correct_input': 'choice_grid'},
        'Enter_Current_time': {'func_to_call_for_empty_field': 'error_with_empty',
                               'empty_error': 'This is a required question',
                               'correct_input': 'enter_time', 'value_as_an_arg': '05', 'value_as_an_arg1': '45',
                               'func_to_call_for_wrong_char': 'error_with_wrong_value',
                               'wrong_pattern_error': 'Invalid time'},
        'Enter_Current_date': {'func_to_call_for_empty_field': 'error_with_empty',
                               'empty_error': 'This is a required question',
                               'correct_input': 'enter_date', 'value_as_an_arg': '03', 'value_as_an_arg1': '25',
                               'func_to_call_for_wrong_char': 'error_with_wrong_value',
                               'wrong_pattern_error': 'Invalid date'}
        }


class TestGoogleForm(unittest.TestCase):
    driver = webdriver.Firefox()
    google_page = page_automation_form.GoogleFormSubmission(driver)

    def setUp(self):
        self.google_page.visit()

    @classmethod
    def setUpClass(cls):
        """
        Authenticate google by login
        """
        query1 = os.environ.get("username")
        query2 = os.environ.get("password")
        try:
            cls.google_page.sign_in_button()

        except NoSuchElementException:
            cls.google_page.visit()
            cls.driver.implicitly_wait(10)
            cls.google_page.sign_in_popup()
        cls.google_page.login(query1, query2)

    def test01_execution_for_pages(self):
        for count in range(9):
            all_headings = self.google_page.questions_headings()
            count = count + 1
            number = "Page " + str(count) + " of 9"
            status = self.google_page.status_of_page()
            print status
            self.assertEqual(status, number)
            for ind, heading in enumerate(all_headings):
                heading = heading.text.replace(' *', '')
                key = heading.replace(' ', '_')
                key = key.replace('?', '')
                self.google_page.click_next_button()
                required_error = getattr(self.google_page, dict.get(key).get('func_to_call_for_empty_field'))(ind)
                self.assertEqual(required_error, dict.get(key).get('empty_error'))
                if dict.get(key). has_key('func_to_call_for_wrong_char'):
                    getattr(self.google_page, dict.get(key).get('func_to_call_for_wrong_char'))(ind)
                call1 = getattr(self.google_page, dict.get(key).get('correct_input'))
                call1(id=ind, values=dict.get(key).get('value_as_an_arg'), value1=dict.get(key).get('value_as_an_arg1'))
            self.google_page.click_next_button()
        confirm_mes = self.google_page.confirmation_message()
        self.assertEqual(confirm_mes, 'Your response has been recorded.')
        """
        View submitted form's score
        """
        self.google_page.view_score()
        """
        Note down how many scores get
        """
        total_score_get = self.google_page.total_score()
        total_score_get.split()
        print "Got " + total_score_get[0] + total_score_get[1] + " points out of 40"
        my_file = open("output.csv", "w")
        for number in range(1, 4):
            for nmb in range(2):
                title = self.google_page.grading_question_list(number, nmb)
                answr_list = self.google_page.correct_input(number, nmb)
                if len(answr_list) != 0:
                    my_file.write('Q: ' + str(title) + "\n")
                    for item in answr_list:
                        my_file.write(str(item.text) + "\n")
        self.google_page.edit_response()
        self.google_page.click_next_button()

        my_file = 'output.csv'
        with open(my_file, 'r') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                print 'ROW' + str(row)
                if row[0].startswith('Q:'):
                    question = row[0].replace('Q: ', '')
                    print 'Question' + str(question)
                    question_found = False
                    for number in range(2):
                        all_headings = self.google_page.questions_headings()
                        for ind, title in enumerate(all_headings):
                            print 'ind' + str(ind)
                            if title.text == question:
                                next_answer = next(csv_reader)
                                print 'next_answer' + next_answer[0]
                                self.google_page.first_uncheck_all_options(ind)
                                self.google_page.correct_inputs(ind, next_answer[0])
                                question_found = True
                                break
                        if question_found:
                            break
                        else:
                            self.google_page.click_next_button()
                else:
                    self.google_page.multiple_inputs(row[0])
        """
        Click next to until you reach last page to resubmit form
        """
        [self.google_page.click_next_button() for _ in range(7)]
        self.google_page.view_submit_form()
        if self.google_page.total_score() == "40/40":
            print "Finally you did it"

    def tearDown(self):
            """
            Verify page has closed
            """
            self.driver.close()
            self.driver.quit()


if __name__ == "__main__":
        unittest.main()
