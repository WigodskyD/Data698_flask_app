#import plotly.graph_objs as go
#import pandas as pd
#import math
from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def page2_render():
    return render_template("page_grid.html")


@app.route('/data_story', methods=['GET', 'POST'])
def page3_render():
    return render_template("page_gridb.html")


@app.route('/models')
def page4_render():
    return render_template("page_gridc.html")


@app.route('/visualizations')
def page5_render():
    return render_template("page_gridd.html")
