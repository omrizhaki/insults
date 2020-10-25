from flask import Flask, render_template, request
import requests

app = Flask(__name__)

languages_dict = {'English': 'en', 'Italian': 'it', 'French': 'fr', 'Spanish': 'es', 'Russian': 'ru', 'Swahili': 'sw', 'German': 'de', 'Greek': 'el', 'Chinese': 'cn'}


@app.route('/')
def hello_world():
    language_entered = request.args.get('language')
    if not language_entered:
        return render_template('index.j2')
    if language_entered not in languages_dict.keys():
        return render_template('index.j2', not_available="You idiot! I told you to choose a language from the list!")
    language = languages_dict[language_entered]
    resp = requests.get(f'https://evilinsult.com/generate_insult.php?lang={language}&type=json')
    if not resp:
        return render_template('index.j2')
    resp_json = resp.json()
    the_insult = resp_json['insult']
    return render_template(
        'index.j2',
        language=language_entered.title(),
        insult=the_insult,
        )


if __name__ == '__main__':
    app.run(threaded=True, port=5000)