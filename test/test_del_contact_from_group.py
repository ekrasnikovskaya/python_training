from model.contact import Contact
from model.group import Group
import random


def test_del_from_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(Contact(firstname="test_contact"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group = random.choice(db.get_group_list())
    if db.get_contact_list_from_group(group.id) == []:
        random_contact = random.choice(db.get_contact_list())
        app.contact.add_contact_to_group(random_contact.id, group.name)
    contact = random.choice(app.contact.get_contacts_in_group(group.name))
    app.contact.delete_contact_from_group(group.name, contact.id)
    assert int(group.id) not in db.get_groups_which_contact_belong(contact.id)

