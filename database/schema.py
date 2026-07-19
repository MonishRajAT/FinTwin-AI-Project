# Centralized SQL schema definitions for FinTwin AI.
# Each constant contains the SQL statement for creating one table.

# USERS
CREATE_USERS_TABLE = """
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

# FINANCIAL PROFILE (DIGITAL TWIN)
# Stores user-defined financial information that cannot be derived from transactions.
CREATE_FINANCIAL_PROFILE_TABLE = """
CREATE TABLE IF NOT EXISTS financial_profiles (
    profile_id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE
        REFERENCES users(user_id)
        ON DELETE CASCADE,
    monthly_income NUMERIC(12,2) DEFAULT 0,
    emergency_fund NUMERIC(12,2) DEFAULT 0,
    total_investments NUMERIC(12,2) DEFAULT 0,
    total_loans NUMERIC(12,2) DEFAULT 0,
    insurance_cover NUMERIC(12,2) DEFAULT 0,
    risk_appetite VARCHAR(20) DEFAULT 'Medium',
    investment_style VARCHAR(20) DEFAULT 'Balanced',
    preferred_currency VARCHAR(10) DEFAULT 'INR',
    monthly_budget NUMERIC(12,2) DEFAULT 0,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

# TRANSACTIONS
CREATE_TRANSACTIONS_TABLE = """
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id SERIAL PRIMARY KEY,
    user_id INTEGER
        REFERENCES users(user_id)
        ON DELETE CASCADE,
    transaction_date DATE NOT NULL,
    merchant VARCHAR(120),
    category VARCHAR(50),
    amount NUMERIC(12,2) NOT NULL,
    transaction_type VARCHAR(20) NOT NULL,
    payment_method VARCHAR(30),
    currency VARCHAR(10) DEFAULT 'INR',
    recurring BOOLEAN DEFAULT FALSE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

# FINANCIAL GOALS
CREATE_FINANCIAL_GOALS_TABLE = """
CREATE TABLE IF NOT EXISTS financial_goals (
    goal_id SERIAL PRIMARY KEY,
    user_id INTEGER
        REFERENCES users(user_id)
        ON DELETE CASCADE,
    goal_name VARCHAR(100),
    target_amount NUMERIC(12,2),
    current_amount NUMERIC(12,2) DEFAULT 0,
    target_date DATE,
    status VARCHAR(20) DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

# DOCUMENTS
CREATE_DOCUMENTS_TABLE = """
CREATE TABLE IF NOT EXISTS uploaded_documents (
    document_id SERIAL PRIMARY KEY,
    user_id INTEGER
        REFERENCES users(user_id)
        ON DELETE CASCADE,
    file_name VARCHAR(255),
    document_type VARCHAR(50),
    document_hash VARCHAR(128),
    document_size BIGINT,
    embedding_status VARCHAR(20) DEFAULT 'Pending',
    upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    processed_at TIMESTAMP
);
"""

# AI CHAT HISTORY
CREATE_CHAT_HISTORY_TABLE = """
CREATE TABLE IF NOT EXISTS ai_chat_history (
    chat_id SERIAL PRIMARY KEY,
    user_id INTEGER
        REFERENCES users(user_id)
        ON DELETE CASCADE,
    conversation_id UUID,
    user_query TEXT,
    ai_response TEXT,
    sources_used TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

# SCENARIO SIMULATIONS
CREATE_SCENARIO_TABLE = """
CREATE TABLE IF NOT EXISTS scenario_simulations (
    simulation_id SERIAL PRIMARY KEY,
    user_id INTEGER
        REFERENCES users(user_id)
        ON DELETE CASCADE,
    scenario_name VARCHAR(100),
    input_data JSONB,
    result_summary TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

# ML PREDICTIONS
CREATE_ML_PREDICTIONS_TABLE = """
CREATE TABLE IF NOT EXISTS ml_predictions (
    prediction_id SERIAL PRIMARY KEY,
    user_id INTEGER
        REFERENCES users(user_id)
        ON DELETE CASCADE,
    model_name VARCHAR(100),
    prediction_type VARCHAR(50),
    prediction_result JSONB,
    confidence NUMERIC(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

# FINANCIAL INSIGHTS
CREATE_FINANCIAL_INSIGHTS_TABLE = """
CREATE TABLE IF NOT EXISTS financial_insights (
    insight_id SERIAL PRIMARY KEY,
    user_id INTEGER
        REFERENCES users(user_id)
        ON DELETE CASCADE,
    insight_type VARCHAR(50),
    title VARCHAR(200),
    description TEXT,
    priority VARCHAR(20),
    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

# DASHBOARD METRICS
CREATE_DASHBOARD_METRICS_TABLE = """
CREATE TABLE IF NOT EXISTS dashboard_metrics (
    metric_id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE
        REFERENCES users(user_id)
        ON DELETE CASCADE,
    financial_health_score NUMERIC(5,2),
    monthly_cash_flow NUMERIC(12,2),
    savings_rate NUMERIC(6,2),
    debt_ratio NUMERIC(6,2),
    investment_ratio NUMERIC(6,2),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

# TABLE EXECUTION ORDER
ALL_TABLES = [
    CREATE_USERS_TABLE,
    CREATE_FINANCIAL_PROFILE_TABLE,
    CREATE_TRANSACTIONS_TABLE,
    CREATE_FINANCIAL_GOALS_TABLE,
    CREATE_DOCUMENTS_TABLE,
    CREATE_CHAT_HISTORY_TABLE,
    CREATE_SCENARIO_TABLE,
    CREATE_ML_PREDICTIONS_TABLE,
    CREATE_FINANCIAL_INSIGHTS_TABLE,
    CREATE_DASHBOARD_METRICS_TABLE,
]