import os


class Setup:
    def __init__(self):
        self.name_sheet = 'Ficha Técnica'
        self.name_sheet_atl = 'Ficha Técnica ATL'
        self.letCode = "A"
        self.letQtd = "B"
        self.letOp = "C"
        self.aux_column = "D"
        self.directory_name = 'processingFolder'
        self.files=os.listdir(f'{ self.directory_name }')

