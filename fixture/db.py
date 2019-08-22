import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, work, mobile, email, "
                           "email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, work, mobile, email, email2, email3) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname,
                                    address=address, homephone=home, workphone=work, mobilephone=mobile,
                                    email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

    def get_groups_which_contact_belong(self, contact_id):
        groups_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id from address_in_groups where id='%s'" % contact_id)
            for group_id in cursor:
                groups_list.append(group_id[0])
        finally:
            cursor.close()
        return groups_list

    def get_contact_list_from_group(self, group_id):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id from address_in_groups where group_id='%s'" % group_id)
            for el in cursor:
                contact_list.append(group_id[0])
        finally:
            cursor.close()
        return contact_list


    def destroy(self):
        self.connection.close()
