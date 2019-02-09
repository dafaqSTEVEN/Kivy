
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '600')

class App(App):
	def build(self):
		def login(self):
				if t1.text == '123' and t2.text == '123':
					t1.text = ''
					t2.text = ''
					l3.text =  'success'
					s.current='screen2'
				else:
					l3.text = 'invalid'
		def back(self):
			s.current = 'screen1'
		s = ScreenManager()
		screen1 = Screen(name = 'screen1')
		screen2 = Screen(name = 'screen2')
		g = FloatLayout(size_hint=(None, None),size =(900,600))
		l1 = Label(text = 'Username:',pos_hint={None:None},pos=(0,400),font_size = 30,size_hint = (None,None),size = (200,100))
		t1 = TextInput(font_size = 30,pos_hint={None:None},pos=(250,400),size_hint = (None,None),size = (200,100))
		l2 = Label(text = 'Password:',pos_hint={None:None},pos=(0,300),font_size = 30,size_hint = (None,None),size = (200,100))
		t2 = TextInput(font_size = 30 ,pos_hint={None:None},pos=(250,300),size_hint = (None,None),size = (200,100))
		btn = Button(text = 'Login' ,pos_hint={None:None},pos=(0,0),size_hint = (None,None),size = (200,100),font_size = 30)
		l3 = Label(text = 'await' ,pos=(200,0),pos_hint={None:None},font_size = 30,size_hint = (None,None),size = (200,100))
		btn.bind(on_press = login)
		t4 = Label(text = 'Done' ,pos_hint={None:None},pos=(0,0),font_size = 30,size_hint = (None,None),size = (200,100))
		btn2 = Button(text = 'Back',pos=(200,200),pos_hint={None:None},font_size = 30,size_hint = (None,None),size = (200,100))
		btn2.bind(on_press = back)
		s.add_widget(screen1)
		s.add_widget(screen2)
		screen2.add_widget(t4)
		screen2.add_widget(btn2)
		s.current = 'screen1'
		screen1.add_widget(g)
		g.add_widget(l1)
		g.add_widget(t1)
		g.add_widget(l2)
		g.add_widget(t2)
		g.add_widget(btn)
		g.add_widget(l3)
		
		
		return s
		

if __name__ == '__main__':
	App().run()

