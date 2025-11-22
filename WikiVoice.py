import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning.")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon.")
    else:
        speak("Good evening.")

    greeting = "I am WikiVoice, your voice assistant. To search anything from Wikipedia, say the keyword followed by the word Wikipedia."
    print(greeting)
    speak(greeting)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print("User said: " + query + ".")
    except Exception as e:
        print("Please say that again...")
        return "None"
    
    return query

last_result = ""

wishMe()
while True:
    query = takecommand().lower()

    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "").strip()
        
        search_successful = False
        try:
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia,")
            print(results)
            speak(results)
            last_result = results
            search_successful = True
            
        except wikipedia.exceptions.PageError:
            speak("I am sorry, I could not find a Wikipedia page for that topic. Please try another search term.")
            print("Error: Wikipedia page not found for query: " + query + ".")
            last_result = ""
        except Exception as e:
            speak("An unexpected error occurred during the search.")
            print("Unexpected error: " + str(e) + ".")
            last_result = ""

        if search_successful:
            copy_prompt = "To copy this summary to a file, say 'Yes, copy'. Otherwise, say 'No, do not copy'."
            speak(copy_prompt)
            print(copy_prompt)
            
            copy_query = takecommand().lower()

            if 'yes copy' in copy_query:
                try:
                    with open("wiki_summary.txt", "a", encoding='utf-8') as ww:
                        ww.write(last_result + "\n\n")
                    speak("The summary has been written to the wiki summary file successfully.")
                except Exception as e:
                    speak("I encountered an error while trying to write the summary to the file. Please check file permissions.")
                    print("File writing error: " + str(e) + ".")
            elif 'no do not copy' in copy_query or 'no' in copy_query:
                pass 
            
        continue_prompt = "Do you want to search for anything more? Say 'Continue' to keep searching, or say 'Terminate' to end the session."
        speak(continue_prompt)
        print(continue_prompt)
        
        continue_query = takecommand().lower()

        if 'terminate' in continue_query:
            # Change 4: Remove "sir"
            speak("Thank you . Have a nice day.")
            exit()
        elif 'continue' in continue_query:
            continue
