#!/usr/bin/python3
-- script that creates the table unique_id on your MySQL server.
CREATE TABLE IF NOT EXISTS unique_id
    (id INT DEFAULT 1 PRIMARY KEY,
    name VARCHAR(256)
    );
