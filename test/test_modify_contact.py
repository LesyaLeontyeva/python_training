from model.contact2 import Contact2


def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact2(firstname="test"))
    app.contact.modify_first_contact(Contact2(firstname="New name"))


def test_modify_first_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact2(lastname="test"))
    app.contact.modify_first_contact(Contact2(lastname="New lastname"))

