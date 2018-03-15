class UserHelper:

    def __init__(self, app):
        self.app = app


    def open_webpage(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()
        if not (wd.current_url.endswith("/") and len(wd.find_elements_by_name("searchform")) > 0):
        wd.get("http://localhost/addressbook/")



    def open_user_creation(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_link_text("add new").click()


    def create(self, users):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        self.open_user_creation()
        wd.find_element_by_name("firstname").send_keys(users.firs_name)
        wd.find_element_by_name("middlename").send_keys(users.middle_name)
        wd.find_element_by_name("lastname").send_keys(users.last_name)
        wd.find_element_by_name("nickname").send_keys(users.nick_name)
        wd.find_element_by_name("title").send_keys(users.title)
        wd.find_element_by_name("company").send_keys(users.companyname)
        wd.find_element_by_name("address").send_keys(users.address)
        wd.find_element_by_name("home").send_keys(users.home)
        wd.find_element_by_name("mobile").send_keys(users.mobile)
        wd.find_element_by_name("work").send_keys(users.work)
        wd.find_element_by_name("fax").send_keys(users.fax)
        wd.find_element_by_name("email").send_keys(users.email)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


    def delete_first_user(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()


    def return_to_users_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()


    def edit_first_user(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        wd.find_element_by_name("firstname").send_keys("1")
        wd.find_element_by_name("middlename").send_keys("2")
        wd.find_element_by_name("lastname").send_keys("3")
        wd.find_element_by_name("nickname").send_keys("4")
        wd.find_element_by_name("title").send_keys("5")
        wd.find_element_by_name("company").send_keys("6")
        wd.find_element_by_name("address").send_keys("7")
        wd.find_element_by_name("home").send_keys("8")
        wd.find_element_by_name("mobile").send_keys("9")
        wd.find_element_by_name("work").send_keys("10")
        wd.find_element_by_name("fax").send_keys("11")
        wd.find_element_by_name("email").send_keys("12")
        wd.find_element_by_name("update").click()


    def count(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        return len(wd.find_elements_by_name("selected[]"))