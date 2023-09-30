
import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the microphone
microphone = sr.Microphone()

# Function to continuously listen and transcribe speech
def listen_and_transcribe():
    print("Listening... (say 'exit' to stop)")
    
    with microphone as source:
        while True:
            try:
                audio = recognizer.listen(source, timeout=10)
                text = recognizer.recognize_google(audio)
                print("You said:", text)
                
                if text.lower() == "exit":
                    break
            
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand your speech.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")

# Main function
def main():
    with microphone as source:
        print("Calibrating microphone... Please remain silent for a moment.")
        recognizer.adjust_for_ambient_noise(source, duration=5)
        print("Microphone calibrated.")
    
    listen_and_transcribe()

if __name__ == "__main__":
    main()
