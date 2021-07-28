from .step import Step
from yt_concate1.model.found import Found


class Search(Step):
    def process(self, data, inputs, utils):
        search_word = inputs['search_word']


        found = []
        for yt in data:
            if not captions:
                continue

            captions = yt.captions
            for caption in captions:
                if search_word in caption:
                    time = captions[caption]
                    f = Found(yt, caption. time)
                    found.append(f)

        print(len(found))
        return found
