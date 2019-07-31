from model.contact import Contact
from random import randrange


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="NewName", lastname="NewLastName")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    assert (sorted(old_contacts, key=Contact.id_or_maxsize) == sorted(new_contacts, key=Contact.id_or_maxsize))
