# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact2 import Contact2



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.create(Contact2(firstname="olesya", lastname="leontyeva", nickname="lesya", title="qwerty",
                                  company="onlc", address="Lenina str, 49", home="Kazan",
                                  mobile="89179043417", work="QA", fax="none", email="email1@mail.ru",
                                  email2="email2@mail.ru", email3="email3@mail.ru", byear="1992",
                                  address2="Kazan,Lenina str,49", phone2="Kazan", notes="first test on Python"))
        app.session.logout()


def test_add__empty_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.create(Contact2(firstname="", lastname="", nickname="", title="", company="", address="",
                                   home="", mobile="", work="", fax="", email="", email2="", email3="", byear="", address2="",
                                   phone2="", notes=""))
        app.session.logout()


