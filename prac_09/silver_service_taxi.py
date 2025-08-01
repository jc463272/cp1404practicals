"""
CP1404 - William Hunter
New Silver Service Taxi class which inherits Taxi.
Estimate: 30 mins
Actual: 20 mins
"""

from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """New fancy taxi class"""
    flagfall = 4.50
    def __init__(self, name, fuel, fanciness):
        """Initialise the Silver Service Taxi class."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """String representation of the Silver Service Taxi class."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Calculate the current fare."""
        return self.flagfall + super().get_fare()
