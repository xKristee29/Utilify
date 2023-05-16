import gspread
from oauth2client.service_account import ServiceAccountCredentials
import scraper

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
		"https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("UtilifyDB").sheet1

def insert_track(track_id,rating):
    artist, track_name, tempo, energy, danceability, popularity = scraper.get_track_info(track_id)
    row = [track_id, artist, track_name, tempo, energy, danceability, popularity, rating]
    sheet.insert_row(row,2)