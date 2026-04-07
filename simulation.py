import random

NUM_PODS = 10
NUM_NODES = 3

pods = []
nodes = []

def init_cluster():

    global pods, nodes

    nodes = [{"id":i,"load":0} for i in range(NUM_NODES)]

    pods = []

    for i in range(NUM_PODS):

        pods.append({
            "id": i,
            "node": random.randint(0,NUM_NODES-1),
            "cpu": random.randint(10,40),
            "mem": random.randint(10,40),
            "status": "RUNNING"
        })


def simulate_step():

    global pods, nodes

    for p in pods:

        p["cpu"] = random.randint(0,100)
        p["mem"] = random.randint(0,100)

        if random.random() < 0.05:
            p["status"] = "CRASHED"

        elif p["cpu"] > 85 or p["mem"] > 85:
            p["status"] = "ANOMALY"

        else:
            p["status"] = "RUNNING"

    return pods
