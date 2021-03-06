import re
from random import randrange
from model.contact2 import Contact2


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def test_information_from_db(app, db, data_contacts):
    if app.contact.count() == 0:
        app.contact.add_contact(data_contacts)
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()
    contact_from_home_page.sort(key=Contact2.id_or_max)
    contact_from_db.sort(key=Contact2.id_or_max)
    assert len(contact_from_home_page) == len(contact_from_db)
    for i in range(len(contact_from_home_page)):
        assert contact_from_home_page[i].parametr['all_phone_from_home_page'] == merge_phones_like_on_home_page(
            contact_from_db[i])
        assert contact_from_home_page[i].parametr['all_emails_from_home_page'] == merge_emails_like_on_home_page(
            contact_from_db[i])
        assert contact_from_home_page[i].parametr['lastname'] == contact_from_db[i].parametr['lastname']
        assert contact_from_home_page[i].parametr['firstname'] == contact_from_db[i].parametr['firstname']
        assert contact_from_home_page[i].parametr['address'] == contact_from_db[i].parametr['address']


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                [contact.home,contact.work,contact.mobile,contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))






