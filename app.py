from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    categories = ["Electronics", "Clothing", "Furniture"]
    sales = [1200, 800, 950]
    return render_template("index.html", categories=categories, sales=sales)

if __name__ == "__main__":
    app.run(debug=True)
