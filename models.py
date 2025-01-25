import sqlite3

class Band:
    @staticmethod
    def concerts(band_id):
        with sqlite3.connect("db/concerts.db") as conn:
            return conn.execute("SELECT * FROM concerts WHERE band_id = ?", (band_id,)).fetchall()

    @staticmethod
    def venues(band_id):
        with sqlite3.connect("db/concerts.db") as conn:
            return conn.execute("""
                SELECT DISTINCT venues.* FROM venues
                JOIN concerts ON venues.id = concerts.venue_id
                WHERE concerts.band_id = ?
            """, (band_id,)).fetchall()

    @staticmethod
    def play_in_venue(venue_id, date):
        with sqlite3.connect("db/concerts.db") as conn:
            conn.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)", (band_id, venue_id, date))

    @staticmethod
    def most_performances():
        with sqlite3.connect("db/concerts.db") as conn:
            result = conn.execute("""
                SELECT bands.*, COUNT(concerts.id) as num_concerts
                FROM bands
                JOIN concerts ON bands.id = concerts.band_id
                GROUP BY bands.id
                ORDER BY num_concerts DESC
                LIMIT 1
            """).fetchone()
        return result

class Venue:
    @staticmethod
    def concerts(venue_id):
        with sqlite3.connect("db/concerts.db") as conn:
            return conn.execute("SELECT * FROM concerts WHERE venue_id = ?", (venue_id,)).fetchall()

    @staticmethod
    def bands(venue_id):
        with sqlite3.connect("db/concerts.db") as conn:
            return conn.execute("""
                SELECT DISTINCT bands.* FROM bands
                JOIN concerts ON bands.id = concerts.band_id
                WHERE concerts.venue_id = ?
            """, (venue_id,)).fetchall()

    @staticmethod
    def most_frequent_band(venue_id):
        with sqlite3.connect("db/concerts.db") as conn:
            return conn.execute("""
                SELECT bands.*, COUNT(concerts.id) as num_concerts
                FROM bands
                JOIN concerts ON bands.id = concerts.band_id
                WHERE concerts.venue_id = ?
                GROUP BY bands.id
                ORDER BY num_concerts DESC
                LIMIT 1
            """, (venue_id,)).fetchone()


class Concert:
    @staticmethod
    def band(concert_id):
        with sqlite3.connect("db/concerts.db") as conn:
            return conn.execute("SELECT * FROM bands WHERE id = (SELECT band_id FROM concerts WHERE id = ?)", (concert_id,)).fetchone()

    @staticmethod
    def venue(concert_id):
        with sqlite3.connect("db/concerts.db") as conn:
            return conn.execute("SELECT * FROM venues WHERE id = (SELECT venue_id FROM concerts WHERE id = ?)", (concert_id,)).fetchone()

    @staticmethod
    def hometown_show(concert_id):
        with sqlite3.connect("db/concerts.db") as conn:
            result = conn.execute("""
                SELECT CASE WHEN venues.city = bands.hometown THEN 1 ELSE 0 END
                FROM concerts
                JOIN bands ON concerts.band_id = bands.id
                JOIN venues ON concerts.venue_id = venues.id
                WHERE concerts.id = ?
            """, (concert_id,)).fetchone()
        return bool(result[0])

    @staticmethod
    def introduction(concert_id):
        with sqlite3.connect("db/concerts.db") as conn:
            result = conn.execute("""
                SELECT venues.city, bands.name, bands.hometown
                FROM concerts
                JOIN bands ON concerts.band_id = bands.id
                JOIN venues ON concerts.venue_id = venues.id
                WHERE concerts.id = ?
            """, (concert_id,)).fetchone()
        return f"Hello {result[0]}!!!!! We are {result[1]} and we're from {result[2]}"
