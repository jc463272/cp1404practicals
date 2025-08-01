"""
CP1404 - William Hunter
Missing Band class for program my_band.py
Estimated: 20 mins
Actual: 26 mins
"""

class Band:
    """Band class with musicians."""
    def __init__(self, name):
        """Initialise instances of band class."""
        self.name = name
        self.members = []

    def add(self, musician):
        """Add members to band."""
        self.members.append(musician)

    def play(self):
        """Each musician is playing what instrument."""
        return "\n".join(member.play() for member in self.members)

    def __str__(self):
        """String representation of band."""
        members_str = ','.join(str(member) for member in self.members)
        return f"{self.name} ({members_str})"
