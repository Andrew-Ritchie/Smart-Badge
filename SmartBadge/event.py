import lvgl as lv
from lib.screen.widgets import *
from timedata import TimeData
from lib.app import App
from main_menu import MainMenuApp


class EventApp(App):

    def __init__(self, disp, buttons, tim, subject, slot):
        super().__init__(name="Name", display=disp, buttons=buttons, timer=tim,
                         btn_left=self.btn_left,
                         btn_right=self.btn_right,
                         )

        self.subject = subject 
        self.slot = slot
        cont = self.get_cont()
        cont.set_center()

        title, time, location = self.get_data()

        self.title_widget = Label(cont.lv_obj, title, font_size=28)
        self.time_widget = Label(cont.lv_obj, time)
        self.location_widget = Label(cont.lv_obj, location)

        self.add_item("Title", self.title_widget)
        self.add_item("Time", self.time_widget)
        self.add_item("Location", self.location_widget)

        #self.add_item("Back", Button(cont.lv_obj, text="Back",
                                          #width=cont.half(), app=EventApp), selectable=True)

        #self.add_item("Forward", Button(cont.lv_obj, text="forward",
                                          #width=cont.half(), app=EventApp), selectable=True)

        self.load_screen()


    def btn_left(self, x):
        self.slot -=1
        try:
            time_data = TimeData("timedata.json", self.subject, self.slot)
            title, time, location = time_data.get_time_data().split(" ")
            self.title_widget.update_text(title)
            self.time_widget.update_text(time)
            self.location_widget.update_text(location)
        except:
            from newtimetable import TimeTableApp
            mm = TimeTableApp(self.disp, self.buttons, self.tim)
 

    def btn_right(self, x):
        self.slot +=1
        try:
            time_data = TimeData("timedata.json", self.subject, self.slot)
            title, time, location = time_data.get_time_data().split(" ")
            self.title_widget.update_text(title)
            self.time_widget.update_text(time)
            self.location_widget.update_text(location)
        except:
            from newtimetable import TimeTableApp
            mm = TimeTableApp(self.disp, self.buttons, self.tim)
 

    def get_data(self):
        self.slot +=1
        time_data = TimeData("timedata.json", self.subject, self.slot)
        return time_data.get_time_data().split(" ")
