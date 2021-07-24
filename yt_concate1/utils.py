import os
from yt_concate1.settings import DOWNLOADS_DIR
from yt_concate1.settings import VIDEOS_DIR
from yt_concate1.settings import CAPTIONS_DIR


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def create_dir():
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)

    @staticmethod
    def get_video_id_from_url(url):
        return url.split('watch?v=')[-1]

    def get_cation_path(self, url):
        return os.path.join(CAPTIONS_DIR, self.get_video_id_from_url(url) + '.txt')
