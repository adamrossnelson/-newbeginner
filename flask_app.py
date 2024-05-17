# A very simple app for you to get started...
from flask import Flask, url_for, render_template
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = "123"

class SentimentForm(FlaskForm):
    text_to_analyze = TextAreaField('What text would you like to analyze?',
                                    description='Sensitive to punctuation and negation.',
                                    default='Having fun shout to #DataBesties',
                                    validators=[DataRequired()],
                                    render_kw={'rows': 10, 'cols':70})
    submit = SubmitField('Submit to Review Sentiment')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sentiment', methods=['GET', 'POST'])
def sentiment_page():

    nltk_scores = False
    form = SentimentForm()

    if form.validate_on_submit():

        text_to_analyze = form.text_to_analyze.data

        from nltk.sentiment.vader import SentimentIntensityAnalyzer
        sid = SentimentIntensityAnalyzer()
        nltk_scores = sid.polarity_scores(text_to_analyze)

    return render_template('sentiment.html', form=form,
                            nltk_scores=nltk_scores)

if __name__ == '__main__':
    app.run(debug=True)
