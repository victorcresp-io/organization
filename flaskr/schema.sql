DROP TABLE IF EXISTS uber_daily_money;
DROP TABLE IF EXISTS uber_daily_cost;


CREATE TABLE IF NOT EXISTS uber_daily_money (
    cost FLOAT,
    date TEXT,
    spent_time TEXT
);

CREATE TABLE IF NOT EXISTS uber_daily_cost (
    date TEXT,
    cost REAL,
    cost_description TEXT
);

CREATE TABLE IF NOT EXISTS despesas(
    id_despesa INTEGER PRIMARY KEY,
    data TEXT,
    tipo_despesa TEXT,
    explicacao_despesa TEXT,
    item_despesa TEXT
);