from model.contact2 import Contact2


def test_modify_first_contact_firstname(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact2(firstname="test"))
    app.contact.modify_first_contact(Contact2(firstname="New name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_first_contact_lastname(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact2(lastname="test"))
    app.contact.modify_first_contact(Contact2(lastname="New lastname"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

