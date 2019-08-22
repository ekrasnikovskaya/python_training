from model.contact import Contact
from model.group import Group
import random


def test_add_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(Contact(firstname="test_contact"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    contact = random.choice(db.get_contact_list())
    group = random.choice(db.get_group_list())
    app.contact.add_contact_to_group(contact.id, group.name)
    assert int(group.id) in db.get_groups_which_contact_belong(contact.id)




