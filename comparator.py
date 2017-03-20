import base64
import os
from flask import Flask, render_template, render_template_string
from PIL import Image

app = Flask(__name__)

IMG_ROOT = "/Volumes/Samsung USB/nv images/out"
TXT_ROOT = "out"

@app.route("/")
def index():
    return "hi"

@app.route("/<imageNum>")
def page(imageNum):
    imgUrl = "https://earlyaudio.s3.amazonaws.com/nv/{}.png".format(imageNum)

    textPath = "{}/{}.txt".format(TXT_ROOT, imageNum)

    with open(textPath) as f:
        text = f.read()

    nextPage = str(int(imageNum) + 1).zfill(4)
    prevPage = str(int(imageNum) - 1).zfill(4) if int(imageNum) >= 2 else None

    return render_template("page.html", text=text, imgUrl=imgUrl, nextPage=nextPage, prevPage=prevPage)


app.run()