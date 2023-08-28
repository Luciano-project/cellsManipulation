# Description: This is the main file of the project, here is where the magic happens
import re
from openpyxl import load_workbook
from setup import Setup
from components import Component

class Main(Setup):
    def __init__(self):
        super().__init__()
        self.wb_file = None
        self.start_values = 1
        self.final_values = 0
        self.aux_waste_wires = []
        self.data = {}

    def clear_waste_list(self):
        self.aux_waste_wires.clear()

    # Process all files inside the folder
    def processing_wb(self):
        for book in self.files:
            wb = load_workbook(filename=f'{self.directory_name}/{book}')
            self.wb_file = book
            wb_sheet = wb[self.name_sheet]
            self.find_extrem_values(wb_sheet)
            self.processing_sheet(wb_sheet)

    # Find where the values start and end
    def find_extrem_values(self, wb):
        i = 1
        while True:
            term = f"{wb[f'{self.letOp}{+i}'].value}"
            if (self.search_values(f'#N/D', term) or self.search_values(f'#N/A', term)) and i > 7:
                break
            i += 1
        self.start_values += i
        self.final_values = self.start_values

    # Process the waste of the wires
    def processing_cells(self, wb):
        while (wb[f'{self.letCode}{+self.final_values}'].value) != None:
            if self.search_values(f'_D', wb[f'{self.letCode}{+self.final_values}'].value):
                self.processing_waste(wb)
            else:
                self.instance_components(wb, self.final_values)
            self.final_values += 1
        self.temporary_print_function()

    def processing_waste(self, wb):
        for i in range(self.final_values,self.start_values,-1):
            if self.search_values(str(wb[f'{self.letCode}{+i}'].value), str(wb[f'{self.letCode}{+self.final_values}'].value.split("_")[0])):
                component_name = str(wb[f'{self.letCode}{+i}'].value)
                component_quantity = wb[f'{self.letQtd}{+self.final_values}'].value
                self.data[component_name].setter_quantity_wasted(component_quantity)
                #print(self.data[component_name].get_component(),self.data[component_name].get_quantity())
                break

    #Instance the components
    def instance_components(self, wb, i):
        instance = Component(str(wb[f'{self.letCode}{+i}'].value), wb[f'{self.letQtd}{+i}'].value, wb[f'{self.letOp}{+i}'].value)
        self.data[instance.get_component()] = instance

    # This is a management function for the others functions
    def processing_sheet(self, wb):
        i = self.start_values + 1
        self.processing_cells(wb)

#AUXILIAR FUNCTIONS
##############################################################################################################
    # Check if the values are in the string (with regex)
    @staticmethod
    def search_values(to_search, on_search):
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
        #print(self.aux_waste_wires)
        
        self.clear_waste_list()
        print("\n\n")
        for item in self.data:
            print(f'\tkey:{item} value:{self.data[item].get_quantity()} Operation:{self.data[item].get_operation()}, Waste:{self.data[item].get_waste_percent()}')
        

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