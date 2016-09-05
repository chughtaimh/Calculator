"""Contains the calculator class."""
from __future__ import division

import ttk
import Tkinter as Tk

from functools import partial


class Calculator(ttk.Frame):

	MATH = '+-*/^'
	NUMS = '1234567890.'
	PARENS = '()'
	ALL_CHARS = list(MATH+NUMS+PARENS+'=')+['AC']

	BUTTONS = [
		# Button, Row, Column
		('1', 1, 0),
		('2', 1, 1),
		('3', 1, 2),
		('+', 1, 3),
		('-', 1, 4),
		('4', 2, 0),
		('5', 2, 1),
		('6', 2, 2),
		('*', 2, 3),
		('/', 2, 4),
		('7', 3, 0),
		('8', 3, 1),
		('9', 3, 2),
		('.', 3, 3),
		('^', 3, 4),
		('(', 4, 0),
		('0', 4, 1),
		(')', 4, 2),
		('=', 4, 3),
		('AC', 4, 4),
	]

	def __init__(self, master=None):
		ttk.Frame.__init__(self, master)
		self.pack()

		self.master.title('Calculator')
		self.master.resizable(width=False, height=False)

		style = ttk.Style()
		style.configure('TButton',
						font=('Serif', 15),
						bg="#ccc",
						fg='blue',
						width=2,
						height=2,
						padding=20,
						)
		style.configure('TLabel',
						font=('Serif', 20),
						justify='right',
						height=2,
						padding=20,
						wraplength=200,
						)

		self.master.bind('<Key>', lambda event: self.key_press(event.char))
		self.master.bind('<Return>', lambda event: self.key_press('='))
		self.master.bind('<Delete>', lambda event: self.key_press('AC'))

		self.calc_value = Tk.StringVar()
		self.calc_value.set('')

		for button in Calculator.BUTTONS:
			b = ttk.Button(self,
						   text=button[0],
						   command=partial(self.button_click, text=button[0]))
			b.grid(row=button[1], column=button[2])

		label = ttk.Label(self, textvariable=self.calc_value).grid(
			row=0, columnspan=5)

	def key_press(self, key):
		if key in Calculator.ALL_CHARS:
			self.button_click(key)
		elif key == '\n':
			self.button_click('=')

	def button_click(self, text):
		current_value = self.calc_value.get()

		if text == 'AC':
			new_val = ''
		elif 'ERROR' in current_value:
			new_val = current_value
		elif (text in Calculator.NUMS) | (text in Calculator.PARENS):
			new_val = current_value + text
		elif text in Calculator.MATH:
			if current_value == '':
				if text == '-':
					new_val = text
				else:
					new_val = current_value
			elif current_value[-1] in Calculator.MATH:
				new_val = current_value[:-1] + text
			else:
				new_val = current_value + text
		elif text == '=':
			if (any(op in current_value for op in Calculator.MATH)):
				if (current_value[-1] not in Calculator.MATH):
					expression = self.strip_zeros(self.calc_value.get())
					expression = expression.replace('^', '**')
					try:
						new_val = eval(expression)
					except SyntaxError:
						new_val = 'ERROR: {}'.format(current_value)
				else:
					new_val = current_value
			else:
				new_val = current_value

		# new_val = new_val or ''
		self.calc_value.set(new_val)

	def __str__(self):
		return 'Class Calculator, subclass of Frame'

	def strip_zeros(self, text):
		new_text = ''
		for i, char in enumerate(text):
			try:
				last_char = text[i-1:i][0]
				if (last_char in Calculator.MATH) | (last_char in Calculator.PARENS):
					if char == '0':
						continue
			except IndexError:
				pass
			new_text = new_text + char
		return new_text.lstrip('0')

		return text.lstrip('0')


root = Calculator()
root.mainloop()
