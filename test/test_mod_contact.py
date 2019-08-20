from model.contact import Contact
from random import randrange


def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="NewName", lastname="NewLastName")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_maxsize) == sorted(app.contact.get_contact_list(), key=Contact.id_or_maxsize)
