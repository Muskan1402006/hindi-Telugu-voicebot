from flask import Flask, render_template, request, jsonify
import pyttsx3
from datetime import datetime

app = Flask(__name__)

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_reply(text):
    text = text.lower()

    if "namaste" in text or "नमस्ते" in text:
        return "Namaste Muskan garu, mee tho maatladadam santosham."

    elif "naa peru" in text or "मेरा नाम" in text:
        return "Mee peru Muskan ani ardham ayyindi."

    elif "ela unnaru" in text or "कैसे" in text:
        return "Nenu bagunnanu, meeru ela unnaru?"

    elif "assignment" in text or "असाइनमेंट" in text:
        return "Mee assignment chala baga undi."

    elif "dhanyavaadalu" in text or "धन्यवाद" in text:
        return "Mee ku kuda dhanyavaadalu."

    else:
        return "Nenu mee maatlu vinnanu."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/talk", methods=["POST"])
def talk():
    data = request.get_json()
    text = data.get("speech", "")

    reply = get_reply(text)
    speak(reply)

    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()}\nUser: {text}\nBot: {reply}\n\n")

    return jsonify({"bot": reply})

if __name__ == "__main__":
    app.run(debug=False)