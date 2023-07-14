from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

url: str = os.getenv('SUPABASE_URL')
key: str = os.getenv('SUPABASE_KEY')
supabase: Client = create_client(url, key)

def get_tracks():
    return supabase.table('tracks').select('*').execute().data

def get_track(track_id):
    try:
        data = supabase.table('tracks').select('*').eq('track_id', track_id).execute().data[0]
    except Exception as e:
        raise Exception('Track not found')
    return data

def get_track_by_hash(hash):
    try:
        data = supabase.table('tracks').select('*').eq('hash', hash).execute().data[0]
    except Exception as e:
        raise Exception('Track not found')
    return data


def get_tracks_by_criteria(danceability, energy, tempo_min, tempo_max):
    danceability = danceability / 100.0
    energy = energy / 100.0
    tracks = supabase.table('tracks').select('*').gte('danceability', danceability).gte('energy', energy).gte('tempo', tempo_min).lte('tempo', tempo_max).execute().data
    return tracks

def insert_track(track):
    try:
        supabase.table('tracks').insert(track).execute()
        return True
    except Exception as e:
        print(e)
        return False