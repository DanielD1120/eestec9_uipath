import re

finput = open("C:\\Users\\neabe\\Desktop\\UIPATH\\mail_content.txt", "r")

mailList = finput.read().split("Subject:")
finput.close()

mails = []
for mail in mailList:
	if mail != "" and mail.lower().find("conferinta") != -1:
		mails.append(mail)

foutput = open("C:\\Users\\neabe\\Desktop\\UIPATH\\output.txt", "w")
for mail in mails:
	content = mail.split("Body:")
	subject = content[0].rstrip().strip()
	body = content[1].rstrip().strip()

	subjectList = re.split(': |; |, | ', subject)
	city = subjectList[-2]
	country = subjectList[-1]

	periodRegex = '.*([0-9][0-9].[0-9][0-9].[1-9][0-9][0-9][0-9][ ]*-[ ]*[0-9][0-9].[0-9][0-9].[1-9][0-9][0-9][0-9]).*'
	period = re.search(periodRegex, body).group(1)

	dates = period.split("-")
	arrival = dates[0].strip().replace(".", "/")
	departure = dates[1].strip().replace(".", "/")
	
	dataRegex = '([0-9][0-9]).([0-9][0-9]).([1-9][0-9][0-9][0-9])'

	result = re.search(dataRegex, arrival)
	arrivalDay = result.group(1)
	arrivalMonth = result.group(2)
	arrivalYear = result.group(3)

	result = re.search(dataRegex, departure)
	departureDay = result.group(1)
	departureMonth = result.group(2)
	departureYear = result.group(3)

	if mails.index(mail) == len(mails) - 1:
		foutput.write(city + "\n")
		foutput.write(country + "\n")
		foutput.write(arrival + "\n")
		foutput.write(departure)
	else:
		foutput.write(city + "\n")
		foutput.write(country + "\n")
		foutput.write(arrival + "\n")
		foutput.write(departure + "\n")

foutput.close()