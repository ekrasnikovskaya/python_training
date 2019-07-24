from model.contact import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="test_contact"))
    app.contact.delete_first()

