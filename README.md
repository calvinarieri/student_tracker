# follow_up_system

**Student Performance Tracker**

This Python application is designed to record, retrieve, and analyze student behavior and exam results, providing an average rating for each student.

**Features:**

- Record student behavior and exam scores
- Retrieve student information for analysis
- Calculate average rating based on behavior and results
- Command-line interface (CLI) for user interaction

**Requirements:**

This application requires the following Python packages:

*  **prompt_toolkit** (for user input in the CLI)
* Linux os / windows sub-system linux

**Installation:**

1. Clone this repository or download the project files.
2. Navigate to the project directory in your terminal.
3. Install the required packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

**Usage:**

1. Run the application from the `lib` directory using:

   ```bash
   python3 app.py
   ```

2. The application will present a CLI menu with options for adding, retrieving, and calculating student ratings. Follow the on-screen prompts to interact with the application.

**Example Usage:**

```
   Welcome CALVIN ARIERI,

   1. View results
   2. View ratings
   3. View misbehavior
   4. Exit

   Enter your choice: 1  


```
 # NB:
    The actual app may vary
**Data Storage:**

The application stores student data in a local database (e.g., `school.db`). You can customize the database name and location by modifying the relevant code in the `app.py` script.

**Future implemantation:**
* Expand the table to accommodate more information. 
* Add emailing and notification incase of changes.
* Have an external database can be accessed by other applications. 
* Come up with a backend
and front end for the same.

**Contribution:**

We welcome contributions to this project! Feel free to fork the repository, make improvements, and submit pull requests.

**License:**

This project is licenced unde Apache 2.0.



