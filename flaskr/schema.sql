DROP TABLE IF EXISTS uber_daily_money;
DROP TABLE IF EXISTS uber_daily_cost;


CREATE TABLE uber_daily_money (
    cost FLOAT,
    date TEXT,
    spent_time TEXT
);

CREATE TABLE uber_daily_cost (
    date TEXT,
    cost REAL,
    cost_description TEXT
)