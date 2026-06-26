from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/analyze")
def analyze():
    return render_template(
        "analyze.html",
        words=None,
        sentences=None,
        reading_time=None,
        avg_words_per_sentence=None,
        difficulty=None,
        text=""
    )

@app.route("/process", methods=["POST"])
def process():
    text = request.form["article"]

    words = len(text.split())
    sentences = text.count(".") + text.count("!") + text.count("?")

    reading_time = max(1, round(words / 200))

    if sentences == 0:
        avg_words_per_sentence = words
    else:
        avg_words_per_sentence = round(words / sentences, 1)

    if avg_words_per_sentence <= 15:
        difficulty = "Easy"
    elif avg_words_per_sentence <= 25:
        difficulty = "Medium"
    else:
        difficulty = "Difficult"
    if difficulty == "Easy":
        message = "Your text is simple and comfortable to read."
    elif difficulty == "Medium":
        message = "Your text is slightly complex but readable."
    else:
        message = "Your text may be difficult for some readers."

    return render_template( 
        "analyze.html",
        words=words,
        sentences=sentences,
        reading_time=f"{reading_time} min",
        text=text,
        avg_words_per_sentence=avg_words_per_sentence,
        difficulty=difficulty,
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True)