import sys
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.lang import Builder

# Builder.load_string("""
#
# <Test>:
#     do_default_tab: False
#     TabbedPanelItem:
#         text: 'first tab'
#         Label:
#             text: 'First tab content area'
#     TabbedPanelItem:
#         text: 'tab2'
#         BoxLayout:
#             Label:
#                 text: 'Second tab content area'
#             Button:
#                 text: 'Button that does nothing'
#     TabbedPanelItem:
#         text: 'tab3'
#         RstDocument:
#             text:
#                 '\\n'.join(("Hello world", "-----------",
#                 "You are in the third tab."))
#
# """)


# class Test(TabbedPanel):
#     pass


class TabbedPanelApp(App):
    # def build(self):
    #     return Test()
    tp = TabbedPanel()
    th = TabbedPanelHeader(text='To-Do List')
    tp.add_widget(th)


if __name__ == '__main__':
    TabbedPanelApp().run()

# class Ui(App):
#     def build(self):
#         self.window = GridLayout()
#         self.window.cols = 1
#         #add widgets to window
#
#
#         #image widget
#         self.window.add_widget(Image(source="alienpic.png"))
#         self.greeting = Label(text="What's your name?")
#         self.window.add_widget(self.greeting)
#         #text input widget
#         self.user = TextInput(multiline=False)
#         self.window.add_widget(self.user)
#         #button widget
#         self.button = Button(text="GREET")
#         self.window.add_widget(self.button)
#         self.button.bind(on_press=self.callback)
#
#         return self.window
#
#     def callback(self, instance):
#         self.greeting.text = "hello " + self.user.text + "!"

# if __name__ == "__main__":
#     Ui().run()