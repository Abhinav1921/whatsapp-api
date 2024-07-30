from flask import Flask

app = Flask(__name__)


@app.route("/whatmsg")
def whatsapp_msg():
    import pywhatkit as kit
    phonenumber = ("+918000499522")
    message = "Hello"
    kit.sendwhatmsg_instantly(phonenumber, message)
    return "message sent"


app.run()

