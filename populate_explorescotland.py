import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'explore_scotland_project')

import django
django.setup()
from explorescotland.models import QuizQuestion, Level

def populate():

    quiz_questions = [
        {"question_id": 1, "question": "What is Glasgow's reputation?", "correctAnswer": "Being an industrial city", "incorrectAnswer1": "Having unique architecture",
         "incorrectAnswer2": "Having huge pockets of greenery", "incorrectAnswer3": "Being among the most important cities in the British Empire", "level": "1"},
        {"question_id": 2, "question": "What is the good used as a major export to England in the late 17th century?", "correctAnswer": "linen", "incorrectAnswer1": "cotton",
         "incorrectAnswer2": "velvet", "incorrectAnswer3": "silk", "level": "1"},
        {"question_id": 3, "question": "Which is the capital of contemporary music in Scotland?", "correctAnswer": "Glasgow", "incorrectAnswer1": "Edinburgh",
         "incorrectAnswer2": "Aberdeen", "incorrectAnswer3": "Stirling", "level": "1"},
        {"question_id": 4, "question": "Which river is the natural location for fishing in Glasgow?", "correctAnswer": "Clyde", "incorrectAnswer1": "Kelvin",
         "incorrectAnswer2": "North Calder Water", "incorrectAnswer3": "Lavern Water", "level": "1"},
        {"question_id": 5, "question": "Who established Glasgow?", "correctAnswer": "St Mungo", "incorrectAnswer1": "Lord Kelvin",
         "incorrectAnswer2": "Queen Mary", "incorrectAnswer3": "Mackintosh", "level": "1"},
        {"question_id": 6, "question": "Which famous book was written in Edinburgh's cafes?", "correctAnswer": "Harry Potter", "incorrectAnswer1": "Hukleberry Finn",
         "incorrectAnswer2": "Animal farm", "incorrectAnswer3": "White Fang", "level": "1"},
        {"question_id": 7, "question": "Which magical creature can be found in Edinburgh?", "correctAnswer": "Unicorn", "incorrectAnswer1": "Dragon",
         "incorrectAnswer2": "Elf", "incorrectAnswer3": "Goblin", "level": "1"},
        {"question_id": 8, "question": "Which sweet can be found in Edinburgh?", "correctAnswer": "Nessie Poo", "incorrectAnswer1": "Loch Ness Poo",
         "incorrectAnswer2": "Highland Poo", "incorrectAnswer3": "Harry Potter Poo", "level": "1"},
        {"question_id": 9, "question": "Who was the founder of Edinburgh", "correctAnswer": "King David 1", "incorrectAnswer1": "Joseph Black",
         "incorrectAnswer2": "Adam Smith", "incorrectAnswer3": "Duke of Argyle", "level": "1"},
        {"question_id": 10, "question": "In which year was Edinburgh established?", "correctAnswer": "1130", "incorrectAnswer1": "1230",
         "incorrectAnswer2": "2018", "incorrectAnswer3": "230", "level": "1"},
        {"question_id": 11, "question": "Which is the legendary Loch Ness Monster?", "correctAnswer": "Nessie", "incorrectAnswer1": "Kraken",
         "incorrectAnswer2": "Fachen", "incorrectAnswer3": "Kelpie", "level": "2"},
        {"question_id": 12, "question": "Who is the first to see Nessie according to the oldest legend?", "correctAnswer": "St. Columbia", "incorrectAnswer1": "Marco Polo",
         "incorrectAnswer2": "Christopher Columbus", "incorrectAnswer3": "Fernando Magellan ", "level": "2"},
        {"question_id": 13, "question": "Which castle is located on the edge of Loch Ness?", "correctAnswer": "Urquhart Castle", "incorrectAnswer1": "Dunnottar Castle",
         "incorrectAnswer2": "Glamis Castle", "incorrectAnswer3": "Tantallon Castle", "level": "2"},
        {"question_id": 14, "question": "What does it mean if you hear a bag piper piping?", "correctAnswer": "He evokes the ghosts of the clans past", "incorrectAnswer1": "He is calling Nessie",
         "incorrectAnswer2": "He is making Nessie to fall asleep", "incorrectAnswer3": "He is calling his clan", "level": "2"},
        {"question_id": 15, "question": "What happened when St. Columba told Nessie to drop the guy?", "correctAnswer": "She obeyed", "incorrectAnswer1": "She ate him",
         "incorrectAnswer2": "She laughed", "incorrectAnswer3": "She swam away", "level": "2"},
        {"question_id": 16, "question": "Which ship was built in Dundee in 1901?", "correctAnswer": "Discovery", "incorrectAnswer1": "Creature",
         "incorrectAnswer2": "Mistery", "incorrectAnswer3": "Conquer", "level": "2"},
        {"question_id": 17, "question": "Dundee is in which position based on its size in Scotland?", "correctAnswer": "4th", "incorrectAnswer1": "2nd",
         "incorrectAnswer2": "1st", "incorrectAnswer3": "5th", "level": "2"},
        {"question_id": 18, "question": "What is the meaning of Dundee in Gaelic?", "correctAnswer": "Fire", "incorrectAnswer1": "Rain",
         "incorrectAnswer2": "Snow", "incorrectAnswer3": "Storm", "level": "2"},
        {"question_id": 19, "question": "In which century the famous Barry Mills was built?", "correctAnswer": "19th century", "incorrectAnswer1": "18th century",
         "incorrectAnswer2": "20th century", "incorrectAnswer3": "16th century", "level": "2"},
        {"question_id": 20, "question": "What did Janet Keiller invent?", "correctAnswer": "Jam", "incorrectAnswer1": "Whale oil",
         "incorrectAnswer2": "jute", "incorrectAnswer3": "sugar", "level": "2"},
        {"question_id": 21, "question": "How is Aberdeen known as?", "correctAnswer": "The Granite City", "incorrectAnswer1": "The Stone City",
         "incorrectAnswer2": "The Iron City", "incorrectAnswer3": "The Cotton City", "level": "3"},
        {"question_id": 22, "question": "Aberdeen is also famous as a ###### capital of the world. In which industry?", "correctAnswer": "oil/ energy", "incorrectAnswer1": "whales",
         "incorrectAnswer2": "fish", "incorrectAnswer3": "coals", "level": "3"},
        {"question_id": 23, "question": "Which is the most famous festival in Aberdeen?", "correctAnswer": "International Youth Festival", "incorrectAnswer1": "Gringe Festival",
         "incorrectAnswer2": "Lights Festival", "incorrectAnswer3": "Christmas Festival", "level": "3"},
        {"question_id": 24, "question": "Who burned the city in 1336?", "correctAnswer": "Edward III of England", "incorrectAnswer1": "Edward I of England",
         "incorrectAnswer2": "Edward II of England", "incorrectAnswer3": "Edward IV of England", "level": "3"},
        {"question_id": 26, "question": "Stirling Bridge and Bannockburn are famous with:", "correctAnswer": "historical battles", "incorrectAnswer1": "music concerts",
         "incorrectAnswer2": "their architecture", "incorrectAnswer3": "nothing", "level": "3"},
        {"question_id": 25, "question": "What is the moto of the city?", "correctAnswer": "Bon accord (Good agreement)", "incorrectAnswer1": "To inspire and achieve",
         "incorrectAnswer2": "Natura Artis Magistra (Nature is the teacher of the art)", "incorrectAnswer3": "Semper Verum (Always true)", "level": "3"},
        {"question_id": 27, "question": "In 1297 William Wallace:", "correctAnswer": "won the battle at Stirling Bridge", "incorrectAnswer1": "won the battle at Bannockburn",
         "incorrectAnswer2": "lost the battle at Stirling Bridge", "incorrectAnswer3": "lost the battle at Bannockburn", "level": "3"},
        {"question_id": 28, "question": "Robert the Bruce, King of the Scots most famous battle was at:", "correctAnswer": "Bannockburn", "incorrectAnswer1": "Stirling Castle",
         "incorrectAnswer2": "Stirling Bridge", "incorrectAnswer3": "Wallace Monument", "level": "3"},
        {"question_id": 29, "question": "Which machine did Kind Edward I used to besiege the Stirling Castle?", "correctAnswer": "War Wolf", "incorrectAnswer1": "War MAchine",
         "incorrectAnswer2": "Big Wolf", "incorrectAnswer3": "Scary Wolf", "level": "3"},
        {"question_id": 30, "question": "For how long did the Scots and English fight during the Middle Ages?", "correctAnswer": "60", "incorrectAnswer1": "20",
         "incorrectAnswer2": "10", "incorrectAnswer3": "100", "level": "3"}]

    levels = [{"number": 1, "topic": "Glasgow", "content": "", "numOfQuestions": 5},
              {"number": 2, "topic": "Edinburgh", "content": "", "numOfQuestions": 5},
              {"number": 3, "topic": "Loch Ness", "content": "", "numOfQuestions": 5},
              {"number": 4, "topic": "Dundee", "content": "", "numOfQuestions": 5},
              {"number": 5, "topic": "Aberdeen", "content": "", "numOfQuestions": 5},
              {"number": 6, "topic": "Stirling", "content": "", "numOfQuestions": 5}]


    for level in levels.items():
        l = add_level(number, topic, content, numOfQuestions]) #TODO ne znam kakvo se sluchva tuk :D
        for q in quiz_questions:
            add_question(l, q["id"], q["question"], q["correctAnswer"], q["incorrectAnswer1"], q["incorrectAnswer2"], q["incorrectAnswer3"])

    for l in Level.objects.all():
        for q in QuizQuestion.objects.filter(level=l):
            print("- {0} - {1}".format(str(l), str(q)))


def add_level(number, topic, content, numOfQuestions):
    l = Level.objects.get_or_create(number=number, topic=topic)[0]
    l.content = content
    l.numOfQuestions = numOfQuestions
    l.save()
    return l



def add_question(id, question, correct, incorrect1, incorrect2, incorrect3):
   q = QuizQuestion.objects.get_or_create(question_id=id)[0]
   q.question = question
   q.correctAnswer = correct
   q.incorrectAnswer1 = incorrect1
   q.incorrectAnswer2 = incorrect2
   q.incorrectAnswer3 = incorrect3
   q.save()
   return q



 # Start execution here
if __name__ == '__main__':
        print("Starting Explore Scotland population script...")
        populate()
