from model.group import Group
from model.contact2 import Contact2
import random
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_adding_contact_to_group(app,db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="group"))
    if len(db.get_contact_list()) == 0:
        app.group.create(Contact2(firstname="contact_added"))
    groups = db.get_group_list()
    group = random.choice(groups)
    contacts = db.get_contact_list()
    contact_for_adding = random.choice(contacts)
    contacts_in_group_before_adding = db.get_contacts_in_group(Group(id=group.id))
    if contact_for_adding not in contacts_in_group_before_adding:
        app.contact.add_contact_to_group(contact_for_adding.id, group.id)
        contacts_in_group_after_adding = db.get_contacts_in_group(Group(id=group.id))
        assert len(contacts_in_group_before_adding) + 1 == len(contacts_in_group_after_adding)
        assert contact_for_adding in contacts_in_group_after_adding
    else:
        print("Contact is already in group")


def test_removing_contact_from_group(app,db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="group"))
    if len(db.get_contact_list()) == 0:
        app.group.create(Contact2(firstname="contact_added"))
        groups = db.get_group_list()
        group = random.choice(groups)
        contacts = db.get_contact_list()
        contact_for_removing = random.choice(contacts)
        contacts_in_group_before_removing = db.get_contacts_in_group(Group(id=group.id))
        if contact_for_removing in contacts_in_group_before_removing:
            app.contact.remove_contact_from_group(contact_for_removing.id, group.id)
            contacts_in_group_after_removing = db.get_contacts_in_group(Group(id=group.id))
            assert len(contacts_in_group_before_removing) == len(contacts_in_group_after_removing) + 1
            assert contact_for_removing not in contacts_in_group_after_removing
        else:
            print("Contact is already removing from group")



