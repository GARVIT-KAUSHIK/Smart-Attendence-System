from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Dashboard(BoxLayout):
    # img=Image()
    pass


class AttendanceApp(App):
    def build(self):
        return Dashboard()


AttendanceApp().run()
