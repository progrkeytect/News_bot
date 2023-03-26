from flask import Flask, render_template, request
app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["blockchain_articles"]
collection = db["articles"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    query = request.args.get("q")
    articles = list(collection.find({"title": {"$regex": query, "$options": "i"}}))
    return render_template("search.html", articles=articles)

if __name__ == "__main__":
    app.run()
