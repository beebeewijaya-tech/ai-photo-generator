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