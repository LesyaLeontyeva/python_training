from model.contact2 import Contact2
import pytest
import random
import string


def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact2(firstname="", lastname="", nickname="", title="", company="", address="",
                     home="", mobile="", work="", fax="", email="", email2="", email3="",
                     address2="", phone2="", notes="")] + [
                     Contact2(firstname=random_string("firstname",10),
                     lastname=random_string("lastname",10),
                     nickname=random_string("nickname",10), title=random_string("title",10),
                     company=random_string("company",10), address=random_string("address",10),
                     home=random_string("home",10),mobile=random_string("mobile",10),
                     work=random_string("work",10), fax=random_string("fax",10), email=random_string("email",10),
                     email2=random_string("email2",10), email3=random_string("email3",10),
                     address2=random_string("address2",10), phone2=random_string("phone2",10),
                     notes=random_string("notes",10))

            for i in range(5)
]


@pytest.mark.parametrize("contact2", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app,contact2):
        old_contacts = app.contact.get_contact_list()
        app.contact.create(contact2)
        assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts.append(contact2)
        assert sorted(old_contacts, key=Contact2.id_or_max) == sorted(new_contacts, key=Contact2.id_or_max)


