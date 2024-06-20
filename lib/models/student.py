from .__init__ import CURSOR, CONN

class Student:
    names = []
    def __init__(self, name, phase, program):
        self.name = name
        self.phase = phase
        self.program = program
        Student.names.append(name)

    def __repr__(self):
        return f"<Student {self.name} {self.phase} {self.program}>"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) < 25:
            self._name = name
        else:
            raise ValueError("Name must be a string less than 25 characters")
        
    @property
    def phase(self):
        return self._phase
    
    @phase.setter
    def phase(self, phase):
        if isinstance(phase, int) and 1<= phase <= 5:
            self._phase = phase
        else:
            raise ValueError("Phase must be an integer between 1-5")
        
    @property
    def program(self):
        return self._program
    
    @program.setter
    def program(self, program):
        if isinstance(program, str):
            if(program == "SE" or program == "DS"):
                self._program = program
        else:
            raise ValueError("Program must be 'SE' or 'DS")

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Student instances """
        sql = """
            CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            phase INTEGER,
            program TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Student instances """
        sql = """
            DROP TABLE IF EXISTS students;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name, phase, and program values of the current Student instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO students (name, phase, program)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.phase, self.program))
        CONN.commit()

        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, phase, program):
        student = cls(name, phase, program)
        student.save()
        return student
    
    @classmethod
    def get_students(cls):
        
        sql = """
            SELECT name
            FROM students
            """
        
        rows = CURSOR.execute(sql).fetchall()
        CONN.commit()
       
        for name in rows:
            print(name[0])
           
      