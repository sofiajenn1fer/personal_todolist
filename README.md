
# To-Do List Web Application

## Project Overview

This is a simple **To-Do List Web Application** built using **Flask** (a Python web framework) and **SQLite** as the database. The app allows users to add, edit, and delete tasks, set priorities, and assign due dates. Overdue tasks are highlighted in red, and users can mark tasks as complete. The application has a modern design with a gradient background, transparent task containers, and uses **Bootstrap** for responsive styling.

## Features

- **Add new tasks** with a description, priority, and due date.
- **Edit existing tasks** to update the task description, priority, or due date.
- **Mark tasks as complete**.
- **Delete tasks**.
- **Sort tasks** by priority and due date.
- **Highlight overdue tasks** in red with an overdue message.
- **Responsive design** using Bootstrap, with a clean, modern interface.

## Technologies Used

- **Python (Flask)**: Back-end web framework.
- **SQLite**: Lightweight database for storing tasks.
- **HTML/CSS/Bootstrap**: Front-end design and styling.
- **Jinja2**: Templating engine for dynamic content rendering.
  
## Installation

### Prerequisites

Ensure you have the following installed on your machine:

- **Python 3.x**: [Download and install Python](https://www.python.org/downloads/)
- **pip** (Python package manager): Comes with Python 3.x.

### Step-by-Step Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/todo-list-flask.git
   cd todo-list-flask
   ```

2. **Create a Virtual Environment (Optional but recommended)**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scriptsctivate
   ```

3. **Install Dependencies**:

   Install the required Python packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt` file, create one and add these dependencies:

   ```txt
   Flask==1.1.2
   ```
   
4. **Run the Application**:

   Run the Flask app locally:

   ```bash
   python app.py
   ```

   After running, open your browser and navigate to `http://127.0.0.1:5000/`.

5. **Database Setup**:

   The app will automatically create an SQLite database (`todo.db`) when you first run the app. If you need to update the database (e.g., add columns for `priority` and `due_date`), you can use the provided `update_db()` function.

## Usage

1. **Add a New Task**:
   - Fill out the task description, choose the priority (High, Medium, Low), and set a due date. Click "Add Task" to add the task to the list.
   
2. **View Tasks**:
   - The tasks will be displayed in a list. Overdue tasks are highlighted in red and marked with an overdue message.

3. **Edit or Delete a Task**:
   - You can click the "Edit" button to update the task or "Delete" to remove it from the list.

4. **Mark Tasks as Complete**:
   - Once a task is completed, you can click the "Mark Complete" button to mark it as finished.

## Screenshots

### Home Page (To-Do List)
![Home Page](./screenshots/home-page.png)

### Adding a Task
![Adding Task](./screenshots/add-task.png)

### Task List with Overdue Tasks
![Task List](./screenshots/task-list.png)

## Customization

### 1. **Changing the Background**:
   The app uses a gradient background. You can replace it with a background image or change the gradient colors in the CSS file. Modify the `body` style in the `index.html` file:

   ```css
   body {
       background: linear-gradient(to right, #6a11cb, #2575fc);
   }
   ```

### 2. **Task Sorting**:
   Tasks are sorted first by overdue status, then by priority, and finally by due date. You can adjust the SQL query in the `index` route in `app.py` to customize sorting.

### 3. **Styling**:
   Bootstrap is used for styling. You can customize the appearance by modifying the Bootstrap classes or adding additional CSS rules.

## Future Enhancements

- **User Authentication**: Allow users to sign in and manage their own tasks.
- **Email Notifications**: Send reminders for upcoming and overdue tasks.
- **Tagging and Categorization**: Add support for task tags or categories to organize tasks more efficiently.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
