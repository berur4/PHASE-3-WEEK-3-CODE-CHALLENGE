import sqlite3

# Utility function for safe database queries
def safe_execute(query, params=()):
    """
    Executes a database query safely with error handling.
    """
    try:
        with sqlite3.connect("db/concerts.db") as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, params).fetchall()
            return result
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

class Band:
    @staticmethod
    def concerts(band_id):
        query = "SELECT * FROM concerts WHERE band_id = ?"
        results = safe_execute(query, (band_id,))
        if not results:
            print(f"No concerts found for band ID {band_id}.")
        return results

    @staticmethod
    def venues(band_id):
        query = """
            SELECT DISTINCT venues.* FROM venues
            JOIN concerts ON venues.id = concerts.venue_id
            WHERE concerts.band_id = ?
        """
        return safe_execute(query, (band_id,))

    @staticmethod
    def play_in_venue(band_id, venue_id, date):
        query = "INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)"
        safe_execute(query, (band_id, venue_id, date))

    @staticmethod
    def most_performances():
        query = """
            SELECT bands.*, COUNT(concerts.id) as num_concerts
            FROM bands
            JOIN concerts ON bands.id = concerts.band_id
            GROUP BY bands.id
            ORDER BY num_concerts DESC
            LIMIT 1
        """
        result = safe_execute(query)
        if result:
            return result[0]
        print("No bands found.")
        return None

    @staticmethod
    def all_introductions(band_id):
        """
        Returns a list of introduction strings for all concerts by this band.
        """
        query = """
            SELECT venues.city, bands.name, bands.hometown
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            JOIN venues ON concerts.venue_id = venues.id
            WHERE bands.id = ?
        """
        results = safe_execute(query, (band_id,))
        introductions = [
            f"Hello {result[0]}!!!!! We are {result[1]} and we're from {result[2]}"
            for result in results
        ]
        return introductions

class Venue:
    @staticmethod
    def concerts(venue_id):
        query = "SELECT * FROM concerts WHERE venue_id = ?"
        results = safe_execute(query, (venue_id,))
        if not results:
            print(f"No concerts found for venue ID {venue_id}.")
        return results

    @staticmethod
    def bands(venue_id):
        query = """
            SELECT DISTINCT bands.* FROM bands
            JOIN concerts ON bands.id = concerts.band_id
            WHERE concerts.venue_id = ?
        """
        return safe_execute(query, (venue_id,))

    @staticmethod
    def most_frequent_band(venue_id):
        query = """
            SELECT bands.*, COUNT(concerts.id) as num_concerts
            FROM bands
            JOIN concerts ON bands.id = concerts.band_id
            WHERE concerts.venue_id = ?
            GROUP BY bands.id
            ORDER BY num_concerts DESC
            LIMIT 1
        """
        result = safe_execute(query, (venue_id,))
        if result:
            return result[0]
        print(f"No frequent band found for venue ID {venue_id}.")
        return None

class Concert:
    @staticmethod
    def band(concert_id):
        query = """
            SELECT * FROM bands WHERE id = (SELECT band_id FROM concerts WHERE id = ?)
        """
        result = safe_execute(query, (concert_id,))
        if not result:
            print(f"No band found for concert ID {concert_id}.")
            return None
        return result[0]

    @staticmethod
    def venue(concert_id):
        query = """
            SELECT * FROM venues WHERE id = (SELECT venue_id FROM concerts WHERE id = ?)
        """
        result = safe_execute(query, (concert_id,))
        if not result:
            print(f"No venue found for concert ID {concert_id}.")
            return None
        return result[0]

    @staticmethod
    def hometown_show(concert_id):
        query = """
            SELECT CASE WHEN venues.city = bands.hometown THEN 1 ELSE 0 END
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            JOIN venues ON concerts.venue_id = venues.id
            WHERE concerts.id = ?
        """
        result = safe_execute(query, (concert_id,))
        if result and result[0][0] == 1:
            return True
        return False

    @staticmethod
    def introduction(concert_id):
        query = """
            SELECT venues.city, bands.name, bands.hometown
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            JOIN venues ON concerts.venue_id = venues.id
            WHERE concerts.id = ?
        """
        result = safe_execute(query, (concert_id,))
        if not result:
            print(f"No introduction available for concert ID {concert_id}.")
            return None
        return f"Hello {result[0][0]}!!!!! We are {result[0][1]} and we're from {result[0][2]}"
