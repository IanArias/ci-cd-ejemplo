from fastapi import FastAPI
from supabase import create_client, Client

# Usa tus claves reales
SUPABASE_URL = "https://sczbllylzrpevvjzdojb.supabase.co"
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNjemJsbHlsenJwZXZ2anpkb2piIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjMyMzM0NDIsImV4cCI6MjA3ODgwOTQ0Mn0.VHDACs3-sUtSyqbyv0SWcL2A-qPcLm1Gv4Bj0z1YVwk"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "API funcionando correctamente"}

@app.get("/notas")
def obtener_notas():
    data = supabase.table("notas").select("*").execute()
    return data.data

@app.post("/notas")
def agregar_nota(texto: str):
    data = supabase.table("notas").insert({"texto": texto}).execute()
    return {"insertado": data.data}
