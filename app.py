from flask import Flask, render_template, request, redirect, url_for
import os
import google.generativeai as genai
from PIL import Image
from io import BytesIO
from gemini_vision_pro import gemini_vision
app = Flask(__name__)

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return redirect(request.url)
    file = request.files['image']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        image = Image.open(BytesIO(file.read()))
        genai.configure(api_key= gemini_vision)  
        model = genai.GenerativeModel('gemini-pro-vision')
        
        # Generate explanation for the image
        response_explanation = model.generate_content([
            image,
            "Please explain this image to me and give me the prompt to generate similar images in stable diffusion based on this image."
        ])
        explanation = response_explanation.candidates[0].content.parts[0].text
        
        # Render the template with the explanation variable
        return render_template('response.html', explanation=explanation)
    else:
        return 'Invalid file format'

if __name__ == '__main__':
    app.run()
