from flask import Flask, render_template, render_template_string

app = Flask(__name__)

IMG_ROOT = "/Volumes/Samsung USB/nv images/out"
TXT_ROOT = "out"

@app.route("/")
def index():
    return "hi"

@app.route("/4123")
def page():
    imageNum = "4123"

    img = "{}/IMG_{}_1L.jpg".format(IMG_ROOT, imageNum)
    with open("{}/IMG_{}_1L.txt".format(TXT_ROOT, imageNum)) as f:
        text = f.read()
        return render_template_string("<pre>{}</pre>".format(text))


app.run()