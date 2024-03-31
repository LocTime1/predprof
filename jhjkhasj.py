from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def getdate():
    return render_template("create_house.html")

@app.route("/housedone", methods=["POST", "GET"])
def create_house():
    date1 = request.form.get('lll')
    print(date1)
    """"""
    lst = [4, 5, [[1, 1, 0, 0 ,0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]], []]

    return render_template("create_house2.html", lst=lst, date1=date1)





if __name__ == '__main__':
    app.run(port=8080, debug=True)