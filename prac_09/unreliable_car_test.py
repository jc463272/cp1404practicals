"""
CP1404 - William Hunter
Time to test some unreliable cars
Estimated: 20 mins
Actual:
"""

from unreliable_car import UnreliableCar

def main():
    """Test unreliable cars."""
    # create cars with different reliabilities
    bad_car = UnreliableCar(name="No good", fuel = 90, reliability= 10)
    good_car = UnreliableCar(name="Good", fuel = 90, reliability= 90)

    # attempt to drive the car and output of distance driven
    for i in range(1,10):
        print(f"attempting to drive {i}km:")
        print(f"{good_car.name:10} drove {good_car.drive(i):2}km")
        print(f"{bad_car.name:10} drove {bad_car.drive(i):2}km")

    # print final
    print(good_car)
    print(bad_car)

main()
