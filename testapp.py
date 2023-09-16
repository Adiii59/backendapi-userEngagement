from flask import Flask, render_template, request
import requests
app = None
def create_app():
    app = Flask(__name__, template_folder = "templates")
    app.app_context().push()
    return app

app = create_app()


@app.route("/", methods = ["GET", "POST"])
def home():
    return render_template("testPage.html")


@app.route("/test/get", methods = ["GET", "POST"])
def getPage():
    output1 = ""
    if request.method == "POST":

        pid = request.form["plantid"]
        x = requests.get(f"https://vedicvaidya-backendapi.onrender.com/comments/{pid}")
        print(x)
        output1 = x.json()["comments"]

    return render_template("testPage.html", output1 = output1)

@app.route("/test/post", methods = ["GET", "POST"])
def postPage():
    output2 = ""
    if request.method == "POST":
        pid = request.form["plantid"]
        uid = request.form["userid"]
        comment = request.form["comment"]
        jsonVals = {"uid": uid, "comment": comment}
        x = requests.post(f"https://vedicvaidya-backendapi.onrender.com/comments/{pid}", json = jsonVals, headers = {"Content-type": "application/json"})
        output2 = x.json()["status"]
    
    return render_template("testPage.html", output2 = output2)





if __name__ == "__main__":
    print("Running")
    app.run(debug = True, port = 8080)