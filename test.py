from selenium import webdriver
import time
from bs4 import BeautifulSoup
import csv

def readData():
	url = 'https://www.century21.ca/search/directory/'
	driver = webdriver.Chrome('C:/Users/as/Desktop/tristan/chromedriver')
	driver.maximize_window()
	driver.get(url)
	pages = driver.find_element_by_class_name('next-link')
	data = []
	for page in range(1,6):
		time.sleep(10)
		page_data = driver.page_source
		soup = BeautifulSoup(page_data, 'lxml')
		all_agents = soup.findAll('div', attrs = {'class':'list-item list-item-agent'})
		for agent_info in all_agents:
			agent_info = agent_info.findAll('ul')
			details = agent_info[0]
			try:
				name = details.find('a', attrs = {'class':'agent-name'})
				name = name.text
			except:
				pass
			
			try:
				job_title = details.find('span', attrs = {'class':'job-title'})
				job_title = job_title.text
			except:
				pass
			try:
				company = details.find('span', attrs = {'class':'company-name'})
				company = company.text
			except:
				pass
			try:
				email = details.find('a', attrs = {'class':'agent-email'})
				email = email['href'].replace('mailto:','')
			except:
				pass
			website = ''
			try:
				website = details.find('a', attrs = {'class':'agent-website'})
				website = str(website['href'])
				if website[0] == '/':
					website = 'http://www.century21.ca' + website
				else:
					website = website
			except:
				pass
			try:
				phones = agent_info[1].findAll('li',attrs = {'class':'agent-phone-number'})
				office_no = ''
				cell_no = ''
				office_fax = ''
				home_no = ''
				if len(phones) == 1:
					cell_no = str(phones[0].text)
				elif len(phones) == 2:
					office_no = str(phones[1].text)
					cell_no = str(phones[0].text)
				elif len(phones) == 3:
					office_no = str(phones[1].text)
					cell_no = str(phones[0].text)
					office_fax = str(phones[2].text) 
				elif len(phones) == 4:
					office_no = str(phones[1].text)
					cell_no = str(phones[0].text)
					office_fax = str(phones[2].text)
					home_no = str(phones[3].text)
				else:
					print("No phones")
			except:
				pass
			data.append({
					'name':str(name),
					'job_title':str(job_title),
					'email':str(email),
					'company':str(company),
					'website':str(website),
					'office_no':str(office_no),
					'cell_no':str(cell_no),
					'office_fax':str(office_fax),
					'home_no':str(home_no),
				}) 

		pages = driver.find_element_by_class_name('next-link').click()
	print(data)
	return data
def writeData():
	with open('data.csv', 'w', newline='') as writeFile:
		writer = csv.writer(writeFile)
		data = readData()
		for data_write in data:
			# row = [data_write['name'],data_write['job_title'],data_write['company'],data_write['email'],
			# 	data_write['website'],data_write['office_no'],data_write['cell_no'],data_write['office_fax'],
			# 	data_write['home_no']]
			writer.writerows(data_write['name'],data_write['job_title'])
		print("!!!!!Successfully written!!!!!")

	

if __name__ =='__main__':
	writeData()