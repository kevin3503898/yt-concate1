import os

from pytube import YouTube

from yt_concate1.pipeline.steps.step import Step


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        for url in data:
            # download the package by:  pip install pytube
            source = YouTube(url)
            en_caption = source.captions.get_by_language_code('a.en')
            en_caption_convert_to_srt = (en_caption.generate_srt_captions())

            print(en_caption_convert_to_srt)
            # save the caption to a file named Output.txt
            text_file = open(utils.get_video_id_from_url(url) + "txt", "w")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
            break


