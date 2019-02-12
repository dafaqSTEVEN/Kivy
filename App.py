
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.config import Config

Config.set('graphics', 'height', '800')
Config.set('graphics', 'width', '700')


class App(App):
	def build(self):
		def login(self):
				if t1.text == '123' and t2.text == '123':
					t1.text = ''
					t2.text = ''
					l3.text =  'success'
					s.current='screen2'
					l3.text = 'await'
				else:
					l3.text = 'invalid'
		def back(self):
			s.current = 'screen1'
		s = ScreenManager()
		screen1 = Screen(name = 'screen1')
		screen2 = Screen(name = 'screen2')
		a = AnchorLayout(anchor_x = 'left',anchor_y = 'center')
		g = BoxLayout(size_hint=(None, None),orientation = 'vertical',padding = [0,10,50,10])
		b1 = BoxLayout(size_hint=(None, None))
		b2 = BoxLayout(size_hint=(None, None))
		b3 = BoxLayout(size_hint=(None, None))
		l1 = Label(text = 'Username:',font_size = 30,size_hint = (None,None),size = (200,100))
		t1 = TextInput(font_size = 30,size_hint = (None,None),size = (200,50))
		l2 = Label(text = 'Password:',font_size = 30,size_hint = (None,None),size = (200,100))
		t2 = TextInput(font_size = 30 ,size_hint = (None,None),size = (200,50))
		btn = Button(text = 'Login' ,size_hint = (None,None),size = (200,50),font_size = 30)
		l3 = Label(text = 'await' ,font_size = 30,size_hint = (None,None),size = (200,50))
		btn.bind(on_press = login)
		t4 = Label(text = 'Done' ,font_size = 30,size_hint = (None,None),size = (200,100))

		b4 = BoxLayout(size_hint=(None, None))
		btn2 = Button(text = 'Back',font_size = 30,size_hint = (None,None),size = (200,50))
		btn2.bind(on_press = back)
		s.add_widget(screen1)
		s.add_widget(screen2)
		screen2.add_widget(b4)
		b4.add_widget(t4)
		b4.add_widget(btn2)
		s.current = 'screen1'
		screen1.add_widget(a)
		a.add_widget(g)
		g.add_widget(b1)
		g.add_widget(b2)
		g.add_widget(b3)
		b1.add_widget(l1)
		b1.add_widget(t1)
		b2.add_widget(l2)
		b2.add_widget(t2)
		b3.add_widget(btn)
		b3.add_widget(l3)
		
		
		return s
		

if __name__ == '__main__':
	App().run()

