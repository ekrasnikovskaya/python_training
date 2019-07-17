def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first("SampleText")
    app.session.logout()