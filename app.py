from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = []

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    tasks.append(data)
    return jsonify({"message": "Task added"}), 201

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        return jsonify({"message": "Task deleted"}), 200
    return jsonify({"message": "Task not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
