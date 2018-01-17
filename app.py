#!/usr/bin/env python3
import random
from flask import Flask, render_template

from models import genres, subjects, outcomes


app = Flask(__name__)


@app.route('/')
def home():
    amount = random.randint(1, 10) * 10
    return render_template('home.html',
        amount=amount,
        number=random.randint(1, amount),
        genre=genres.get(),
        subject=subjects.get(),
        outcome=outcomes.get()
    )


if __name__ == '__main__':
    app.run()
