from kivy.uix.button import Button
from database_work import get_data
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivymd.uix.list import MDList, ThreeLineListItem
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder


from kivy.core.window import Window
Window.size = (1280, 720)


custom_float_button = """
MDFloatingActionButtonSpeedDial:
    data: app.data
    rotation_root_button: True
    root_button_anim: True
    icon: 'settings-outline'
    callback: app.callback
"""

custom_text_input = """
BoxLayout:
    padding: 20
    size_hint_y: None
    MDTextField:
        multiline: False
        pos_hint: {'center_x': .5, 'center_y': .5}
        hint_text: "Введите цвет"
        mode: "rectangle"
"""


custom_flat_button = """
BoxLayout:
    padding: 20
    size_hint_y: None
    size_hint_x: 0.1
    MDRectangleFlatButton:
        text: "Поиск"
        font_size: 16
        pos_hint: {'center_x': .5, 'center_y': .45}
        size: 1, 45
"""



class MyApp(MDApp):
    
    data = {
        'plus': 'Добавить',
        'cloud': 'Изменить',
        'trash-can-outline': 'Удалить',
    }
    
    
    def callback(self, instance):
        if instance.icon == 'plus':
            print('хуй')
        elif instance.icon == 'cloud':
            print('анал')
        elif instance.icon == 'trash-can-outline':
            content = Button(text='Close me!')
            popup = Popup(content=content, auto_dismiss=False)
            content.bind(on_press=popup.dismiss)
            popup.open()

    
    def on_focus(instance, value):
        if value:
            print('User focused', instance)
        else:
            print('User defocused', instance)


    

    def build(self):

        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.theme_style = 'Dark'
        
        screen = MDScreen()
        layout = GridLayout(cols=1)
        row = BoxLayout(size_hint_y=None)
        row_items = GridLayout(cols=2)
        row_items.add_widget(Builder.load_string(custom_text_input))
        row_items.add_widget(Builder.load_string(custom_flat_button))
        row.add_widget(row_items)
        layout.add_widget(row)
        
        
        scroll = ScrollView()
        list_view = MDList()
        scroll.add_widget(list_view)
        
        db_data = get_data()
        
        for i in range(len(db_data)):
            list_view.add_widget(ThreeLineListItem(text=f"{db_data[i][3]} {db_data[i][1]}", 
                                            secondary_text=f"Цена: {str(db_data[i][2])}, {db_data[i][-2]}", 
                                            tertiary_text=f"Цвет: {db_data[i][-1]}",
                                            ))
        
        layout.add_widget(scroll)
        screen.add_widget(layout)
        screen.add_widget(Builder.load_string(custom_float_button))
        
        return screen


if __name__ == '__main__':
    MyApp().run()
