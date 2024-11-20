from flask import Flask, render_template
from analysis import Analysis
from input import Input
from task import Task
from criteria import Criteria
from review import Review
from access import Access
from report import Report
from about import About

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analysis")
def analysis():
    analysis = Analysis()
    return analysis.run()

@app.route("/input")
def input():
    input = Input()
    return input.run()

@app.route("/task")
def task():
    task = Task()
    return task.run()

@app.route("/criteria")
def criteria():
    criteria = Criteria()
    return criteria.run()

@app.route("/review")
def review():
    review = Review()
    return review.run()

@app.route("/access")
def access():
    access = Access()
    return access.run()

@app.route("/report")
def report():
    report = Report()
    return report.run()

@app.route("/about")
def about():
    about = About()
    return about.run()

if __name__ == "__main__":
    app.run()
