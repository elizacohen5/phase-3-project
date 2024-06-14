import sqlite3

CONN = sqlite3.connect('student_stories.db')
CURSOR = CONN.cursor()
