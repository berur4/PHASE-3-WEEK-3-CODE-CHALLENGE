# Concerts Management System

## Overview

The **Concerts Management System** is a Python-based application that interacts with a SQLite database to manage data related to bands, venues, and concerts. It allows users to view details about bands, venues, and concerts, as well as perform actions such as adding concerts and querying band and venue information.

This project consists of the following components:

- **Database**: A SQLite database to store and retrieve data about concerts, bands, and venues.
- **Models**: Python classes (`Band`, `Venue`, and `Concert`) that interact with the database.
- **Migrations**: A schema to set up the database structure and seed it with sample data.
- **User Interface**: A simple text-based menu allowing users to interact with the system.

## Features

### Core Features

1. **View All Bands**: Displays a list of all bands in the system, including their ID, name, and hometown.
2. **View All Venues**: Displays a list of all venues in the system, including their ID, title, and city.
3. **View All Concerts**: Displays a list of all concerts, including the band, venue, and date.
4. **Add a New Concert**: Allows users to add a new concert by providing a band ID, venue ID, and concert date.
5. **View a Band's Concerts**: Allows users to view all concerts of a specific band.
6. **View a Venue's Concerts**: Allows users to view all concerts held at a specific venue.
7. **View Band with Most Performances**: Displays the band with the most concerts performed, along with the number of performances.
8. **Exit**: Exits the application.

### Database Schema

The system uses the following tables:

- **Bands**: Stores band information including ID, name, and hometown.
- **Venues**: Stores venue information including ID, title, and city.
- **Concerts**: Stores concert information, linking bands and venues with a concert date.

The schema is defined in the `schema.sql` file and is executed when the program is run to initialize the database.

### Sample Data

The system comes pre-loaded with sample data for 10 bands, 10 venues, and 10 concerts. These are inserted into the database upon initialization.

## Setup and Installation

### Prerequisites

- Python 3.x
- SQLite (SQLite is bundled with Python, so you don't need to install it separately)

### Steps to Set Up the Project

1. **Clone the Repository**

   Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/berur4/PHASE-3-WEEK-3-CODE-CHALLENGE
   cd concerts-management-system

This project does not require any external libraries beyond Python's standard library. However, you will need to make sure Python 3.x is installed on your machine.


Welcome to the Concerts Management System!
Please select an option:
1. View all Bands
2. View all Venues
3. View all Concerts
4. Add a new Concert
5. View a Band's Concerts
6. View a Venue's Concerts
7. View Band with Most Performances
8. Quit
Choose options from the menu to interact with the system.

Code Explanation
main.py
The main.py file contains the core logic of the application:

run_migrations(): Initializes the database by running the schema.sql file to create tables and insert sample data.
user_input(): Displays the user interface and handles user input for interacting with the system.
models.py
The models.py file contains three classes: Band, Venue, and Concert. These classes represent entities in the database and contain methods to interact with the database.

Band Class: Contains methods to retrieve concerts of a band, view venues where a band performs, and play concerts at venues.
Venue Class: Contains methods to retrieve concerts at a venue, view bands that perform at a venue, and find the most frequent band at a venue.
Concert Class: Contains methods to retrieve information about the concert's band and venue, check if a concert is a hometown show, and provide an introduction to the concert.
Database Operations
The database operations are handled using a utility function, safe_execute(), which safely executes SQL queries with parameters.

Contribution
Feel free to fork this repository and submit issues or pull requests if you would like to contribute improvements or new features.

New Features
Band and venue performance tracking
Ability to generate reports based on concerts and performances

Contact
For any questions or feedback, please reach out to:

Author: Caleb Koech
Email: berurcaleb@gmail.com