DROP TABLE IF EXISTS concerts;
DROP TABLE IF EXISTS bands;
DROP TABLE IF EXISTS venues;



CREATE TABLE bands (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    hometown TEXT NOT NULL
);

CREATE TABLE venues (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    city TEXT NOT NULL
);

CREATE TABLE concerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    band_id INTEGER NOT NULL,
    venue_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY (band_id) REFERENCES bands (id),
    FOREIGN KEY (venue_id) REFERENCES venues (id)
);

-- Insert sample bands
INSERT INTO bands (name, hometown) VALUES 
('The Beatles', 'Liverpool'),
('Wakadinali', 'Kayole'),
('Queen', 'London'),
('Coldplay', 'London'),
('Sauti Sol', 'Nairobi'),
('Imagine Dragons', 'Las Vegas'),
('H_art the Band', 'Nairobi'),
('BTS', 'Seoul'),
('Metallica', 'San Francisco'),
('Florence and the Machine', 'London');

-- Insert sample venues
INSERT INTO venues (title, city) VALUES 
('Madison Square Garden', 'New York'),
('Wembley Stadium', 'London'),
('Kasarani Stadium', 'Nairobi'),
('The O2 Arena', 'London'),
('Sydney Opera House', 'Sydney'),
('Hollywood Bowl', 'Los Angeles'),
('Allianz Arena', 'Munich'),
('Tokyo Dome', 'Tokyo'),
('The Gorge Amphitheatre', 'Washington'),
('Red Rocks Amphitheatre', 'Colorado');

-- Insert sample concerts
INSERT INTO concerts (band_id, venue_id, date) VALUES 
(1, 1, '2025-01-15'),
(2, 2, '2025-01-20'),
(3, 3, '2025-02-05'),
(4, 4, '2025-02-10'),
(5, 5, '2025-03-01'),
(6, 6, '2025-03-15'),
(7, 7, '2025-04-01'),
(8, 8, '2025-04-20'),
(9, 9, '2025-05-05'),
(10, 10, '2025-05-20'),
(1, 4, '2025-06-01'),
(3, 5, '2025-06-10'),
(5, 1, '2025-07-01'),
(7, 2, '2025-07-15'),
(9, 6, '2025-08-05');