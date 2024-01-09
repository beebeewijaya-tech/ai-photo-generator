import time

from decouple import config

from services.ai import AiService
from services.digital_spaces import DigitalOceanSpaceService

do_svc = DigitalOceanSpaceService()
ai_svc = AiService()


class ImageManager:
    @staticmethod
    def upload_raw_photo(files):
        filenames = []
        for file in files:
            file_open = file.file.read()
            output_name = f"{file.filename}-{time.time():.0f}.png"
            do_svc.upload(file_open, f"raw/{output_name}")
            filenames.append(output_name)
        return filenames

    @staticmethod
    def generate_ai_photo(filenames):
        urls = []
        for filename in filenames:
            url = f"{config('SPACES_BUCKET_URL')}/{config('SPACES_BUCKET_NAME')}/raw/{filename}"
            urls.append(url)

        text_from_photo = ai_svc.image_to_text(urls)
        photo = ai_svc.text_to_image(
            f'Generate a single 3D front-facing chibi-style avatar with a front-facing view, placing a strong emphasis on detailed and captivating eyes and hair. The avatar should be set against a simple, empty background, featuring a carefully chosen background color that complements the character\'s design. in line with these criteria, {text_from_photo}' + ' choose one best expressions only for all findings, so you can just generate one of them')

        return photo
