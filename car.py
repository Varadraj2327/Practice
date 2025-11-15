class Car:
    def __init__(self, brand, model, year, colour, for_sale):
        self.brand = brand
        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale


    def drive(self):
        print(f"You drive the {self.colour} {self.brand} {self.model}")

    def stop(self):
        print(f"Stop the {self.colour} {self.brand} {self.model}")