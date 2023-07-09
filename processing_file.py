
#Wires functions (for new module)
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
