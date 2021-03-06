import os
os.environ['KIVY_IMAGE'] = 'sdl2'
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.config import Config
from kivy.graphics import Color, Rectangle,Line
from kivy.core.image import Image 
from kivy.uix.image import Image
from kivy.garden.qrcode import QRCodeWidget
from time import strftime
Config.set('graphics', 'height', '1920')
Config.set('graphics', 'width', '1080')

dir_path = os.path.dirname(os.path.realpath(__file__))
exec(open(dir_path + '/user.py').read())

user_name = 'null'

class App(App):
	def build(self):
		def login(self):
				global user_name
				if t1.text in login_list and login_list[t1.text] == t2.text:
					user_name = t1.text
					print(user_name)
					t1.text = ''
					t2.text = ''
					l3.text =  'success'
					s.current='screen2'
					l3.text = 'await'
					l5 = Label(text='Welcome ' + user_name + '.\nThe time now is ' + strftime('%H%M'), pos=(20, 20),font_size=50)
					screen2.add_widget(l5)
				else:
					l3.text = 'invalid'
		def back(self):
			s.current = 'screen1'
		root = FloatLayout(size = (1080,1920))
		with root.canvas.before:
			Color(255, 255, 255, 0.7)
			self.rect = Rectangle(size = root.size)
		def generate(self):
			b5.add_widget(QRCodeWidget(data='Authenticated.' + user_name))

		s = ScreenManager()
		b5 = BoxLayout(size_hint =(0.2,0.2),pos = (400,400),orientation = 'vertical')
		l4 = Button(text = 'Generate ID QR code',size = (300,300))
		l4.bind(on_press = generate)
		screen1 = Screen(name = 'screen1')
		with screen1.canvas.before:
			Line(points=[100, 700, 400, 700], width=3)
			Line(points=[600, 700, 900, 700], width=3)
		screen2 = Screen(name = 'screen2')
		g = BoxLayout(pos =(190,800),size_hint=(700,700),orientation = 'vertical')
		logo = Label(font_name = 'FONT',markup = True,text = '[color=000000]ASSIST[/color]' ,size_hint = (None,None),size = (300,90),font_size = 200,pos = (350,1400))
		t1 = TextInput(hint_text = 'Username',font_size = 20,size_hint = (None,None),size = (600,50))
		space = Label(size_hint = (None,None),size = (400,50))
		t2 = TextInput(hint_text = 'Password',font_size = 20 ,size_hint = (None,None),size = (600,50),password = True)
		btn = Button(font_name = 'FONT',markup = True,text = '[color=FFFFFF]LOGIN[/color]' ,size_hint = (None,None),size = (100,30),font_size = 20,pos = (450,680))
		l3 = Label(text = 'await',font_size = 30,size_hint = (None,None),size = (200,50),markup = True,pos = (50,50))
		btn.bind(on_press = login)
		t4 = Label(text = 'SIGNED IN' ,font_size = 30,size_hint = (None,None),size = (200,100))
		b4 = BoxLayout(pos = (600,1800),size_hint=(None, None))
		btn2 = Button(text = 'Log Out',font_size = 30,size_hint = (None,None),size = (200,50))
		btn2.bind(on_press = back)

		root.add_widget(s)
		s.add_widget(screen1)
		s.add_widget(screen2)
		screen2.add_widget(b4)
		screen2.add_widget(b5)
		b5.add_widget(l4)
		b4.add_widget(t4)
		b4.add_widget(btn2)
		s.current = 'screen1'
		screen1.add_widget(g)
		screen1.add_widget(l3)
		screen1.add_widget(logo)
		screen1.add_widget(btn)
		g.add_widget(t1)
		g.add_widget(space)
		g.add_widget(t2)

		
		
		return root
		

if __name__ == '__main__':
	App().run()

