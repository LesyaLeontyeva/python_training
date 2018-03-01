from model.contact2 import Contact2
import random


def test_delete_some_contact(app,db,check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact2(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact2.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                      key=Contact2.id_or_max)

