⭐ WikiVoice Assistant ⭐

WikiVoice is a Python-based voice assistant designed to bridge the gap between users and information. It allows users to search Wikipedia using voice commands, reads the summaries aloud, and offers the functionality to log these summaries into a text file.


⭐Table of Contents-

Overview

Features

Technical Stack

Installation & Setup

Code Structure & Logic

Error Handling

Example Workflow


⭐Overview-

The primary purpose of WikiVoice is to assist individuals—specifically those with limb disabilities or those who prefer hands-free interaction—to access information quickly. It eliminates the need for typing, making knowledge acquisition accessible and fun.


⭐Features-

Voice Activation: Accepts audio input via microphone.

Smart Greeting: Greets the user based on the time of day.

Wikipedia Integration: Fetches summaries directly from Wikipedia.

Text-to-Speech (TTS): Reads results aloud using offline drivers.

File Logging: Option to save search results to wiki_summary.txt.

Robust Error Handling: Manages network errors, undefined pages, and ambiguous queries.


⭐Technical Stack-

Libraries Used

pyttsx3: An offline Text-to-Speech (TTS) library. Used to convert the string response from Wikipedia into audible speech.

speech_recognition: Used to capture audio from the microphone and convert it into text (Speech-to-Text) using the Google Web Speech API.

wikipedia: A Python wrapper for the Wikipedia API to fetch summaries.

datetime: A standard library used to fetch the current system time for context-aware greetings.


⭐Installation & Setup-

Clone the Repository:

git clone [https://github.com/Balajipathak301/WikiVoice.git](https://github.com/Balajipathak301/WikiVoice.git)
cd wikivoice


Install Dependencies:
You need to install the third-party libraries using pip:

pip install pyttsx3 wikipedia SpeechRecognition

Note: If you encounter errors with PyAudio (required by SpeechRecognition), you may need to install the PyAudio .whl file manually or use pip install pyaudio.

Run the Application:

python main.py


⭐Code Structure & Logic-

Initialization

engine = pyttsx3.init('sapi5')


We initialize the sapi5 engine (Microsoft Speech API). We explicitly set the voice property to voices[0].id (typically a male voice) to ensure consistent audio output.

Core Functions

1. speak(audio)

Input: Takes a string (audio).

Logic: Uses engine.say() to queue the text and engine.runAndWait() to block execution until speaking is complete.

2. wishMe()

Logic: Fetches datetime.datetime.now().hour.

Condition: * 0-12: "Good Morning"

12-18: "Good Afternoon"

Else: "Good Evening"

Purpose: Establishes a friendly user experience before asking for commands.

3. takecommand()

Setup: Initializes sr.Recognizer() and opens sr.Microphone().

Logic: * Sets pause_threshold = 1 to allow the user to take brief pauses while speaking.

Uses r.listen(source) to capture input.

Try/Except Block: * Try: Sends audio to r.recognize_google(language='en-IN').

Except: Catches audio errors and returns "None" string instead of crashing, prompting the user to speak again.

Main Loop Logic

The script runs inside a while True loop to ensure continuous service until the user says "Terminate".

Search Trigger: Checks if "wikipedia" is in the query.

Processing: Removes the word "wikipedia" from the string to isolate the topic.

File I/O: If the user confirms "Yes copy", it opens wiki_summary.txt in append mode ("a") and writes the result.


⭐Error Handling-

The system implements specific try-except blocks to prevent crashes:

wikipedia.exceptions.PageError: Triggered when a page doesn't exist (e.g., "Child labour in America"). The system informs the user the page wasn't found.

General Exception (Search): Catch-all for other Wikipedia errors, such as DisambiguationError (e.g., searching for "Tum").

File I/O Errors: Catches permission errors or path issues when trying to write to wiki_summary.txt.


⭐Example Workflow-

Scenario: User searches for "Pokemon Sun and Moon".

Input: User says "Pokemon Sun and Moon from Wikipedia".

Parsing: The system strips "from Wikipedia", leaving "Pokemon Sun and Moon".

Fetching: wikipedia.summary() retrieves the first 5 sentences about the Nintendo 3DS games.

Output: The assistant reads the summary about the game's release and features.

Copying: Assistant asks to copy. User says "Yes copy".

Result: The summary is appended to wiki_summary.txt and the loop continues.