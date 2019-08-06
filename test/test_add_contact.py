# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import string
import random


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email():
    good_symbols = string.ascii_letters + string.digits + "-"*10 + "."*5
    name = "".join([random.choice(good_symbols) for k in range(random.randrange(10))])
    mailserver = "".join([random.choice(good_symbols) for k in range(random.randrange(7))])
    domain = "".join([random.choice(string.ascii_letters) for k in range(random.randrange(5))])
    return name+"@"+mailserver+"."+domain


testdata = [Contact(firstname="", lastname="", address="", email="", homephone="")] + [
    Contact(firstname=random_string("name", 10), lastname=random_string("lname", 10), address=random_string("ad", 10),
            email=random_email(), homephone=random_string("phone", 8))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new(contact)
    assert (len(old_contacts) + 1) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert (sorted(old_contacts, key=Contact.id_or_maxsize) == sorted(new_contacts, key=Contact.id_or_maxsize))

