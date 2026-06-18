from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

tasks = []

html = """
<h1>Todo App</h1>
<form method="POST">
    <input name="task" placeholder="Enter task">
    <button type="submit">Add</button>
</form>

<ul>
{% for t in tasks %}
  <li>{{t}}</li>
{% endfor %}
</ul>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
        return redirect("/")
    return render_template_string(html, tasks=tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
