from flask import Flask,render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    "id": 1,
    "title": "Data Analyst",
    "Location": "Valley Stream, NY",
    "Salary": "120K USD"
  },
 {
    "id": 1,
    "title": "Java Developer",
    "Location": "Remote",
    "Salary": "120K USD"
  },
 {
    "id": 1,
    "title": "Front End Developer",
    "Location": "Valley Stream, NY",
    "Salary": "120K USD"
  },
  {
    "id": 1,
    "title": "Database Admin",
    "Location": "Valley Stream, NY",
    "Salary": "120K USD"
  }
]

@app.route("/")
def hello_world():
  return render_template("home.html",jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  

if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)
