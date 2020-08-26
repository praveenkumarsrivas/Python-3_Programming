class Car():
    def __init__(self, name, model, year, mileage):
        self.name = str(name)
        self.model = str(model)
        self.year = str(year)
        self.mileage = str(mileage)
        self.meter_read = str('0')

    def car_details(self):
        result1 = self.name + " " + self.model + " " + self.year + " " + self.mileage + " " + self.meter_read
        return (result1)


c = Car('audi', 'A4', '2018', '20')
print(c.car_details())

