import csv
import re


with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

    new_contacts_list = []

    for raw_contact in contacts_list:
        new_contact = ''
        temp_contact = ''
        for string in raw_contact:
          temp_contact += string + ','

        result = re.match(r'[\w]*[ ,][\w]*[ ,][\w]*', temp_contact)
        if result != None:
            result = re.split(r'[ ,]', result.group(0))
        new_contact += result[0] + ',' + result[1] + ',' + result[2]

        result = re.split(r',', temp_contact)
        new_contact += ',' + result[3] + ',' + result[4] + ',' + result[5] + ',' + result[6]
        pattern = re.compile(r'(\+7|8){1}\s*\-?\(?(\d{3})\)?\s*\-?(\d{3})\s*\-?(\d{2})\s*\-?(\d{2})')
        new_contact = pattern.sub(r'+7(\2)\3-\4-\5', new_contact)
        pattern = re.compile(r'\s*\(?(доб.)\s*(\d+)\s*\)?')
        new_contact = pattern.sub(r'\1\2', new_contact)

        temp_list = new_contact.split(',')

        found = False
        for test_list in new_contacts_list:
            if temp_list[0] in test_list and temp_list[1] in test_list:
              found = True

        if not found:
          new_contacts_list.append(temp_list)

with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(new_contacts_list)