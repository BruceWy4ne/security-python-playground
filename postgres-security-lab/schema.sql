CREATE TABLE users (
    id serial primary key,
    username text unique not null,
    email text unique,
    pass text not null,
    created date not null
);

CREATE TABLE login (
    id serial primary key,
    user_id integer not null references users(id),
    status text not null,
    attempted date not null,
    ip text not null
);