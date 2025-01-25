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
INSERT INTO bands (name, hometown) VALUES ('The Beatles', 'Liverpool'), ('Queen', 'London');

-- Insert sample venues
INSERT INTO venues (title, city) VALUES ('Madison Square Garden', 'New York'), ('Wembley Stadium', 'London');

-- Insert sample concerts
INSERT INTO concerts (band_id, venue_id, date) VALUES (1, 1, '2025-01-15'), (2, 2, '2025-01-20');
