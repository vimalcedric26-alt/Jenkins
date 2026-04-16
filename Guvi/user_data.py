import openpyxl
import os

class Excel:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.fname = os.path.join(base_dir, "testdata", "Excel.xlsx")

    def get_data(self):
        workbook = openpyxl.load_workbook(self.fname)
        sheet = workbook.active

        data = []
        for row in sheet.iter_rows(min_row=2, values_only=True):
            data.append(row)

        return data