import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
import openai

# Import messagebox from tkinter
from tkinter import messagebox

# Set your OpenAI API key
openai.api_key = "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"

# Initialize the recognizer with Google Web Speech API
recognizer = sr.Recognizer()

# Initialize the translator
translator = Translator()

# Intoduction text
print("Welcome Abdulkadir. I am listening to you...")

# Create a function to send a user message to ChatGPT and get a response
def get_ai_response(user_message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message},
        ],
    )
    return response.choices[0].message["content"]

# Create a function to translate and respond
def translate_and_respond():
    try:
        # Get the selected input language from the combobox
        input_language = input_language_combobox.get()
        input_language_code = language_codes.get(input_language)

        # Check if the selected input language is supported
        if input_language_code is None:
            messagebox.showerror("Error", "Input language not supported")
            return

        # Detect speech and recognize text using Google Web Speech API
        with sr.Microphone() as source:
            print("listening...")
            audio = recognizer.listen(source)
        
        spoken_text = recognizer.recognize_google(audio)
        print(f"Spoken Text: {spoken_text}")

        # Get the selected output language from the combobox
        output_language = output_language_combobox.get()
        output_language_code = language_codes.get(output_language)

        # Check if the selected output language is supported
        if output_language_code is None:
            messagebox.showerror("Error", "Output language not supported")
            return

        # Translate to the selected output language
        translated = translator.translate(spoken_text, src=input_language_code, dest=output_language_code)
        translated_text = translated.text

        print(f"Translation to {output_language}: {translated_text}")

        # Check the response type (text, audio, or reply)
        response_type = response_type_combobox.get()

        if response_type == "Text only":
            response_text.config(text=f"Translation: {translated_text}")
        elif response_type == "Audio with Text":
            # Convert translated text to speech
            tts = gTTS(translated_text, lang=output_language_code)
            tts.save("translation.mp3")

            # Play the translated speech
            os.system("start translation.mp3")
        elif response_type == "A Conversation with Text":
            response_text.config(text=f"Translation: {translated_text}")

            # Get an AI response based on the translated text
            ai_response = get_ai_response(translated_text)
            response_text.config(text=f"AI Response: {ai_response}")

            # Convert AI response to speech
            ai_tts = gTTS(ai_response, lang=output_language_code)
            ai_tts.save("ai_response.mp3")

            # Play the AI response
            os.system("start ai_response.mp3")

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Create a function for the voice assistant's response
def assistant_response(response):
    print(f"Voice Assistant: {response}")
    response_text.config(text=response)
    tts = gTTS(response, lang="en")  # Voice assistant responds in English
    tts.save("assistant_response.mp3")
    os.system("start assistant_response.mp3")

# Create the main window
window = tk.Tk()
window.title("Speech Translation App")

language_codes = {
    "Arabic": "ar",
    "Bengali": "bn",
    "English": "en",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Spanish": "es",
}

# Create a label and a combobox to select the input language
input_language_label = tk.Label(window, text="Select Input Language:")
input_language_label.pack()
input_language_combobox = ttk.Combobox(window, values=list(language_codes.keys()))
input_language_combobox.set("English")
input_language_combobox.pack()

# Create a label and a combobox to select the target language
output_language_label = tk.Label(window, text="Select Ouput Language:")
output_language_label.pack()
output_language_combobox = ttk.Combobox(window, values=list(language_codes.keys()))
output_language_combobox.set("Arabic")
output_language_combobox.pack()

# Create a label and a combobox to select the response type
response_type_label = tk.Label(window, text="Select Response Type:")
response_type_label.pack()
response_type_combobox = ttk.Combobox(window, values=["Text only", "Audio with Text", "A Conversation with Text"])
response_type_combobox.set("Have AI reply with...")
response_type_combobox.pack()

# Create a button to trigger translation
translate_button = tk.Button(window, text="Translate", command=translate_and_respond)
translate_button.pack()

# Create a label to display the response
response_text = tk.Label(window, text="")
response_text.pack()

# Start the main loop
window.mainloop()