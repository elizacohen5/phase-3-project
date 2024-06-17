from .__init__ import CURSOR, CONN

class Story:

    def __init__(self, student, story):
        self.student_id = student.id
        self.story = story
        # self.adj = adj1
        # self.ridiculous_event = ridiculous_event
        # self.fictional_villain = fictional_villain
        # self.beverage = beverage
        # self.emotion = emotion
        # self.celebrity = celebrity
        # self.topic = topic
        # self.animal = animal
        # self.stimulant = stimulant 
        # self.food = food
        # self.emotional_turmoil = emotional_turmoil
        # self.tech_trend = tech_trend
        # self.tv_show = tv_show
        # self.video_game = video_game
        # self.error = error
        # self.end_of_day_activity = end_of_day_activity
    
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
    