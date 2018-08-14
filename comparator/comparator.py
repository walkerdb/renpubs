import base64
import os
from flask import Flask, render_template, request, redirect, url_for, send_file
from PIL import Image

app = Flask(__name__, static_path="/static")

TXT_ROOT = "../input_output/data"

@app.route('/favicon.ico')
def favicon():
    return ""

@app.route("/")
def index():
    return "hi"

@app.route("/<image_num>", methods=["GET", "POST"])
def page(image_num):
    img_url = "https://earlyaudio.s3.amazonaws.com/nv/{}.png".format(image_num)
    text_path = "{}/{}.txt".format(TXT_ROOT, image_num)

    next_page = str(int(image_num) + 1).zfill(4)
    prev_page = str(int(image_num) - 1).zfill(4) if int(image_num) >= 2 else None

    if request.method == "POST" and request.form.get("text"):
        with open(text_path, "w") as f:
            f.write(request.form.get("text").replace("\r\n", "\n"))

        return redirect(url_for("page", image_num=next_page))

    else:
        with open(text_path) as f:
            text = f.read()

        return render_template("page.html", text=text, imgUrl=img_url, nextPage=next_page, prevPage=prev_page, currentPage=image_num)


@app.route("/text/<image_num>", methods=["GET"])
def text(image_num):
    text_path = "{}/{}.txt".format(TXT_ROOT, image_num)

    with open(text_path) as f:
        text = f.read()
        print(text)
        return text


@app.route("/img/<image_num>.png", methods=["GET"])
def img(image_num):
    path_template = "/Volumes/Samsung USB/crops/{}.png"
    img_path = path_template.format(image_num)

    return send_file(img_path)

app.run()
