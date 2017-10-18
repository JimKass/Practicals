from prac_08.unreliable_car import UnreliableCar

print("Testing Initialization...")
delorean = UnreliableCar("DeLorean", 100, 50)
print(delorean)

print("Testing Initialization...")
print(delorean.drive(10))
print(delorean)
delorean.drive(10)
print(delorean)
delorean.drive(10)
print(delorean)
