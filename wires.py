import os
import re
from openpyxl import load_workbook

class Main:
    def __init__(self) -> None:
        self.files=os.listdir('processingFolder')
        self.letCode = "A"
        self.letQtd = "B"
        self.letOp = "C"
        self.aux_column = "D"
        self.start_values = 1
        self.final_values = 0
        self.aux_waste_wires = []

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
                self.aux_waste_wires.append({wb[f'{self.letCode}{+self.final_values}'].value: f"{self.final_values}"})
            self.final_values += 1
        self.temporary_print_function()

    # This is a management function for the others functions
    def processing_sheet(self, wb):
        i = self.start_values + 1
        self.processing_waste(wb, i)

#Wires functions
    # Calculate the waste percent of wires
    def waste_percent(self, waste, index):
        return waste*100/(self.index)
        #wb[f'{self.aux_column}{+i}'].value = wb[f'{self.letQtd}{+i}'].value*100/wb[f'{}']

    def waste_code_search(self, wb, i):
        for index in range(self.start_values, self.final_values):
            for item in self.aux_waste_wires:
                for i in item:
                    if self.search_values(f'{wb[f"{self.letCode}{+i}"].value}', f'{self.aux_waste_wires[index]}'):
                        break
        wb.save(f'processingFolder/{wb.filename}')
#########
#Generic functions
    def column_search(self, wb):
        pass
        """for index in range(self.start_values, self.final_values):
            if self.search_values(f'{wb[f"{self.letCode}{+i}"].value}', f'{self.aux_waste_wires[index]}'):
                return True"""

#AUXILIAR FUNCTIONS
##############################################################################################################
    # Check if the values are in the string (with regex)
    def search_values(self, to_search, on_search):
        if re.search(f'{to_search}', f"{on_search}"):
            return True
        return False

 ###################################Temporary function to print the waste list
    def temporary_print_function(self):
        """for item in self.aux_waste_wires:
            print(f'\tkey:{item.keys()} value:{item.values()}')"""
        for item in self.aux_waste_wires:
            for i in item:
                print(f'\tkey:{i} value:{item[i]}')
        print(self.aux_waste_wires)
        
        self.clear_waste_list()
        print("\n\n")



def test():
    pessoas = {"nome": "João", "idade": 23, "cidade": "São Paulo"}
    print (pessoas.keys())
    pessoas.clear()
    print (pessoas.keys())
if __name__ == "__main__":
    """test()
    """
    main = Main()
    main.processing_wb()