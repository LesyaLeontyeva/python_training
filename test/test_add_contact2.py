from model.contact2 import Contact2


def test_add_contact(app,db,json_contacts):
        contact2 = json_contacts
        old_contacts = db.get_contact_list()
        app.contact.create(contact2)
        new_contacts = db.get_contact_list()
        old_contacts.append(contact2)
        assert sorted(old_contacts, key=Contact2.id_or_max) == sorted(new_contacts, key=Contact2.id_or_max)


