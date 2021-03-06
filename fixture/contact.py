from model.contact2 import Contact2
import re


class ContactHelper:

    def __init__(self,app):
        self.app = app

    def create(self, contact2):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact2)
        self.submit_contact()
        self.return_to_home_page()
        self.contact_cache = None

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
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self,index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_element_by_css_selector('input[value="Delete"]').click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id(self,id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        wd.find_element_by_css_selector('input[value="Delete"]').click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value=%s]" % id).click()

#    def modify_first_contact(self):
#        self.modify_contact_by_index(0)

#    def modify_contact_by_index(self, index, new_contact_data):
#        wd = self.app.wd
#        self.open_home_page()
#        self.select_contact_by_index(index)
#        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
#        self.fill_contact_form(new_contact_data)
#        wd.find_element_by_name("update").click()
#        self.open_home_page()
#        self.contact_cache = None

    def modify_contact_by_index(self, index,new_contact_data):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/addressbook/')):
            wd.find_element_by_link_text("home page").click()

    def submit_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            wd.find_element_by_link_text("home").click()
            self.contact_cache = []
            rows = wd.find_elements_by_name("entry")
            print(rows)
            for element in rows:
                cells = element.find_elements_by_tag_name("td")
                lastname_text = cells[1].text
                firstname_text = cells[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                address = cells[3].text
                self.contact_cache.append(Contact2(firstname=firstname_text,lastname=lastname_text, id=id,
                                                   all_phones_from_home_page=all_phones,
                                                   all_emails_from_home_page=all_emails, address=address))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self,index):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self,index):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self,index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact2(firstname=firstname, lastname=lastname,id=id,
                        home=home,mobile=mobile,work=work,phone2=phone2,address=address,email=email,
                        email2=email2,email3=email3)

    def get_contact_from_view_page(self,index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)",text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("F: (.*)", text).group(1)
        return Contact2(home=home, mobile=mobile, work=work, phone2=phone2)


















