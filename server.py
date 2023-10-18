import requests
from flask import Flask, render_template

app = Flask(__name__)


res = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_post = res.json()
# first_blog = res[0]["title"]
# sec_blog = res[1]["title"]
# th_blog = res[2]["title"]
# blog = res[0]["subtitle"]
# blog1 = res[1]["subtitle"]
# blog2 = res[2]["subtitle"]


# @app.route("/")
# def home():
#     return render_template('index.html', first=first_blog, sec=sec_blog, third=th_blog, blog1=blog1, blog2=blog2, blog=blog)

@app.route("/")
def home():
    return render_template('index.html', posts=all_post)


@app.route("/read/<name>")
def bye(name):
    return f"hey {name}"


@app.route("/blog/<int:id>")
def blog(id):

    for blog in all_post:

        if blog["id"] == id:
            req = blog
            print(req)
    return render_template('post.html', post=req)


if __name__ == '__main__':
    app.run(debug=True)
