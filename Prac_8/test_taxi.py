from Prac_8.Car import Taxi
from Prac_8.Car import Unreliablecar
from Prac_8.Car import SilverServiceTaxi

taxi1 = Taxi('Prius 1',100)
taxi1.drive(40)

print(taxi1)
print(taxi1.get_fare())

taxi1.start_fare()
taxi1.drive(100)

print(taxi1)
print(taxi1.get_fare())

unreliable = Unreliablecar("Carl's Car", 100, 25)
print(unreliable.drive(40))

silver = SilverServiceTaxi('Huma', 100, 2)
silver.drive(10)
print(silver)
print(silver.get_fare())