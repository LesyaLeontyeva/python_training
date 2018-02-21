from model.contact2 import Contact2
from random import randrange


def test_modify_some_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact2(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    cont = Contact2(firstname="firstname", id=old_contacts[index].id)
    app.contact.modify_contact_by_index(cont,index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = cont
    assert sorted(old_contacts, key=Contact2.id_or_max) == sorted(new_contacts, key=Contact2.id_or_max)


#def test_modify_first_contact_lastname(app):
#    old_contacts = app.contact.get_contact_list()
#    if app.contact.count() == 0:
#        app.contact.create(Contact2(lastname="test"))
#    app.contact.modify_first_contact(Contact2(lastname="New lastname"))
#   new_contacts = app.contact.get_contact_list()
#   assert len(old_contacts) == len(new_contacts)

