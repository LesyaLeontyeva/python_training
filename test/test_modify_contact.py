from model.contact2 import Contact2


def test_modify_first_contact_firstname(app):
    app.contact.modify_first_contact(Contact2(firstname="New name"))


def test_modify_first_contact_lastname(app):
    app.contact.modify_first_contact(Contact2(lastname="New lastname"))

