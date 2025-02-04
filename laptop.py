class Laptop:
    def __init__(self, brand, model, processor, ram, storage):
        self.brand = brand
        self.model = model
        self.processor = processor
        self.ram = ram
        self.storage = storage
        self.isOn = False
    def on(self)   :
        if not self.isOn:
            self.isOn=True 
            print(f"laptop  {self.brand} is turning on")
        else:
            print(f"laptop {self.brand} is already on ")   
    def off(self):
        if self.isOn:
            self.isOn=False
            print(f"laptop  {self.brand} shutting down")
        else:
            print(f"laptop  {self.brand} already off") 
            
              
my_laptop=Laptop("dell","2022","i3","8gb","256gb")
my_laptop.on()
my_laptop.off()

hp=Laptop("hp","2022","i5","6gb","156")
hp.on()
hp.off()



