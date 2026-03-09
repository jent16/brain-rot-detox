import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load variables from .env
load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

if not url or not key:
    print("Error: SUPABASE_URL or SUPABASE_KEY not found in .env file!")
    exit()

supabase: Client = create_client(url, key)

def fetch_latest_logs():
    try:
        # Fetching the last 5 entries from usage_logs to test
        response = supabase.table("usage_logs").select("*").limit(5).execute()
        print(f"Connection Successful! Found {len(response.data)} logs.")
        for log in response.data:
            print(f"Video detected: {log.get('video_url')}")
    except Exception as e:
        print(f"Error connecting to Supabase: {e}")

if __name__ == "__main__":
    fetch_latest_logs()