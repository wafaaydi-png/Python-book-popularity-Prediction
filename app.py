from flask import Flask, render_template, request
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Charger le modèle
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "models", "book_popularity_model.pkl")
model = joblib.load(model_path)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # récupérer données formulaire
        book_title = request.form['book_title']
        price = float(request.form['price'])
        review_summary = request.form['review_summary']
        review_text = request.form['review_text']
        description = request.form['description']
        helpful_reviews = int(request.form['helpful_reviews'])
        total_reviews = int(request.form['total_reviews'])

        # dataframe
        data = pd.DataFrame({
            'book_title': [book_title],
            'price': [price],
            'review_summary': [review_summary],
            'review_text': [review_text],
            'description': [description],
            'helpful_reviews': [helpful_reviews],
            'total_reviews': [total_reviews]
        })

        # prédiction
        prediction = model.predict(data)[0]

        # convertir résultat
        if prediction == 1:
            result = "Popular"
        else:
            result = "Unpopular"

        return render_template(
            'index.html',
            prediction_text=result
        )

    except Exception as e:
        return render_template(
            'index.html',
            prediction_text="Erreur : " + str(e)
        )


if __name__ == "__main__":
    app.run(debug=True)