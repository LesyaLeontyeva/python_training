class ContactHelper:

    def __init__(self,app):
        self.app = app

    def create(self, contact2):
        wd = self.app.wd
        # add new contact
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact2)
        self.submit_contact()

    def fill_contact_form(self, contact2):
        wd = self.app.wd
        self.change_field_value("firstname", contact2.firstname)
        self.change_field_value("lastname", contact2.lastname)
        self.change_field_value("nickname", contact2.nickname)
        self.change_field_value("title", contact2.title)
        self.change_field_value("company", contact2.company)
        self.change_field_value("address", contact2.address)
        self.change_field_value("home", contact2.home)
        self.change_field_value("mobile", contact2.mobile)
        self.change_field_value("work", contact2.work)
        self.change_field_value("fax", contact2.fax)
        self.change_field_value("email", contact2.email)
        self.change_field_value("email2", contact2.email2)
        self.change_field_value("email3", contact2.email3)
        self.change_field_value("address2", contact2.address2)
        self.change_field_value("phone2", contact2.phone2)
        self.change_field_value("notes", contact2.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        # Click on modification icon
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[7]/a/img").click()
        # Click on modify button
        wd.find_element_by_name("modifiy").click()
        # fill new data in form
        self.fill_contact_form(new_contact_data)
        # Submit modification. Click on 'update' button
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def submit_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))







