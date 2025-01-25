import sqlite3

# Function to run migrations and seed data
def run_migrations():
    with open('schema.sql', 'r') as file:
        schema = file.read()

    conn = sqlite3.connect('db/concerts.db')
    cursor = conn.cursor()

    # Execute schema and seed data
    cursor.executescript(schema)
    print("Database initialized and seeded successfully.")

    conn.commit()
    conn.close()

# Function to test the database and queries
def test_queries():
    conn = sqlite3.connect('db/concerts.db')
    cursor = conn.cursor()

    # Test: Fetch all bands
    print("\nAll Bands:")
    cursor.execute("SELECT * FROM bands")
    print(cursor.fetchall())

    # Test: Fetch all venues
    print("\nAll Venues:")
    cursor.execute("SELECT * FROM venues")
    print(cursor.fetchall())

    # Test: Fetch all concerts
    print("\nAll Concerts:")
    cursor.execute("SELECT * FROM concerts")
    print(cursor.fetchall())

    # Test: Fetch a band for a specific concert
    concert_id = 1
    print(f"\nBand for Concert ID {concert_id}:")
    cursor.execute("""
        SELECT bands.name, bands.hometown
        FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        WHERE concerts.id = ?
    """, (concert_id,))
    print(cursor.fetchone())

    # Test: Fetch all concerts for a venue
    venue_id = 1
    print(f"\nConcerts for Venue ID {venue_id}:")
    cursor.execute("""
        SELECT concerts.id, concerts.date, bands.name
        FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        WHERE concerts.venue_id = ?
    """, (venue_id,))
    print(cursor.fetchall())

    conn.close()

if __name__ == '__main__':
    # Run migrations and seed data
    run_migrations()

    # Test database queries
    test_queries()
