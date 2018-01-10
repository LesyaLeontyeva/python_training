# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.new_contact_add_page(wd, firstname="olesya", lastname="leontyeva", nickname="lesya")
        self.fill_information_about_company(wd, title="qwerty", company="onlc", address="Lenina str, 49", home="Ufa", mobile="89179043417", work="QA",
                                            fax="none", firstemail="email1@mail.ru", secondemail="email2@mail.ru", thirdemail="email3@mail.ru", byear="1992",
                                            address2="Kazan,Lenina str,49", phone2="Kazan", notes= "first test on Python")
        self.submit_contact_creation(wd)
        self.logout(wd)

    def test_add_contact_empty(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.new_contact_add_page(wd, firstname="", lastname="", nickname="")
        self.fill_information_about_company(wd, title="", company="", address="", home="", mobile="", work="",
                                            fax="", firstemail="", secondemail="", thirdemail="", byear="",
                                            address2="", phone2="", notes="")
        self.submit_contact_creation(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def submit_contact_creation(self, wd):
        # Submit  contact creation (Enter button)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_information_about_company(self, wd, title, company, address, home, mobile, work, fax, firstemail,
                                       secondemail, thirdemail, byear, address2, phone2, notes):
        # Fill information about company
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(firstemail)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(secondemail)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(thirdemail)
        wd.find_element_by_name("homepage").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[16]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[16]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[9]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[9]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(byear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(notes)

    def new_contact_add_page(self, wd, firstname, lastname, nickname):
        # Open new contact add page
        wd.find_element_by_link_text("add new").click()
        # fill information about firstname,lastname and nickname
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(nickname)

    def login(self, wd, username, password):
        # Login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
