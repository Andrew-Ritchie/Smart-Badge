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


class HighScores(object):

    def __init__(self, filename, game):

        f = open(filename)
        settings = ujson.load(f)

        self.first = settings[game][0]
        self.second = settings[game][1]
        self.third = settings[game][2]

    def get_top_three(self):
        return "{} {} {}".format(self.first, self.second, self.third)
