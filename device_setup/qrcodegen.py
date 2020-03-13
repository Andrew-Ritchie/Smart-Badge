import pyqrcode
from segno import helpers


class URLGenerator():

    def __init__(self, url, filename):
        url = pyqrcode.create(url)
        url.svg(filename, scale=8)


class ContactGenerator():

    def __init__(self, name, displayname, email, phone):
        qr = helpers.make_vcard(
            name=name, displayname=displayname, email=email, phone=phone)
        qr.save("{}.png".format(name), scale=2)


github = URLGenerator(
    "https://github.com/Andrew-Ritchie/Smart-Badge", "SmartBadgeGithub.svg")

ashwin = ContactGenerator("Ashwin;Jaison;Maliampurakal",
                          "Ashwin Maliampurakal", "2249314m@student.gla.ac.uk", "123456")
