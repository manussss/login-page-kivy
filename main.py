from kivymd.app import MDApp
from kivy import Config
from kivy.lang import Builder
Config.set('graphics', 'multisamples', '0')
Config.set('graphics', 'height', 500)
Config.set('graphics', 'width', 500)
Config.write()

class Login(MDApp):
    def build(self):
        self.screen = Builder.load_file('login.kv')
        return self.screen

    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)
        


def main():
    Login().run()


if __name__ == '__main__':
    main()