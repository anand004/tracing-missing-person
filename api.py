import requests

def sendFoundSMS(caseId,name,mobile,location):
	url = "http://35.222.240.241:8080/missingPerson-0.0.1-SNAPSHOT/send-sms/"
	data = {"number":mobile,
		"caseId":caseId,
		"location":location,
		"name":name}
	r = requests.post(url = url, json = data)
	print(r.content)

def sendFoundMail(imagePath,caseId,name,email,location):
	url = "http://35.222.240.241:8080/missingPerson-0.0.1-SNAPSHOT/send-mail-attachment/"
	data = {
			"caseid":caseId,
			"email":email,
			"location":location,
			"name":name


	}
	files = {'file': open(imagePath,'rb')}

	r = requests.post(url = url, data = data ,files = files)
	print(r.content)

def sendCaseRegistrationEmail(caseId,name,emailId):
	url = "http://35.222.240.241:8080/missingPerson-0.0.1-SNAPSHOT/send-mail"
	data = {
			"caseId":caseId,
			"emailId":emailId,
			"name":name

	}
	r = requests.post(url = url , json = data)
	print(r.content)

#sendCaseRegistrationEmail("103","unknown","singh.anand004@gmail.com")

def sendCaseRegistrationMessage(caseId,name,phone):
	url = "http://35.222.240.241:8080/missingPerson-0.0.1-SNAPSHOT/send-registration-sms"
	data = {
			"caseId":caseId,
			"number":phone,
			"name":name

	}
	r = requests.post(url = url, json = data)
	print(r.content)

#sendCaseRegistrationMessage("103","Rajeev Kumar","7760496160")
