"""

"""

from prac_08.silver_service_taxi import SilverServiceTaxi

print("Testing Initialization...")
limo = SilverServiceTaxi("Limo", 100, 2)
print(limo)

print("\nTesting drive method...")
limo.drive(18)
print(limo)

print("\nTesting get_fare method...")
print(limo.get_fare())
