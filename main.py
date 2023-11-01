from pprint import pprint
import csv
import re


def extract_name(full_name):
    last_name, first_name, surname = '', '', ''

    name_parts = re.match(r'(.+?)\s(.+?)\s(.+)', full_name)
    if name_parts:
        last_name, first_name, surname = name_parts.groups()
    else:
        name_parts = full_name.split()
        if len(name_parts) == 3:
            last_name, first_name, surname = name_parts
        elif len(name_parts) == 2:
            last_name = name_parts[0]
            name_and_surname = name_parts[1]
            name_parts = name_and_surname.split(" ", 1)
            if len(name_parts) == 2:
                first_name, surname = name_parts
            else:
                first_name = name_and_surname
                surname = ''


    return last_name, first_name, surname


with open("phonebook_raw.csv", encoding="UTF-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

contacts_list[0][:3] = ['last_name', 'first_name', 'surname']

for row in contacts_list[1:]:
    last_name, first_name, surname = extract_name(row[0])
    row[:3] = [last_name, first_name, surname]


pprint(contacts_list)