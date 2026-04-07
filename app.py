from flask import Flask, render_template, jsonify
import simulation

app = Flask(__name__)

simulation.init_cluster()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def data():

    pods = simulation.simulate_step()

    total_cpu = sum(p["cpu"] for p in pods)
    total_mem = sum(p["mem"] for p in pods)

    anomalies = len([p for p in pods if p["status"]=="ANOMALY"])
    crashes = len([p for p in pods if p["status"]=="CRASHED"])

    return jsonify({
        "pods": pods,
        "cpu": total_cpu,
        "mem": total_mem,
        "anomalies": anomalies,
        "crashes": crashes
    })

if __name__ == "__main__":
    app.run(debug=True)
