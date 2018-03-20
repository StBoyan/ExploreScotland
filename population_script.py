import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'explore_scotland_project.settings')

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

    levels = {1: {"topic": "Glasgow", "content": "<h1>Glasgow</h1> <img src=\"https://peoplemakeglasgow.com/images/Clydeside1.jpg\">Glasgow has a reputation of being an industrial city, but also in the past used to be a  natural location for fishing.\
              The area around Glasgow has hosted communities for millennia, with the River Clyde providing a natural location for fishing.<br>\
              The Romans later built outposts in the area and, to keep separate from the Celtic and Pictish Caledonia, constructed the Antonine Wall.\
              Glasgow itself was founded by the Christian Missionary Saint Mungo in the 6th century.\
              He established a church on the Molendinar Burn, where the present Glasgow Cathedral stands, and in the following years Glasgow became a religious centre.\
              After 1860 the Clydeside shipyards specialised in steamships made of iron (after 1870, made of steel), which rapidly replaced the wooden sailing vessels of both the merchant fleets and the battle fleets of the world.\
              It became the world's pre-eminent shipbuilding centre.\
              In the late 17th century, Scottish linen was a major export to England. In 1680, the linen industry employed about 12,000 people in the Glasgow area, and the industry was heavily promoted by the government.\
              Thanks to a series of government acts and beneficial tax measures, by 1770, Glasgow had become the largest linen manufacturer in Britain. \
              Glasgow is the capital of contemporary music in Scotland, and has many venues and clubs such as the Barrowlands, Barfly and King Tut's Wah Wah Hut that promote new bands and DJs.\
              Additionally, it is home to some artists well known in the UK such as Franz Ferdinand and Belle & Sebastian.","numOfQuestions": 5},

              2: {"topic": "Edinburgh", "content": "From Edinburgh Castle down the Royal Mile to the Palace of Holyroodhouse, Edinburgh spans centuries of Scottish history, and continues to this day, as the capital of Scotland.\
              It's a city that captures the imagination.J.K. Rowling wrote the first Harry Potter books in Edinburgh cafes. Traveling around Edinburgh, cobbled streets and narrow lanes lead into unexpected places, where a dog, unicorns, Mary Queen of Scots, fairy cakes, and the Stone of Destiny await.\
              Look for unicorns – Unicorns are a central theme of the Royal Arms of Scotland. See how many unicorns you can find. There are plenty to see around the Palace of Holyroodhouse, also in Edinburgh Castle, in St. Giles' Cathedral, on the Mercat Cross.\
              In shops look for old fashioned sweets (also the gift shop at the National Museum of Scotland) – sour plooms, black and white humbugs, iron brew creams, fried eggs, saltire (blue and white like flag of Scotland), butterscotch, pan drops, Edinburgh rock.\
              There's also Haggis Poo – chocolate covered raisins, and Nessie Poo – toffee on the outside, a raisin inside.\
              The city has a very interesting history, but what is most important to know is that it was established by King David 1 in 1130 and as one of Scotland\'s earliest royal burghs, protected by his royal fortress, on the slope below the castle rock, which still is present and it is open for visitors. ","numOfQuestions": 5},

              3: {"topic": "Loch Ness", "content": "Loch Ness is magical place to visit. It is beautiful lake in the North part of Scotland and is famous with different legends about a monster called Nessie.\
              St. Columba commanded Nessie to drop the guy and the monster obeyed. Nessie may not put in an appearance, but you'll have a great afternoon cruising this lovely loch.\
              On the edge of the Loch Ness sits the ruins of Urquhart castle. It hasn't crumbled all on its own – part of it was blown up in 1692.\
              Don\'t be surprised if you hear a bagpiper piping tunes that evoke the ghosts of clans past – he\'s real.\
              You can run up and down the grassy ruined rooms or just sit peacefully on the stone ramparts, watching the wind ruffle waves on Loch Ness.", "numOfQuestions": 5},

              4: {"topic": "Dundee", "content": "Dundee (Scottish Gaelic: Dùn Dèagh) is the fourth-largest city in Scotland.Its history begins with the Picts in the Iron Age.\
              The name Dundee is of uncertain etymology.It incorporates the place - name element dùn, fort, present in both Gaelic and in Brythoniclanguages such as Pictish.The remainder of the name is less obvious.\
              One possibility is that it comes from the Gaelic Deagh meaning fire.Two very important places should be remembered when visiting Dundee.\
              The first one is the Discovery Ship and the second one is the Barry Mill. The Royal Research Ship Discovery was built in Dundee for the 1901 expedition of Scott and Shackleton to Antarctica.\
              This tall masted ship spent two winters locked in the ice, but now is restored and sitting dockside in Dundee.\
              Barry Mill is a water mill invented in the 19th century, still grinding corn.\
              All the moving mechanical stuff, elevators, sieves and sack hoists, is fascinating.\
              The city was also industrial centre in Scotland.Dundee's location on a major estuary allowed for the easy importation of jute from the Indian subcontinent as well as whale oil—needed for the processing of the jute—from the city's large whaling industry.\
              A substantial coastal marine trade also developed, with inshore shipping working between the city of Dundee and the port of London.\
              The industry began to decline in the 20th century as it became cheaper to process the cloth on the Indian subcontinent.\
              The city's last jute mill closed in the 1970s. In addition to jute the city is also known for jam and journalism.\
              The jam association refers to marmalade, which was purportedly invented in the city by Janet Keiller in 1797 (although in reality, recipes for marmalade have been found dating back to the 16th century).\
              Keiller's marmalade became a famous brand because of its mass production and its worldwide export.", "numOfQuestions": 5},

              5: {"topic": "Aberdeen", "content":"Aberdeen, the third largest city in Britain, is called The Granite City, but it has some of the best gardens – roses are a local specialty.\
              But there\'s more than gardens for kids in Aberdeen – this is an ocean-going city and you\'re never far away from its rich martime heritage.\
              Aberdeen is one of Britain\'s busiest harbors, and has a long maritime history.\
              In the Maritime Museum, you can\'t miss a three stories high re - creation of an oil rig in the North Sea.\
              The museum has hundreds of ship models, and exhibits about shipbuilding, whaling, life and work at sea.\
              Since the discovery of North Sea oil in the 1970 s, other nicknames have been the Oil Capital of the World or the Energy Capital of the World. \
              During the Wars of Scottish Independence, Aberdeen was under English rule, so Robert the Bruce laid siege to Aberdeen Castle before destroying it in 1308.\
              The city was burned by Edward III of England in 1336, but was rebuilt and extended, and called New Aberdeen.The city was strongly fortified to prevent attacks by neighbouring lords, but the gates were removed by 1770. \
              Aberdeen is a host of Aberdeen International Youth Festival, a major international event of young performers." ,"numOfQuestions": 5},

              6: {"topic": "Stirling", "content": "Stirling is the site of two great battles in Scottish history:\
              Stirling Bridge and Bannockburn.\
              During the Middle Ages, the Scots and English fought for 60 years – Stirling Castle was a prize for both sides.\
              In 1297, William Wallace had a small force, but he lured English knights across Stirling Bridge, split their army, and won the day.\
              Robert the Bruce, King of the Scots, set the scene for the English army to get bogged down, literally, at Bannockburn.\
              Traveling to Stirling with kids, step into Scotland centuries ago.\
              Not at all a crumbly castle, Stirling Castle is a jewel of Scottish castle construction.\
              It sits on rock overlooking the valley below, and was attacked over and over in the MiddleAges.\
              William Wallace took the castle from the English, but seven years later King Edward I successfully besieged the great fortresswith a huge war machine, called War Wolf.\
              The moto of the city is Bon Accord, which means good agreement and has been used in the past as a password for entering the city." ,"numOfQuestions": 5}}


    for level, level_data in levels.items():
        print(level)
        newLevel = add_level(level, level_data["topic"], level_data["content"], level_data["numOfQuestions"]) #TODO ne znam kakvo se sluchva tuk :D
        for q in quiz_questions:
            if (q["question_id"] <= len(levels.items()) * level and q["question_id"] > len(levels.items()) * (level-1)):
                add_question(newLevel, q["question_id"], q["question"], q["correctAnswer"], q["incorrectAnswer1"], q["incorrectAnswer2"], q["incorrectAnswer3"])

    for l in Level.objects.all():
       for q in QuizQuestion.objects.filter(level=l):
            print("- {0} - {1}".format(l.topic, q.question))


def add_level(number, topic, content, numofquestions):
    level = Level.objects.get_or_create(number=number, numOfQuestions=numofquestions)[0]
    level.topic = topic
    level.content = content
    level.numOfQuestions = numofquestions
    level.save()

    return level



def add_question(level, id, question, correct, incorrect1, incorrect2, incorrect3):
   print("trying to create question with id: ", id, "for level: ", level.number)
   q = QuizQuestion.objects.get_or_create(question_id=id, level = level)[0]
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
