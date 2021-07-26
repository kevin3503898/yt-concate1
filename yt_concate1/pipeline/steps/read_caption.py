import os
from pprint import pprint

from .step import Step
from yt_concate1.settings import CAPTIONS_DIR

class ReadCaption:

    def process(self, data, inputs, utils):
        data = {}
        for caption_file in os.listder(CAPTIONS_DIR):
            captions = {}
            with open(os.path.join(CAPTIONS_DIR, caption_file), 'r') as f:
                time_line = False
                time = None
                caption = None
                for line in f:
                    if '-->' in line:
                        time_line = True
                        time = line
                        continue
                    if time_line:
                        caption = line
                        captions[caption] = time
                        time_line = False
            data[caption_file] = captions


        pprint(data)
        return data


