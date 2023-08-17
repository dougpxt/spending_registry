<h1>Spending Registry</h1>
Simplify your expense tracking with the Spending Registry, a Python-based project that offers a user-friendly interface for managing your expenses. The project utilizes SQLite for data storage and retrieval, and it's built using the PySimpleGUI library for creating a graphical user interface.

<h2>Features</h2>
CRUD Functionality: Easily Create, Read, and Delete spending data entries. (no update func)
SQLite Integration: Utilizes an SQLite database for secure and efficient data storage.
PySimpleGUI Interface: Provides an intuitive and visually appealing user interface for seamless interaction.
Expense Insights: Gain insights into spending habits through visualized data trends.
Data Export: Export your expense data in a formatted TXT file for easy sharing and backup.
Usage
Installation: Make sure you have Python and SQLite installed. Clone this repository and navigate to the project directory.

Dependencies: Install the required dependencies using the following command:

Copy code
SQLite extensions needed
pip install PySimpleGUI
Run the Application: Execute the spendingRegFunc.py script to start the Spending Registry application.

Usage: Add, update, and delete spending entries using the intuitive interface. Export your data as a formatted TXT file for record-keeping.

<h2>Code Overview</h2>
<p bold>The code is organized into two main parts:</p>


spendingReg.py: The entry point of the application, where the GUI window and classes are defined/launched and the spendingRegFunc.py functionality is utilized.

spendingRegFunc.py: Contains the CRUD operations, SQLite database integration.
