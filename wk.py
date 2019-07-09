from helper import *
import wikipedia

class find_info():

	def __init__(self,data):
		self.data = data
	def find_wiki(self):

		try:
			wikipedia.set_lang('vi')
			datarep = wikipedia.summary(self.data, sentences = 2)
			datarep = sent(datarep)
			return datarep
		except:
			datarep = 'Tìm không ra rồi anh ơi'
			return datarep
