# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new(Contact(firstname="John", lastname="Dorian", nickname="JD", company="SacredHeart", mobile="+12436587987", email="jd@sacredheart.com"))
    app.session.logout()

