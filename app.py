from flask import Flask, render_template, redirect
import subprocess, os

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/run-agent")
def run_agent():
    subprocess.Popen(["python", "autogen_app.py"])
    return redirect("/")

@app.route("/open-md")
def open_folder():
    os.startfile(".")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
