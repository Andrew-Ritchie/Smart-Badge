import ujson


class TimeData(object):

    def __init__(self, filename, subject, slot):

        f = open(filename)
        timedata = ujson.load(f)
        self.title = timedata[subject]['class' + str(slot)]['title']
        self.time = timedata[subject]['class' + str(slot)]['time']
        self.location = timedata[subject]['class' + str(slot)]['location']



    def get_time_data(self):

        return "{} \"{}\" {}".format(self.title, self.time, self.location)
