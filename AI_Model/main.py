from STT.STT import SpeechToTextListener
from TTS.DeepGram import AI_Speak
from TEXT.basedGPT import generate
from IMG.deepInfra_IMG import generate_img
if __name__ == "__main__":
    while True:

        listener = SpeechToTextListener(language="en-IN")  # You can specify the desired language here
        query = listener.listen()
        print(f"You: {query}")

        if "what"or"who"or"where"or"which"or"how" in query:
            
            conversation_history = [{"role": "user", "content": query}]
            response = generate(conversation_history)
            AI_Speak(response)
        elif "generate" in query:
            generate_img(query)
            AI_Speak("Your is image is generated")
        elif "Your voice is just like a human" in query:
            AI_Speak("Yes I am built with latest AI models")
        else:
            AI_Speak("Thank You")