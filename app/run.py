from flask import Flask, request, render_template, url_for, redirect, abort
from lyrics_visualize import lv
import os


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def route_page():
    if request.method == 'GET':
        return render_template("index.html")

    if request.method == 'POST':
        artist = request.form.get('artist')
        title = request.form.get('title')

        try:
            if not os.path.exists('static/images/'+title+'.png'):
                lv.create(artist=artist, song=title)

            args = '?artist='+artist + '&title='+title
            return redirect('/create'+args)

        except:
            return render_template("no_lv.html", artist=artist, title=title)


@app.route('/create')
def create():
    try:
        title = request.args.get('title')
        artist = request.args.get('artist')

        folder = "images/" + title+".png"
        url = url_for('static', filename=folder)

        return render_template("image.html", artist=artist, title=title, url=url)

    except:
        return abort(404)


if __name__ == '__main__':
    app.run(debug=True)
