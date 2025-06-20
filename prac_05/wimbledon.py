"""
Wimbledon
Estimate: 20 mins
Actual: 50 mins
CP1404 - William Hunter
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read data file and print Wimbledon winners and their countries."""
    records = load_records(FILENAME)
    player_to_wins, countries = process_records(records)
    display_results(player_to_wins, countries)


def process_records(records):
    """Create dictionary and set from records"""
    player_to_wins = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            player_to_wins[record[INDEX_CHAMPION]] += 1
        except KeyError:
            player_to_wins[record[INDEX_CHAMPION]] = 1
    return player_to_wins, countries


def load_records(filename):
    """Load records from file."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as infile:
        infile.readline()
        for line in infile:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def display_results(player_to_wins, countries):
    """Display results."""
    print("Wimbledon Winners:\n")
    name_length = max(len(player) for player in player_to_wins)
    for player, wins in player_to_wins.items():
        print(f"{player:{name_length}} \t{wins}")
    print(f"\nThese countries {len(countries)} have one Wimbledon")
    print(", ".join(sorted(countries)))


main()
