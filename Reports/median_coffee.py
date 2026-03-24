import csv
from collections import defaultdict
from tabulate import tabulate
from statistics import median


class MedianCoffee:

    def __init__(self, files):
        self.files = files
        self.user_spent = defaultdict(list)
        self.report_data = []
        self.headers = ["student", "median_spent"]

    def start(self):
        for file in self.files:
            self.file_processing(file)
        self.median()
        self.send_report()

    def file_processing(self, file):
        with open(file, "r", newline="", encoding="UTF=8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.user_spent[row["student"]].append(int(row["coffee_spent"]))

    def median(self):
        for user_name, spent in self.user_spent.items():
            self.report_data.append([user_name, int(median(spent))])

    def send_report(self):
        print(tabulate(self.report_data, headers=self.headers, tablefmt="grid"))
