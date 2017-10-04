from prac_08.taxi import Taxi

print("Testing Initialization...")
prius = Taxi("Prius 1", 100)
print(prius)

print("\nTesting Drive method...")
prius.drive(40)
print(prius, "(Excepting fuel=60 and odometer=40)")

print("\nTesting get_fare method...")
print(prius.get_fare(), "(Expecting 49.2)")

print("\nTesting start_fare method...")
prius.start_fare()

print()
print(prius)
print(prius.get_fare(), "(Expecting 0.0)")
