from segno import helpers


class ContactGenerator():

    def __init__(self, displayname, email, phone):
        qr = helpers.make_vcard(
            name=displayname, displayname=displayname, email=email, phone=phone)
        qr.save("../SmartBadge/vcard.png", scale=1)


vcard = ContactGenerator("Joseph Bloggs", "joey99@example.com", "123456")
