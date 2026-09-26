CREATE TABLE dim_refinery (
    refinery_key BIGSERIAL PRIMARY KEY,
    refinery_id TEXT UNIQUE NOT NULL,
    refinery_name TEXT NOT NULL,
    operator TEXT,
    state TEXT,
    padd TEXT,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    status TEXT
);

CREATE TABLE dim_complexity (
    complexity_key BIGSERIAL PRIMARY KEY,
    nci NUMERIC,
    complexity_tier TEXT,
    nci_source TEXT,
    nci_date DATE,
    nci_method TEXT
);

CREATE TABLE dim_time (
    time_key INTEGER PRIMARY KEY,
    calendar_date DATE NOT NULL,
    year INTEGER,
    quarter INTEGER,
    month INTEGER
);

CREATE TABLE fact_refinery_capacity (
    refinery_key BIGINT REFERENCES dim_refinery(refinery_key),
    complexity_key BIGINT REFERENCES dim_complexity(complexity_key),
    time_key INTEGER REFERENCES dim_time(time_key),
    crude_capacity_bpd NUMERIC,
    PRIMARY KEY (refinery_key, time_key)
);
