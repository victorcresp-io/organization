DROP TABLE IF EXISTS uber_diaria
DROP TABLE IF EXISTS uber_gastos

CREATE TABLE uber_daily_money (
    cost FLOAT,
    date TEXT,
    spent_time TEXT
);

CREATE TABLE uber_daily_cost (
    cost REAL,
    cost_description TEXT
);