# coding = utf-8
import csv


class CSVParser:
    def __init__(self, csv_path):
        self.csv_path = csv_path

    def get_dict_from_csv(self):
        data_dict = dict()
        with open(self.csv_path) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data_dict[row['Ref']] = row

        return data_dict


# csvObject = CSVParser("aa")
# dict = csvObject.get_dict_from_csv()
# print len(dict)


