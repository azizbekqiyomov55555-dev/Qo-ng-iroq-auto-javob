from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def home():
    return "Azizbek Voice Bot ishlayapti!"

@app.route("/voice", methods=["GET", "POST"])
def voice():
    twiml = """
    <Response>
        <Say voice="alice" language="en-US">
            Assalomu alaykum. Azizbek bilan bog'lab beraman siz.
            Iltimos, kutib turing.
        </Say>

        <Pause length="5"/>

        <Say voice="alice" language="en-US">
            Kechirasiz. Hozirgi paytda Azizbek band edilar.
            Keyinroq qo'ng'iroq qiling.
        </Say>

        <Hangup/>
    </Response>
    """
    return Response(twiml, mimetype="text/xml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
