from model.contact2 import Contact2


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact2(firstname="test"))
    app.contact.delete_first_contact()

