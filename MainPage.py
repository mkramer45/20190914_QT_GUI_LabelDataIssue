import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
import bs4
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen as uReq



class MainPage(QDialog):
	def __init__(self):
		super(MainPage, self).__init__()
		loadUi('GUI.ui', self)
		#run the retrievetext function 
		self.retrieveText

	def retrieveText(self):
		#list of URLs to scrape from
		my_url = ['https://www.ndbc.noaa.gov/station_page.php?station=44013']

		for url in my_url:
		#initiating python's ability to parse URL
			uClient = uReq(url)
		# this will offload our content in'to a variable
			page_html = uClient.read()
		# closes our client
			uClient.close()
			page_soup = BeautifulSoup(page_html, "html.parser")	
		# Fetching/Defining data to variables
			wave_height = page_soup.find('td', string='Wave Height (WVHT):').find_next_sibling().get_text().strip()
			# words = self.wave_height
		# Attaching the wave height value to the 'label' variable in the UI file
			self.label.setText(wave_height)

app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec_())


