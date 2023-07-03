import os
import re
from openpyxl import load_workbook

class Main:
    def __init__(self) -> None:
        self.files=os.listdir('processingFolder')
        self.letCode = "A"
        self.letQtd = "B"
        self.letOp = "C"
        self.waste = "D"
        self.start_values = 1
        self.final_values = 0
        self.wast_wires = []

    # Process all files inside the folder
    def processing_wb(self):
        for book in self.files:
            wb = load_workbook(filename=f'processingFolder/{book}')
            wb_sheet = wb['Ficha Técnica']
            self.find_extrem_values(wb_sheet)
            self.processing_sheet(wb_sheet)

    # Find where the values start and end
    def find_extrem_values(self, wb):
        for i in range(1, 1000):
            term = f"{wb[f'{self.letOp}{+i}'].value}"
            if self.search_values(f'#N/D', term) or self.search_values(f'#N/A', term):
                break
            i += 1
        self.start_values = i

    # Process the waste of the wires
    def processing_waste(self, wb, i):
        self.final_values += i
        while (wb[f'{self.letCode}{+self.final_values}'].value) != None:
            if self.search_values(f'_D', wb[f'{self.letCode}{+self.final_values}'].value):
                self.wast_wires.append({wb[f'{self.letCode}{+self.final_values}'].value: f"{self.final_values}"})
            self.final_values += 1
        self.temporary_print_function()

    # This is a management function for the others functions
    def processing_sheet(self, wb):
        i = self.start_values + 1
        self.processing_waste(wb, i)

    def waste_percent(self, wb, i): pass
        #wb[f'{self.waste}{+i}'].value = wb[f'{self.letQtd}{+i}'].value*100/wb[f'{}']

    # Check if the values are in the string (with regex)
    def search_values(self, to_search, on_search):
        if re.search(f'{to_search}', f"{on_search}"):
            return True
        return False

    def temporary_print_function(self):
        for item in self.wast_wires:
            print(f'\tkey:{item.keys()} value:{item.values()}')
if __name__ == "__main__":
    main = Main()
    main.processing_wb()