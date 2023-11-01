import csv
import re
from pprint import pprint


fio_pattern = re.compile(r'^(?P<lastname>[А-Яа-яЁё]+)\s*(?P<firstname>[А-Яа-яЁё]+)?\s*(?P<surname>[А-Яа-яЁё]+)?$')

# Читаем адресную книгу в формате CSV в список contacts_list:
with open("phonebook_raw.csv", encoding="UTF-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def split_name(fio_pattern):
    corrected_data = []

    for record in contacts_list:
        if len(record) >= 3:
            match = fio_pattern.match(record[0])
            if match:
                lastname = match.group('lastname')
                firstname = match.group('firstname')
                surname = match.group('surname')
            else:
                lastname = record[0]
                firstname = ''
                surname = ''

            corrected_record = [lastname, firstname, surname] + record[1:]
            corrected_data.append(corrected_record)




    # with open("phonebook_corrected.csv", mode='w', encoding='UTF-8', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerows(corrected_data)

# pprint(split_name(fio_pattern))
pprint(contacts_list)