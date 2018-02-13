from model.contact2 import Contact2


def test_modify_first_contact_firstname(app):
    old_contacts = app.contact.get_contact_list()
    contact2 = Contact2(firstname="test")
    contact2.id = old_contacts[0].id
#    if app.contact.count() == 0:
#        app.contact.create(contact2)
    app.contact.modify_first_contact(contact2)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact2
    assert sorted(old_contacts, key=Contact2.id_or_max) == sorted(new_contacts, key=Contact2.id_or_max)


#def test_modify_first_contact_lastname(app):
#    old_contacts = app.contact.get_contact_list()
#    if app.contact.count() == 0:
#        app.contact.create(Contact2(lastname="test"))
#    app.contact.modify_first_contact(Contact2(lastname="New lastname"))
#   new_contacts = app.contact.get_contact_list()
#   assert len(old_contacts) == len(new_contacts)

