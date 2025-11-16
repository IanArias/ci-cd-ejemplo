from supabase import create_client, Client

SUPABASE_URL = "https://TU-PROJECT-ID.supabase.co"
SUPABASE_ANON_KEY = "TU-ANON-KEY"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)
