#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__      = "Ricardo Ribeiro"
__credits__     = ["Ricardo Ribeiro"]
__license__     = "MIT"
__version__     = "0.0"
__maintainer__  = "Ricardo Ribeiro"
__email__       = "ricardojvr@gmail.com"
__status__      = "Development"


from __init__ import *
import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
sql = "SELECT title FROM albums WHERE title='Glow'"
cursor.execute(sql)
titleNames = cursor.fetchall()
titleName = titleNames[0]
finalName = titleName[0]


class SimpleExample2(BaseWidget):
	
	def __init__(self):
		super(SimpleExample2,self).__init__('Simple example 2')

		#Definition of the forms fields
		self._firstname 	= ControlText('First name', 'Default value')
		self._middlename 	= ControlText('Middle name')
		self._lastname 		= ControlText('Lastname name')
		self._fullname 		= ControlText('Full name')
		self._button		= ControlButton('Press this button')
		self._checkbox      = ControlCheckBox('Check Here')

		#Define the organization of the forms
		self.formset = ['_firstname','_middlename','_lastname', '_fullname', '_button','_checkbox',' ']
		#The ' ' is used to indicate that a empty space should be placed at the bottom of the window
		#If you remove the ' ' the forms will occupy the entire window

		#Define the button action
		self._button.value = self.__buttonAction

	def __buttonAction(self):
		"""Button action event"""

		self._fullname.value = self._firstname.value +" "+ self._middlename.value + \
				" "+ self._lastname.value

		if self._checkbox.value:
			self._fullname.value = finalName
		





##################################################################################################################
##################################################################################################################
##################################################################################################################

#Execute the application
if __name__ == "__main__":	 pyforms.start_app( SimpleExample2 )
	