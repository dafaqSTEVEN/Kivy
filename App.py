import kivy


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


def login(self):
	if t1.text == '123' and t2.text == '123':
		t1.text = ''
		t2.text = ''
		l3.text =  'success'
	else:
		l3.text = 'invalid'

class App(App):
	def build(self):
		def login(self):
				if t1.text == '123' and t2.text == '123':
					t1.text = ''
					t2.text = ''
					l3.text =  'success'
				else:
					l3.text = 'invalid'
		g = GridLayout(cols = 2 , rows = 3 )
		l1 = Label(text = 'Username:',size_hint_y = None ,height = 60)
		t1 = TextInput(font_size = 20,size_hint_y = None ,height = 60)
		l2 = Label(text = 'Password:',size_hint_y = None ,font_size = 20,height = 60)
		t2 = TextInput(font_size = 20,size_hint_y = None ,height = 60)
		btn = Button(text = 'Login',size_hint_y = None ,height = 40)
		l3 = Label(text = 'await',size_hint_y = None ,font_size = 20,height = 40)
		btn.bind(on_press = login)
		g.add_widget(l1)
		g.add_widget(t1)
		g.add_widget(l2)
		g.add_widget(t2)
		g.add_widget(btn)
		g.add_widget(l3)
		
		
		return g
		

if __name__ == '__main__':
	App().run()

