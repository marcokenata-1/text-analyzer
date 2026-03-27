import requests
import psycopg2

NEON_URL = "https://ep-tiny-lake-a7f82uxx.neonauth.ap-southeast-2.aws.neon.tech/fund_data/"
API_REST_URL = "https://ep-tiny-lake-a7f82uxx.apirest.ap-southeast-2.aws.neon.tech/fund_data/"
EMAIL = "marcokenata1@gmail.com"
PASS = "12345678"

# 🔴 UPDATE THIS WITH YOUR ACTUAL POSTGRESQL CONNECTION STRING
# Example: "postgresql://postgres:password@localhost:5432/postgres"
DB_URL = "postgresql://localhost/postgres"

def fetch_and_save_data():
    # 1. Connect to PostgreSQL
    try:
        conn = psycopg2.connect(DB_URL)
        cursor = conn.cursor()
    except psycopg2.OperationalError as e:
        print(f"❌ Failed to connect to PostgreSQL: {e}")
        print("💡 Please make sure PostgreSQL is running and your DB_URL is correct.")
        return

    # 2. Check if the table already exists and has data (Skip the whole thing if it does)
    cursor.execute("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_name = 'financial_statements'
        );
    """)
    table_exists = cursor.fetchone()[0]
    
    if table_exists:
        cursor.execute("SELECT COUNT(*) FROM financial_statements")
        count = cursor.fetchone()[0]
        if count > 0:
            print(f"✅ Data already exists in PostgreSQL ({count} rows found in `financial_statements`).")
            print("⏭️ Skipping the entire API fetch process.")
            conn.close()
            return  # Skip the whole thing!

    # 3. If we reach here, we need to fetch the data
    print("⬇️ No data found in Postgres. Fetching from API...")
    session = requests.Session()
    
    # Get Auth Token
    token_resp = session.post(
        f"{NEON_URL}auth/sign-in/email",
        json={"email": EMAIL, "password": PASS},
        headers={"origin": NEON_URL}
    )
    token_resp.raise_for_status()
    token = token_resp.json()["token"]

    # Get JWT Token
    jwt_resp = session.get(
        f"{NEON_URL}auth/token",
        headers={"Authorization": f"Bearer {token}", "Origin": NEON_URL}
    )
    jwt_resp.raise_for_status()
    jwt_token = jwt_resp.json()["token"]

    # Get Financial Data
    data_resp = session.get(
        f"{API_REST_URL}rest/v1/financial_statements",
        headers={"Authorization": f"Bearer {jwt_token}", "Origin": API_REST_URL}
    )
    data_resp.raise_for_status()
    financial_data = data_resp.json()
    print(f"✅ Successfully fetched {len(financial_data)} records from API.")

    # 4. Save the data to PostgreSQL
    print("💾 Saving records directly to PostgreSQL...")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS financial_statements (
            id INTEGER PRIMARY KEY,
            description VARCHAR(255),
            amount NUMERIC(20, 2),
            note VARCHAR(255)
        )
    """)
    
    # We use ON CONFLICT DO NOTHING to prevent duplicate errors
    insert_query = """
        INSERT INTO financial_statements (id, description, amount, note)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING
    """
    
    for record in financial_data:
        cursor.execute(insert_query, (
            record.get('id'),
            record.get('description', ''),
            record.get('amount', 0.0),
            record.get('note', '')
        ))
        
    conn.commit()
    print("🎉 All data successfully saved to the database!")
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    fetch_and_save_data()
