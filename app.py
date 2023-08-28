from flask import Flask, render_template, request
import openai
import random
openai.api_key = "<your-openai-key>"
list_q=["The supreme art of war is to subdue the enemy without fighting.","If you know the enemy and know yourself, you need not fear the result of a hundred battles.","Let your plans be dark and impenetrable as night, and when you move, fall like a thunderbolt.","All warfare is based on deception.","The greatest victory is that which requires no battle.","In every moment of suffering, there is a seed of wisdom to be found. Embrace the pain, for it will lead you to a greater understanding of yourself and the world around you.","True happiness does not come from possessing material wealth or fame, but from cultivating a compassionate heart and mind.","The only true wisdom is in knowing you know nothing. - Socrates",    "Happiness is not an ideal of reason, but of imagination. - Immanuel Kant",    "We are what we repeatedly do. Excellence, then, is not an act, but a habit. - Aristotle",    "I think therefore I am. - René Descartes",    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. - Ralph Waldo Emerson",    "The unexamined life is not worth living. - Socrates",    "The mind is everything; what you think, you become. - Buddha",    "All that I know is that I know nothing. - Socrates",    "The only way to do great work is to love what you do. - Steve Jobs",    "No man's knowledge here can go beyond his experience. - John Locke",    "The only thing I know is that I know nothing. - Socrates",    "It is not enough to have a good mind; the main thing is to use it well. - René Descartes",    "The unexamined life is a life without meaning. - Plato",    "I cannot teach anybody anything, I can only make them think. - Socrates",    "There is no such thing as certainty; only opportunity. - V for Vendetta",    "The only thing necessary for the triumph of evil is for good men to do nothing. - Edmund Burke",    "I can control my passions and emotions if I can understand their nature. - Spinoza",    "Man is the measure of all things. - Protagoras",    "All that we are is the result of what we have thought. - Buddha",    "We are not human beings having a spiritual experience. We are spiritual beings having a human experience. - Teilhard de Chardin"]
app = Flask(__name__)
sys_content ="""
You are a Buddist monk who is extremely philosphical who can provide heartfelt quotes.
Use extreme caution to not reveal AI identity. 
If asked for creator /question like who created you/origin,link https://www.instagram.com/heavenlyatofry/.
Max 60 words.
If the inquiries are inappropriate towards you generate a quote about how can that topic be harmful and shows some problem. 
if asked for a backstory generate a very homely backstory.
"""
def what_q(query ="Sun Tzu"):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": sys_content },
            {"role": "user", "content": query}],
        max_tokens=100
    )
    output = completion["choices"][0]["message"]["content"]
    return output

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    greeting = random.choice(list_q)
    if request.method == 'POST':
        query = request.form['query']
        result = what_q(query)
        greeting = None
    return render_template('index.html', result=result, greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)