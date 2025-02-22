import sqlite3


db_name = "quiz.db"
conn = None
cursor = None




def open():
   global conn, cursor
   conn = sqlite3.connect(db_name)
   cursor = conn.cursor()




def close():
   cursor.close()
   conn.close()




def do(query):
   cursor.execute(query)
   conn.commit()




def clear_db():
   ''' видаляє всі таблиці '''
   open()
   query = '''DROP TABLE IF EXISTS quiz_content'''
   do(query)
   query = '''DROP TABLE IF EXISTS question'''
   do(query)
   query = '''DROP TABLE IF EXISTS quiz'''
   do(query)
   close()




def show(table):
   query = 'SELECT * FROM ' + table
   open()
   cursor.execute(query)
   print(cursor.fetchall())
   close()




def show_tables():
   show('question')
   show('quiz')
   show('quiz_content')






# task 1: Створення таблиць та опис зв'язків між ними
def create():
   open()
   cursor.execute('''PRAGMA foreign_keys=on''')

   do('''CREATE TABLE IF NOT EXISTS question (id INTEGER PRIMARY KEY, question VARCHAR,answer VARCHAR, wrong1 VARCHAR, wrong2 VARCHAR, wrong3 VARCHAR)''')

   do('''CREATE TABLE IF NOT EXISTS quiz_content (id INTEGER PRIMARY KEY, quiz_id INTEGER, FOREIGN KEY (quiz_id) REFERENCES quiz (id), FOREIGN KEY (question_id) REFERENCES question (id) )''')
   close()



# task 2: Заповнення таблиць даними
def add_questions():
   questions =[]



# task 3: Отримання тексту запитання та варіантів відповідей






def main():
   clear_db()
   create()
   add_questions()
   add_quiz()
   add_links()
   show_tables()
   # Виведення в консоль питання з id=3, id вікторини = 1
   print(get_question_after(3, 1))




if __name__ == "__main__":
   main()





