import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import scraper

cred = credentials.Certificate("./utilify-acd8b.json")
app = firebase_admin.initialize_app(cred)
firestore_client = firestore.client()

def insert_track(track_id,rating):
    artist, name, tempo, energy, danceability, popularity = scraper.get_track_info(track_id)
    doc_ref = firestore_client.collection('tracks')
    doc_ref.add({
        'artist': artist,
        'name': name,
        'tempo': tempo,
        'energy': energy,
        'danceability': danceability,
        'popularity': popularity,
        'rating': rating
    })