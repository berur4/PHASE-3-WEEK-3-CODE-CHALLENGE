import sqlite3

# Utility function for safe database queries
def safe_execute(query, params=()):
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
        return safe_execute(query, (band_id,))

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
    def all_introductions(band_id):
        query = """
            SELECT venues.city, bands.name, bands.hometown
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            JOIN venues ON concerts.venue_id = venues.id
            WHERE bands.id = ?
        """
        results = safe_execute(query, (band_id,))
        return [
            f"Hello {result[0]}!!!!! We are {result[1]} and we're from {result[2]}"
            for result in results
        ]

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
        return None

    @staticmethod
    def test_queries():
        print("=" * 50)
        print("All Bands:")
        bands = safe_execute("SELECT * FROM bands")
        for band in bands:
            print(f"ID: {band[0]}, Name: {band[1]}, Hometown: {band[2]}")
        print("=" * 50)

class Venue:
    @staticmethod
    def concerts(venue_id):
        query = "SELECT * FROM concerts WHERE venue_id = ?"
        return safe_execute(query, (venue_id,))

    @staticmethod
    def bands(venue_id):
        query = """
            SELECT DISTINCT bands.* FROM bands
            JOIN concerts ON bands.id = concerts.band_id
            WHERE concerts.venue_id = ?
        """
        return safe_execute(query, (venue_id,))

    @staticmethod
    def concert_on(date):
        query = "SELECT * FROM concerts WHERE date = ? LIMIT 1"
        result = safe_execute(query, (date,))
        return result[0] if result else None

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
        return result[0] if result else None

    @staticmethod
    def test_queries():
        print("=" * 50)
        print("All Venues:")
        venues = safe_execute("SELECT * FROM venues")
        for venue in venues:
            print(f"ID: {venue[0]}, Title: {venue[1]}, City: {venue[2]}")
        print("=" * 50)

class Concert:
    @staticmethod
    def band(concert_id):
        query = """
            SELECT * FROM bands WHERE id = (SELECT band_id FROM concerts WHERE id = ?)
        """
        result = safe_execute(query, (concert_id,))
        return result[0] if result else None

    @staticmethod
    def venue(concert_id):
        query = """
            SELECT * FROM venues WHERE id = (SELECT venue_id FROM concerts WHERE id = ?)
        """
        result = safe_execute(query, (concert_id,))
        return result[0] if result else None

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
        return result[0][0] == 1 if result else False

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
        if result:
            return f"Hello {result[0][0]}!!!!! We are {result[0][1]} and we're from {result[0][2]}"
        return None

    @staticmethod
    def test_queries():
        print("=" * 50)
        print("All Concerts:")
        concerts = safe_execute("SELECT * FROM concerts")
        for concert in concerts:
            print(f"ID: {concert[0]}, Band ID: {concert[1]}, Venue ID: {concert[2]}, Date: {concert[3]}")
        print("=" * 50)
