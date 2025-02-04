import PyPDF2
from gtts import gTTS

def extract_text_from_pdf(pdf_path):
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text

def text_to_audio(text, audio_path):
    tts = gTTS(text=text, lang='en')
    tts.save(audio_path)

def pdf_to_audio(pdf_path, audio_path):
    text = extract_text_from_pdf(pdf_path)
    text_to_audio(text, audio_path)

pdf_path = r'C:\january_2025\2025batch\projects\hyderabad.pdf'
audio_path = r'C:\january_2025\2025batch\projects\hyd.mp3'
pdf_to_audio(pdf_path, audio_path)
