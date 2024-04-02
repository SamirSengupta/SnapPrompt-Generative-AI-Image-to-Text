from google.generativeai import configure, GenerativeModel

SnAPI = 'YOUR API KEY HERE'

internal = "Please explain this image to me and give me the prompt to generate exactly similar images in stable diffusion based on this image, tell every minute detail which will help to generate the image very well"

configure(api_key=SnAPI)
snap = GenerativeModel('gemini-pro-vision')
