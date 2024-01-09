## Introduction

Applying a AI Generator project using OpenAI, you can upload your own photo to the API and it will extract the criteria
of your photo, the information.
And we will use that photo information to generate some sort-of avaatar for you

## Tools that been used

1. OpenAI Vision - To convert from image to text
2. OpenAI Image generator - To convert from text to image

## Flow

1. Upload photo
2. Vision will detect what is the photo criteria looks like, it will extract the information from the photo
3. We will passed the text from vision to the image generator as a prompt
4. It will generate a result

## Demo link

## Image sample

![Alt text](./docs/upload_ui.png?raw=true "Upload UI")
![Alt text](./docs/sample_1.png?raw=true "Sample 1")
![Alt text](./docs/sample_2.png?raw=true "Sample 2")
![Alt text](./docs/sample_3.png?raw=true "Sample 3")
![Alt text](./docs/sample_4.png?raw=true "Sample 4")
