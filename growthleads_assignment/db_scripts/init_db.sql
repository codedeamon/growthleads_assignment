--//CREATE SCHEMA [IF NOT EXISTS] growthleads;
--
--
--//SET search_path TO assignment;


CREATE TABLE IF NOT EXISTS country_info (
    name text primary key,
    capital text,
    region text,
    subregion text,
    population int,
    currency text
);