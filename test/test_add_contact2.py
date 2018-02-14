# -*- coding: utf-8 -*-
from model.contact2 import Contact2


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact2 = Contact2(firstname="olesya", lastname="leontyeva", nickname="lesya", title="qwerty",
                                    company="onlc", address="Lenina str, 49", home="Kazan",
                                    mobile="89179043417", work="QA", fax="none", email="email1@mail.ru",
                                    email2="email2@mail.ru", email3="email3@mail.ru",
                                    address2="Kazan,Lenina str,49", phone2="Kazan", notes="first test on Python",)
    app.contact.create(contact2)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact2)
    assert sorted(old_contacts, key=Contact2.id_or_max) == sorted(new_contacts, key=Contact2.id_or_max)


#def test_add__empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    contact2 = Contact2(firstname="", lastname="", nickname="", title="", company="", address="",
#                                    home="", mobile="", work="", fax="", email="", email2="", email3="",
#                                    address2="", phone2="", notes="")
#    app.contact.create(contact2)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    old_contacts.append(contact2)
#    assert sorted(old_contacts, key=Contact2.id_or_max) == sorted(new_contacts, key=Contact2.id_or_max)



