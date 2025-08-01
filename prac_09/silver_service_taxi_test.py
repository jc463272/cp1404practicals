"""
CP1404 - William Hunter
Test SilverServiceTaxi class
Estimate: 30 mins
Actual: 20 mins
"""

from silver_service_taxi import SilverServiceTaxi

def main():
    """Test SilverServiceTaxi class"""
    taxi = SilverServiceTaxi("Silver Service Taxi test", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(f"\nThe total fare price is ${taxi.get_fare():.2f}")

main()
