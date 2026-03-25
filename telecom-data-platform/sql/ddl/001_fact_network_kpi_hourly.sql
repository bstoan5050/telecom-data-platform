CREATE TABLE IF NOT EXISTS fact_network_kpi_hourly (
    network_kpi_id BIGSERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    station_code VARCHAR(50) NOT NULL,
    cell_code VARCHAR(80) NOT NULL,
    total_call_attempt INT NOT NULL,
    connected_call INT NOT NULL,
    miss_call INT NOT NULL,
    silence_call INT NOT NULL,
    drop_call INT NOT NULL,
    miss_call_rate NUMERIC(12,6),
    silence_call_rate NUMERIC(12,6),
    mc_staon_num_r NUMERIC(12,6),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
