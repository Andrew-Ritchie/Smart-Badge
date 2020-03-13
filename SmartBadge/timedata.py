import ujson


class TimeData(object):

    def __init__(self, filename, subject):

        f = open(filename)
        settings = ujson.load(f)

        self.title = settings[subject]['title']
        self.time = settings[subject]['time']
        self.location = settings[subject]['location']


    def get_time_data(self):
        
        return "{} \"{}\" {}".format(self.title, self.time, self.location)
