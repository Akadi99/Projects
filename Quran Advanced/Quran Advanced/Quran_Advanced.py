import speech_recognition as sr

# Define the expected Quranic chapter (Surah Al-Fatiha in this example)
expected_surah = "بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ"

# Initialize the recognizer
recognizer = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Please recite Surah Al-Fatiha:")
    audio = recognizer.listen(source)

# Recognize the speech in Arabic
try:
    recognized_text = recognizer.recognize_google(audio, language="ar-SA")
    print("You recited:", recognized_text)

    # Check if the recognized Arabic text matches the expected Surah
    if recognized_text == expected_surah:
        print("Recitation is correct!")
    else:
        print("Recitation is incorrect. Please try again.")

except sr.UnknownValueError:
    print("Sorry, I couldn't understand your recitation.")
except sr.RequestError as e:
    print(f"Could not request results; {e}")

