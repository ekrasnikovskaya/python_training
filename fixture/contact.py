from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new(self, contact):
        # add new contact
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.open_home_page()
        self.contact_cache = None

    def delete_first(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.implicitly_wait(3)
        wd.find_element_by_css_selector("div.msgbox")
        self.app.open_home_page()
        self.contact_cache = None

    def modify_first(self, new_data):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("(.//img[@alt='Edit'])").click()
        self.fill_contact_form(new_data)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("company", contact.company)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("email", contact.email)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            # self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                text = element.text
                newtext = text.split(' ')
                firstname = newtext[1]
                lastname = newtext[0]
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)







