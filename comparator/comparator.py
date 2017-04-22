import base64
import os
from flask import Flask, render_template, request, redirect, url_for
from PIL import Image

app = Flask(__name__, static_path="/static")

TXT_ROOT = "../input_output/data"

@app.route("/")
def index():
    return "hi"

@app.route("/<imageNum>", methods=["GET", "POST"])
def page(imageNum):
    imgUrl = "https://earlyaudio.s3.amazonaws.com/nv/{}.png".format(imageNum)
    textPath = "{}/{}.txt".format(TXT_ROOT, imageNum)

    nextPage = str(int(imageNum) + 1).zfill(4)
    prevPage = str(int(imageNum) - 1).zfill(4) if int(imageNum) >= 2 else None

    if request.method == "POST" and request.form.get("text"):
        with open(textPath, "w") as f:
            f.write(request.form.get("text").replace("\r\n", "\n"))

        return redirect(url_for("page", imageNum=nextPage))

    else:
        with open(textPath) as f:
            text = f.read()

        return render_template("page.html", text=text, imgUrl=imgUrl, nextPage=nextPage, prevPage=prevPage, currentPage=imageNum)


app.run()