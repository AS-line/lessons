from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader

class ButtonGrid(GridLayout):
	def do_click(self, number):
		soundname = 'Sounds/audio' + number + '.mp3'
		sound = SoundLoader.load(soundname)
		sound.play()


class MyApp(App):
	def build(self):
		return ButtonGrid()

if __name__ == '__main__':
	MyApp().run()