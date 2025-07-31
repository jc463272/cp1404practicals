"""
CP1404 - William Hunter
Estimate:20 mins
Actual:10 mins
"""

from taxi import Taxi

def main():
    """Test taxi class."""
    #Create taxi object for testing
    my_taxi = Taxi("Prius 1", fuel = int(100), price_per_km = float(1.23))
    print(my_taxi)

    #Drive taxi 40km
    my_taxi.drive(40)

    #Print details and current fair
    print(my_taxi)
    print(my_taxi.get_fare())

    #Restart the meter and drive 100km
    my_taxi.start_fare()
    my_taxi.drive(100)

    #Print details and current fare
    print(my_taxi)
    print(my_taxi.get_fare())

main()
