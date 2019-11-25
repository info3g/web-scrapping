from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import xlsxwriter
import time

class DataScrap():


	def getData(self):
		AgentName = []
		JobTitle = []
		CompanyName = []
		Email = []
		Contact = []
		# Direct_phone = []
		# Office_phone = []
		# Office_fax = []
		# Second_phone = []
		# Cell_phone = []
		# Home_phone = []
		url = 'https://www.century21.ca/search/directory/'
		driver = webdriver.Chrome('C:/Users/as/Desktop/tristan/chromedriver')
		driver.get(url)
		for page in range(1,167):
			time.sleep(10)
			page_data = driver.page_source
			soup = BeautifulSoup(page_data,'lxml')
			data_list = soup.findAll('div',attrs = {'class':'list-item list-item-agent'})
			# print("data list: ",len(data_list))
			for single in data_list:
				try:
					agent_name = single.find('a',attrs = {'class':'agent-name'})
					print(agent_name.text)
					AgentName.append(agent_name.text)
				except:
					AgentName.append('not found')
				try:
					job_title  = single.find('span',attrs ={'class':'job-title'})
					print(job_title.text)
					JobTitle.append(job_title.text)
				except:
					JobTitle.append('not found')
				try:
					company_name = single.find('span',attrs ={'class':'company-name'})
					print(company_name.text)
					CompanyName.append(company_name.text)
				except:
					CompanyName.append('not found')
				try:
					email = single.find('a',attrs={'class':'agent-email'})
					print(email['href'][7:])
					Email.append(email['href'][7:])
				except:
					Email.append('not found')
				try:
					all_contact = single.find('li',attrs={'class':'agent-phone-number'})
					print(all_contact.text)
					contact_text = all_contact.text
					seprate = contact_text.split()
					Contact.append(seprate[1])

				except:
					Contact.append('')
			
			
			try:
				pages = driver.find_element_by_class_name('next-link')
				pages.click()
			except:
				break
			
		
		# for x in range(0,166):
		# 	try:
		# 		driver.find_element_by_class_name('next-link').click()
		# 		soup = BeautifulSoup(driver.page_source,'html')
		# 		t = soup.find('title')
		# 		print(title)
		# 		title.append(t)
		# 		# data_list = soup.findAll('div',attrs = {'class':'list-item list-item-agent'})
		# 		# for y in data_list:
		# 		# 	print("next: ",data_list)
		# 	except:
		# 		break

		# self.getData()
			# for x in all_contact:
			# 	span = x.find('span')
			# 	# print(span.text)
				
			# 	# try:
			# 	if span.text == ' Direct':
			# 		print(x.text[7:])
			# 		Direct_phone.append(x.text[7:])
			# 		break
			# 	else:
			# 		Direct_phone.append('not found')
			# 		break
			# 	# except:
			# 		# Direct_phone.append('not found')
				
			# 	# try:
			# 	if span.text == ' Phone 2':
			# 		print(x.text[7:])
			# 		Second_phone.append(x.text[7:])
			# 		break
			# 	else:
			# 		Second_phone.append('not found')
			# 		break
			# 	# except:
			# 	# 	Second_phone.append('not found')
				
			# 	# try:
			# 	if span.text == ' Office':
			# 		print(x.text[7:])
			# 		Office_phone.append(x.text[7:])
			# 	else:
			# 		Office_phone.append('not found')
				# except:
				# 	Office_phone.append('not found')
				
				# try:
				# 	if span.text == ' Office Fax':
				# 		print(x.text[11:])
				# 		Office_fax.append(x.text[11:])
				# except:
				# 	Office_fax.append('not found')
				# try:
				# 	if span.text == ' Cell':
				# 		print(x.text[5:])
				# 		Cell_phone.append(x.text[5:])
				# except:
				# 	Cell_phone.append('not found')

				
				# try:
				# 	if span.text == ' Home':
				# 		print(x.text[5:])
				# 		Home_phone.append(x.text[5:])
				# except:
				# 	Home_phone.append('not found')
			# print(Direct_phone)	
			# data.append({'AgentName':agent_name.text,'JobTitle':job_title.text,'CompanyName':company_name.text,'Email':email.text})
			# print(data)
			# return data
		# print(Second_phone)
		# print(Direct_phone)
		# print(Second_phone)
		# print(len(Direct_phone))
		# print(len(Office_phone))
		# print(Office_phone)
		# print(Contact)
		# print(len(Contact))
		workbook = xlsxwriter.Workbook("test_century20.xlsx")
		worksheet = workbook.add_worksheet()
		bold = workbook.add_format({'bold': True})
		worksheet.write(0,0,'Name',bold)
		worksheet.write(0,1,'Job Title',bold)
		worksheet.write(0,2,'Company Name',bold)
		worksheet.write(0,3,'Email ',bold)
		worksheet.write(0,4,'Contact No',bold)
		# worksheet.write(0,5,'Secondry Phone',bold)
		# worksheet.write(0,4,'Office',bold)
		# worksheet.write(0,5,'Office Fax',bold)
		# worksheet.write(0,8,'Cell Phone',bold)
		# worksheet.write(0,9,'Home Phone',bold)
		for i in range(1,len(AgentName)+1):
			worksheet.write(i,0,AgentName[i-1])
			worksheet.write(i,1,JobTitle[i-1])
			worksheet.write(i,2,CompanyName[i-1])
			worksheet.write(i,3,Email[i-1])
			worksheet.write(i,4,Contact[i-1])
			# worksheet.write(i,5,Second_phone[i-1])
			# worksheet.write(i,4,Office_phone[i-1])
			# worksheet.write(i,5,Office_fax[i-1])
			# worksheet.write(i,8,Cell_phone[i-1])
			# worksheet.write(i,9,Home_phone[i-1])
		workbook.close()




if __name__ == '__main__':
	obj = DataScrap()
	obj.getData()
