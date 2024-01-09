from decouple import config
from openai import OpenAI


class AiService():
    client = None

    def __init__(self):
        self.client = OpenAI(
            # This is the default and can be omitted
            api_key=config("OPENAI_API_KEY"),
        )

    def image_to_text(self, images):
        content = [
            {"type": "text", "text": "What’s in this image?"}
        ]

        for image in images:
            content.append({
                "type": "image_url",
                "image_url": {
                    "url": image
                },
            })
        response = self.client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": content
                }
            ],
            max_tokens=300,
        )
        return response.choices[0].message.content

    def text_to_image(self, prompt):
        response = self.client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        return response.data
