from model.group import Group
from model.contact2 import Contact2


def test_group_list(app,db):
    ui_list = app.group.get_group_list()

    def clean(group):
        return Group(id=group.id,name=group.name.strip())
    db.list = map(clean,db.get_group.list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_contact_list(app,db):
    ui_list = app.contact2.get_contact_list()

    def clean(contact2):
        return Contact2(id=contact2.id, firstname=contact2.firstname.strip(),lastname=contact2.lastname.strip())
    db.list = map(clean,db.get_contact.list())
    assert sorted(ui_list, key=Contact2.id_or_max) == sorted(db_list, key=Contact2.id_or_max)
