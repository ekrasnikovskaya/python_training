

def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first("SampleName")
    app.session.logout()