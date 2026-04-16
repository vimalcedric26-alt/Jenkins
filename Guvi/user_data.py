import openpyxl

class Excel:
    class Excel:
        def __init__(self, file_path, sheet_name):
            self.file_path = file_path
            self.sheet_name = sheet_name

    def get_data(self):
        workbook = openpyxl.load_workbook(self.fname)
        sheet = workbook.active

        data = []
        for row in sheet.iter_rows(min_row=2, values_only=True):
            data.append(row)

        return data