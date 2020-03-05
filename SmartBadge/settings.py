import ujson

class Settings(object):

    def __init__(self, filename):

        f = open(filename)
        settings = ujson.load(f)

        self.firstname = settings['user']['firstname']
        self.lastname = settings['user']['lastname']
        self.nickname = settings['user']['nickname']
        self.email = settings['user']['email']
        self.ssid = settings['connectivity']['ssid']
        self.ssid = settings['connectivity']['password']

    def get_str_name_and_nickname(self):
        return "{} \"{}\" {}".format(self.firstname, self.nickname, self.lastname)
    
    def get_str_name(self):
        return "{} {}".format(self.firstname, self.lastname)

