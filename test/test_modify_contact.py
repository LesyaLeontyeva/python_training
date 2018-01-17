from model.contact2 import Contact2


def test_modify_first_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact2(firstname="New name"))
    app.session.logout()


def test_modify_first_contact_lastname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact2(lastname="New lastname"))
    app.session.logout()
