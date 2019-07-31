from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="NewName", lastname="NewLastName")
    contact.id = old_contacts[0].id
    app.contact.modify_first(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert (sorted(old_contacts, key=Contact.id_or_maxsize) == sorted(new_contacts, key=Contact.id_or_maxsize))
