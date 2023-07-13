import database as db
from sklearn.metrics.pairwise import cosine_similarity
import random

class MusicData:
    def __init__(self):
        self.update_data()
        
    def update_data(self):
        data = db.get_tracks()
        if len(data) > 0:
            self.track_dict = {}
            self.data = []
            self.track_data = []
            for i, track in enumerate(data):
                self.track_dict[track['track_id']] = i
                self.track_data.append({'id':track['track_id'], 'name':track['track_name']})
                self.data.append(track['tags'])
            self.train_model()
    
    def get_data(self):
        return self.data
    
    def train_model(self):
        self.cosine_sim = cosine_similarity(self.data)

    def recommend_by_track(self, track_id, limit):
        track_index = self.track_dict[track_id]
        similar_tracks = list(enumerate(self.cosine_sim[track_index]))
        sorted_similar_tracks = sorted(similar_tracks, key=lambda x:x[1], reverse=True)[1:]
        recommended_tracks = []
        for i in range(limit):
            self.track_data[sorted_similar_tracks[i][0]]['similarity'] = sorted_similar_tracks[i][1]
            recommended_tracks.append(self.track_data[sorted_similar_tracks[i][0]])
        return recommended_tracks
    
    def recommend_random(self, limit):
        track = random.choice(self.track_data)
        return [track] + self.recommend_by_track(track['id'], limit)