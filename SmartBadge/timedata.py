import ujson


class TimeData(object):

    def __init__(self, filename, subject, class):

        f = open(filename)
        timedata = ujson.load(f)

        try:
            self.title = timedata[subject]['class' + class]['title']
            self.time = timedata[subject]['class' + class]['time']
            self.location = timedata[subject]['class' + class]['location']
        except ValueError:
            from newtimetable import TimeTableApp
            mm = TimeTableApp(self.disp, self.buttons, self.tim)



    def get_time_data(self):

        return "{} \"{}\" {}".format(self.title, self.time, self.location)
