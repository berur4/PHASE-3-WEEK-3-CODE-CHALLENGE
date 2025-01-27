import sqlite3
from models import Band, Venue, Concert

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

def user_input():
    print("Welcome to the Concerts Management System!")
    while True:
        print("\nPlease select an option:")
        print("1. View all Bands")
        print("2. View all Venues")
        print("3. View all Concerts")
        print("4. Add a new Concert")
        print("5. View a Band's Concerts")
        print("6. View a Venue's Concerts")
        print("7. View Band with Most Performances")  # New option
        print("8. Quit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            Band.test_queries()
        elif choice == '2':
            Venue.test_queries()
        elif choice == '3':
            Concert.test_queries()
        elif choice == '4':
            band_id = int(input("Enter Band ID: "))
            venue_id = int(input("Enter Venue ID: "))
            date = input("Enter Concert Date (YYYY-MM-DD): ")
            Band.play_in_venue(band_id, venue_id, date)
            print("Concert added successfully!")
        elif choice == '5':
            band_id = int(input("Enter Band ID: "))
            concerts = Band.concerts(band_id)
            for concert in concerts:
                print(concert)
        elif choice == '6':
            venue_id = int(input("Enter Venue ID: "))
            concerts = Venue.concerts(venue_id)
            for concert in concerts:
                print(concert)
        elif choice == '7':  # Handle the new option
            most_performances_band = Band.most_performances()
            if most_performances_band:
                print(f"Band with the most performances: {most_performances_band[1]} from {most_performances_band[2]} with {most_performances_band[3]} performances.")
            else:
                print("No bands found.")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    run_migrations()
    user_input()
