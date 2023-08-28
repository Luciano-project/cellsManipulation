

class Component:
    def __init__(self, component, quantity, operation, quantity_waste = 0):
        self._component = str(component)
        self._quantity = quantity
        self._operation = operation
        self._waste_quantity = quantity_waste
        self._waste_percent = 0

    def __repr__(self):
        return self._component
    
    def __str__(self):
        return self._component

    def calculate_wire_waste(self):
        if self._waste_quantity > 0:
            self._waste_percent = self._waste_quantity * 100 / self._quantity

    def get_component(self): return self._component
    def get_quantity(self): return self._quantity
    def get_operation(self): return self._operation
    def get_waste_quantity(self): return self._waste_quantity
    def get_waste_percent(self): return self._waste_percent
    
    #
    def setter_quantity(self, quantity):
        self._quantity = quantity
        self.calculate_wire_waste()
    
    def setter_quantity_wasted(self, quantity):
        self._waste_quantity = quantity
        self.calculate_wire_waste()

comp = Component(141414, 10, 1)
comp2 = Component(14, 10, 1, 2)
comp3 = Component(1414, 10, 1, 2)
ab = {comp.get_component():comp, comp2.get_component():comp2, comp3.get_component():comp3}
if __name__ == "__main__":
    print(ab["13"])
#verify if a component is in a dictionary
# if "1414" in ab:
#     print("1414" in ab)
#     print(ab["1414"])
