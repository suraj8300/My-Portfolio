from flask import Flask, render_template, request

app = Flask(__name__)

def caesar(original_text, shift_amount, choice):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cypher_text = ""
    for i in original_text:
        if i not in alphabet:
            cypher_text += i
        else:
            if choice == "encrypt":
                cypher_text += alphabet[(alphabet.index(i) + shift_amount) % 26]
            elif choice == "decrypt":
                cypher_text += alphabet[(alphabet.index(i) - shift_amount) % 26]
    return cypher_text

@app.route('/', methods=["GET","POST"])
def home():
    result = ""
    if request.method == "POST":
        text = request.form["text"].lower()
        shift = int(request.form["shift"])
        choice = request.form["choice"]
        print(f"Received: text={text}, shift={shift}, choice={choice}")
        result = caesar(text, shift, choice)
    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
