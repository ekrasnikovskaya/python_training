# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new_contact(Contact(firstname="John", lastname="Dorian", nickname="JD", company="SacredHeart", mobile="+12436587987", email="jd@sacredheart.com"))
    app.session.logout()


