import json
from segno import helpers


class ContactGenerator():

    def __init__(self, displayname, nickname, email, phone):
        qr = helpers.make_vcard(
            name=displayname, displayname=displayname, nickname=nickname, email=email, phone=phone)
        qr.save("../SmartBadge/vcard.png", scale=1)


class Setup:
    def __init__(self):
        self.settings_data = None

    def set_settings(self, **kwargs):
        user = {}
        user['firstname'] = kwargs.get('firstname', None)
        user['lastname'] = kwargs.get('lastname', None)
        user['nickname'] = kwargs.get('nickname', None)
        user['email'] = kwargs.get('email', None)
        user['phone'] = kwargs.get('phone', None)
        conn = {}
        conn['ssid'] = kwargs.get('ssid', None)
        conn['password'] = kwargs.get('password', None)
        self.settings_data = {'user': user, 'connectivity': conn}

    def write_json_to(self, filename):
        with open('../SmartBadge/' + filename, 'w') as f:
            json.dump(self.settings_data, f)

    def __str__(self):
        return str(self.settings_data)


if __name__ == '__main__':
    s = Setup()
    fn = input('First name of user> ') or None
    ln = input('Last name of user> ') or None
    nn = input('Nickname for user> ') or None
    email = input('Email address for user (optional)> ') or None
    phone = input('Phone no. for user (optional)> ') or None
    s.set_settings(firstname=fn, lastname=ln, nickname=nn,
                   email=email)
    s.write_json_to('settings.json')

    ContactGenerator("{} {}".format(fn, ln), nn, email, phone)
