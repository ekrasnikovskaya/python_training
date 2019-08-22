import re


def test_all_table_data(app, db):
    for index in range(len(app.contact.get_contact_list())):
        contact_from_home_page = app.contact.get_contact_list()[index]
        contact_from_db = db.get_contact_list()[index]
        assert contact_from_home_page.lastname == contact_from_db.lastname
        assert contact_from_home_page.firstname == contact_from_db.firstname
        assert contact_from_home_page.address == clear(contact_from_db.address)
        assert contact_from_home_page.all_emails_from_homepage == merge_emails_like_on_homepage(contact_from_db)
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)


def clear(s):
    return re.sub("[() -.]", "", s)


def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x !="", [contact.email, contact.email2, contact.email3]))


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))
