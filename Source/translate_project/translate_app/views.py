from django.shortcuts import render
from googletrans import Translator
from PIL import Image
import pytesseract
import os
import tempfile

def text_translation_view(request):
    if request.method == 'POST':
        translator = Translator()
        target_language = request.POST.get('target_language', 'en')  # Default to English

        if 'speech_text' in request.POST:  # Text translation from user input
            text = request.POST.get('speech_text', '').strip()
            if text:
                translated_text = translator.translate(text, dest=target_language).text
            else:
                translated_text = "No text provided for translation."
            return render(request, 'transt/tran.html', {'translated_text': translated_text})

        elif 'image_file' in request.FILES:  # Image text extraction and translation
            image_file = request.FILES['image_file']
            
            # Save the uploaded image to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_img:
                temp_img.write(image_file.read())
                temp_img_path = temp_img.name

            try:
                # Extract text from image
                extracted_text = pytesseract.image_to_string(Image.open(temp_img_path)).strip()

                if extracted_text:
                    translated_text = translator.translate(extracted_text, dest=target_language).text
                else:
                    translated_text = "No readable text found in the image."

            except Exception as e:
                translated_text = f"Error processing image: {str(e)}"
            finally:
                os.remove(temp_img_path)  # Clean up the temporary image file

            return render(request, 'translate_app/translation.html', {'translated_text': translated_text})

    return render(request, 'transt/tran.html')  # Default render for GET requests
