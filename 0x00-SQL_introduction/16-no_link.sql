#!/usr/bin/python3
-- script that lists all records of the table second_table without rows that don't have a name value.
SELECT score, name
    FROM second_table
    WHERE name IS NOT NULL AND name <> ''
    ORDER BY score DESC;
