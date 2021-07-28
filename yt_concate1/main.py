from yt_concate1.pipeline.steps.preflight import Preflight
from yt_concate1.pipeline.steps.get_video_list import GetVideoList
from yt_concate1.pipeline.steps.initialize_yt import InitializeYT
from yt_concate1.pipeline.steps.download_captions import DownloadCaptions
from yt_concate1.pipeline.steps.read_caption import ReadCaption
from yt_concate1.pipeline.steps.search import Search
from yt_concate1.pipeline.steps.download_videos import DownloadVideos
from yt_concate1.pipeline.steps.postflight import Postflight
from yt_concate1.pipeline.steps.step import StepException
from yt_concate1.pipeline.pipeline import Pipeline
from yt_concate1.utils import Utils



CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'incredible'
    }

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
