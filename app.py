from flask import Flask, request, jsonify
from math import sqrt, pi

app = Flask(__name__)

@app.route("/calcul", methods=["GET"])
def calcul():
    figure = request.args.get("figure")
    if figure == "carre":
        cote = float(request.args.get("cote", 1))
        surface = cote * cote
        perimetre = 4 * cote
    elif figure == "rectangle":
        l = float(request.args.get("longueur", 1))
        L = float(request.args.get("largeur", 1))
        surface = l * L
        perimetre = 2 * (l + L)
    elif figure == "triangle":
        base = float(request.args.get("base", 1))
        h = float(request.args.get("hauteur", 1))
        hypo = sqrt(base**2 + h**2)
        surface = (base * h) / 2
        perimetre = base + h + hypo
    elif figure == "cercle":
        r = float(request.args.get("rayon", 1))
        surface = pi * r**2
        perimetre = 2 * pi * r
    else:
        return jsonify({"error": "Figure inconnue"}), 400

    return jsonify({
        "figure": figure,
        "surface": surface,
        "perimetre": perimetre
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
