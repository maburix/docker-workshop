
CREATE ROLE hello_user WITH LOGIN PASSWORD 'hello_pg#1';

CREATE DATABASE hello_app OWNER hello_user;

\c hello_app

CREATE TABLE counter (
    date TIMESTAMP,
    counter SERIAL
);

ALTER TABLE counter OWNER TO hello_user;