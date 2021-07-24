from yt_concate1.pipeline.steps.get_video_list import GetVideoList
from yt_concate1.pipeline.steps.step import StepException

from yt_concate1.pipeline.pipeline import Pipeline


CHANNEL_ID = 'UCJFN9Mo4AMR_qZ1ZB6i2N8Q'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    steps = [
        GetVideoList()
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
