import sqlite3
from models import Band

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

# Function to test database queries
def test_queries():
    conn = sqlite3.connect('db/concerts.db')
    cursor = conn.cursor()

    # Fetch all bands
    print("=" * 50)
    print("All Bands:")
    cursor.execute("SELECT * FROM bands")
    bands = cursor.fetchall()
    for band in bands:
        print(f"ID: {band[0]}, Name: {band[1]}, Hometown: {band[2]}")
    print("=" * 50)

    # Fetch all venues
    print("\nAll Venues:")
    cursor.execute("SELECT * FROM venues")
    venues = cursor.fetchall()
    for venue in venues:
        print(f"ID: {venue[0]}, Title: {venue[1]}, City: {venue[2]}")
    print("=" * 50)

    # Fetch all concerts
    print("\nAll Concerts:")
    cursor.execute("SELECT * FROM concerts")
    concerts = cursor.fetchall()
    for concert in concerts:
        print(f"ID: {concert[0]}, Band ID: {concert[1]}, Venue ID: {concert[2]}, Date: {concert[3]}")
    print("=" * 50)

    # Fetch a band for a specific concert
    concert_id = 2
    print(f"\nBand for Concert ID {concert_id}:")
    cursor.execute("""
        SELECT bands.name, bands.hometown
        FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        WHERE concerts.id = ?
    """, (concert_id,))
    band = cursor.fetchone()
    if band:
        print(f"Name: {band[0]}, Hometown: {band[1]}")
    else:
        print("No band found.")
    print("=" * 50)

    # Fetch all concerts for a venue
    venue_id = 2
    print(f"\nConcerts for Venue ID {venue_id}:")
    cursor.execute("""
        SELECT concerts.id, concerts.date, bands.name
        FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        WHERE concerts.venue_id = ?
    """, (venue_id,))
    venue_concerts = cursor.fetchall()
    for concert in venue_concerts:
        print(f"Concert ID: {concert[0]}, Date: {concert[1]}, Band: {concert[2]}")
    print("=" * 50)

    conn.close()

# Function to test the Band.all_introductions method
def test_band_introductions():
    band_id = 1  # Change this to test with different band IDs
    introductions = Band.all_introductions(band_id)
    print(f"Introductions for Band ID {band_id}:")
    for intro in introductions:
        print(intro)

if __name__ == '__main__':
    # Run migrations and seed data
    run_migrations()

    # Test database queries
    test_queries()

    # Test Band.all_introductions()
    test_band_introductions()
