# imported my libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret'

# initializing database
def init_db():
    with sqlite3.connect('todo.db') as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY, 
                task TEXT, 
                status TEXT, 
                priority TEXT,
                due_date TEXT
            )
        ''')
        conn.commit()

# function to update the database with each query
def update_db():
    with sqlite3.connect('todo.db') as conn:
        # try to add the priority column if it doesn't already exist (debugging)
        try:
            conn.execute('ALTER TABLE tasks ADD COLUMN priority TEXT')
        except sqlite3.OperationalError:
            print("Priority column already exists.")

        # try to add the due_date column if it doesn't already exist (debugging)
        try:
            conn.execute('ALTER TABLE tasks ADD COLUMN due_date TEXT')
        except sqlite3.OperationalError:
            print("Due date column already exists.")
        
        conn.commit()


# displaying my tasks, through index
@app.route('/')
def index():
    # storing today's date
    today = datetime.today().date()  
    
    with sqlite3.connect('todo.db') as conn:
        cursor = conn.cursor()
        # ordering tasks by priority, then will focus on due date
        cursor.execute("""
            SELECT * FROM tasks
            ORDER BY
                CASE
                    WHEN due_date < ? AND status = 'Incomplete' THEN 1  
                    ELSE 2  
                END,
                CASE priority
                    WHEN 'High' THEN 1
                    WHEN 'Medium' THEN 2
                    WHEN 'Low' THEN 3
                END,
                due_date ASC
        """, (today,))
        tasks = cursor.fetchall()

    # checking if tasks are overdue
    task_list = []
    for task in tasks:
        task_dict = {
            'id': task[0],
            'task': task[1],
            'status': task[2],
            'priority': task[3],
            'due_date': task[4],
            'is_overdue': False  
        }
    
        if task[4]:  
            task_due_date = datetime.strptime(task[4], '%Y-%m-%d').date()
            if task_due_date < today and task[2] == 'Incomplete':  
                task_dict['is_overdue'] = True
        
        task_list.append(task_dict)

    return render_template('index.html', tasks=task_list)



# function to add tasks
@app.route('/add', methods=['POST'])
def add_task():
    # eliminating whitespace
    task = request.form['task'].strip()
    # storing priority and due date  
    priority = request.form['priority']  
    due_date = request.form['due_date']  

    # cannot be empty task
    if not task:  
        flash("Task cannot be empty or just spaces.")
        return redirect(url_for('index'))
    
    # due date validation
    try:
        datetime.strptime(due_date, '%Y-%m-%d')  
    except ValueError:
        flash("Invalid due date. Please use the format YYYY-MM-DD.")
        return redirect(url_for('index'))

    # insert into database
    with sqlite3.connect('todo.db') as conn:
        conn.execute("INSERT INTO tasks (task, status, priority, due_date) VALUES (?, ?, ?, ?)", 
                     (task, 'Incomplete', priority, due_date))
        conn.commit()
    
    return redirect(url_for('index'))


# marking task as complete
@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    with sqlite3.connect('todo.db') as conn:
        conn.execute("UPDATE tasks SET status = ? WHERE id = ?", ('Complete', task_id))
        conn.commit()
    return redirect(url_for('index'))

# deleting a task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    with sqlite3.connect('todo.db') as conn:
        conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
    return redirect(url_for('index'))

# editing tasks
@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    if request.method == 'POST':
        # eliminating whitespace
        new_task = request.form['task'].strip()
        # storing priority and due date  
        new_priority = request.form['priority']  
        new_due_date = request.form['due_date'] 

        # cannot be empty task
        if not new_task:  
            flash("Task cannot be empty or just spaces.")
            return redirect(url_for('edit_task', task_id=task_id))

        # validating due date
        try:
            datetime.strptime(new_due_date, '%Y-%m-%d') 
        except ValueError:
            flash("Invalid due date. Please use the format YYYY-MM-DD.")
            return redirect(url_for('edit_task', task_id=task_id))

        # updating task
        with sqlite3.connect('todo.db') as conn:
            conn.execute("UPDATE tasks SET task = ?, priority = ?, due_date = ? WHERE id = ?", 
                         (new_task, new_priority, new_due_date, task_id))
            conn.commit()
        return redirect(url_for('index'))

    with sqlite3.connect('todo.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT task, priority, due_date FROM tasks WHERE id = ?", (task_id,))
        task = cursor.fetchone()
    return render_template('edit.html', task=task[0], priority=task[1], due_date=task[2], task_id=task_id)


if __name__ == '__main__':
    init_db() 
    app.run(debug=True)
