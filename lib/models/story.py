from .__init__ import CURSOR, CONN

class Story:

    def __init__(self, id, story):
        self.student_id = id
        self.story = story
    
    def __repr__(self):
        return f"story {self.student} {self.story}"
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Story instances """
        sql = """
            CREATE TABLE IF NOT EXISTS story (
            id INTEGER PRIMARY KEY,
            student_id TEXT,
            story TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Story instances """
        sql = """
            DROP TABLE IF EXISTS story;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        """ Insert a new row with the student id, and story values of the current Story instance.
        Update object id attribute using the primary key value of new row.
        """
        sql = """
            INSERT INTO story (student_id, story)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.student_id, self.story))
        CONN.commit()

        self.id = CURSOR.lastrowid
    
    @classmethod
    def create(cls, student_id, story):
        story = cls(student_id, story)
        story.save()
        return story
    
    @classmethod
    def get_student_story(cls, student_name):

        sql = """
            SELECT story
            FROM story
            JOIN students
            ON story.student_id = students.id
            WHERE LOWER(students.name) = ?
        """
        row = CURSOR.execute(sql, (student_name,)).fetchone()
        CONN.commit()
        print(row[0])