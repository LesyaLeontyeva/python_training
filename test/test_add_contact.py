# -*- coding: utf-8 -*-
from model.contact import Contact
from model.company import Company
from fixture.application_for_contacts import ApplicationForContacts
import pytest

@pytest.fixture
def app(request):
    fixture = ApplicationForContacts()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.new_contact_add_page(Contact(firstname="olesya", lastname="leontyeva", nickname="lesya"))
    app.fill_information_about_company(Company(title="qwerty", company="onlc", address="Lenina str, 49", home="Ufa", mobile="89179043417", work="QA",
                                            fax="none", firstemail="email1@mail.ru", secondemail="email2@mail.ru", thirdemail="email3@mail.ru", byear="1992",
                                            address2="Kazan,Lenina str,49", phone2="Kazan", notes= "first test on Python"))
    app.logout()


def test_add_contact_empty(app):
    app.login(username="admin", password="secret")
    app.new_contact_add_page(Contact(firstname="", lastname="", nickname=""))
    app.fill_information_about_company(Company(title="", company="", address="", home="", mobile="", work="",
                                            fax="", firstemail="", secondemail="", thirdemail="", byear="",
                                            address2="", phone2="", notes=""))
    app.logout()


