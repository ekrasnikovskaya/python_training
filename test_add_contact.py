# -*- coding: utf-8 -*-
import pytest
from application_for_contacts import AppFC
from contact import Contact


@pytest.fixture
def app(request):
    fixture = AppFC()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.add_new_contact(Contact(firstname="John", lastname="Dorian", nickname="JD", company="SacredHeart", mobile="+12436587987", email="jd@sacredheart.com"))
    app.logout()


