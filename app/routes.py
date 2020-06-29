#!/usr/bin/env python
# -*- coding: utf-8 -*-
# r3nt0n

from app import app
from flask import render_template, redirect, url_for, request

from app.monopoly import Monopoly

monopoly = Monopoly()

@app.route('/', methods=['GET', 'POST'])
@app.route('/index/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        return redirect(url_for("game"))


@app.route('/game/', methods=['GET', 'POST'])
def game():

    if request.method == 'POST':
        monopoly.move()

    places = monopoly.places
    position = monopoly.position
    result = monopoly.result

    return render_template("game.html", places=places, position=position, result=result)
