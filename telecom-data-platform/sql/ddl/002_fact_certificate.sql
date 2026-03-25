CREATE TABLE IF NOT EXISTS fact_certificate (
    cert_id BIGSERIAL PRIMARY KEY,
    cert_business_id VARCHAR(80) UNIQUE NOT NULL,
    station_code VARCHAR(50) NOT NULL,
    issue_date DATE,
    expiry_date DATE,
    cert_type VARCHAR(50),
    issuing_agency VARCHAR(150),
    days_to_expiry INT,
    document_status VARCHAR(30),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
