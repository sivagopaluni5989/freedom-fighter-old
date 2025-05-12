from flask import Flask, render_template

app = Flask(__name__)

# Hindu National Heroes Data
heroes = [
    {
        "name": "Chandra Shekar Azad",
        "image": "Azad.jpg",
        "description": "Aggressive fighter  of the Indian independence movement through Unconditional-violence."
    },
    {
        "name": "Bhagat Singh",
        "image": "bhagat.jpg",
        "description": "Young revolutionary who became a symbol of heroism in the Indian freedom struggle."
    },
    {
        "name": "S Vallabhbhai Patel",
        "image": "patel.jpg",
        "description": "The Iron Man of India who united the princely states into a single nation."
    },

        ]


@app.route("/")
def index():
    return render_template("index.html", heroes=heroes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

