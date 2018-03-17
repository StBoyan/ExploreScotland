import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'explore_scotland_project')

import django
django.setup()
from explorescotland.models import textFieldOnMap

def populate():
    markers = [
    {"marker_id=":1, "text1":"Glasgow has a reputation of being an industrial city, but also in the past used to be a  natural location for fishing.",
"The area around Glasgow has hosted communities for millennia, with the River Clyde providing a natural location for fishing. The Romans later built outposts in the area and, to keep separate from the Celtic and Pictish Caledonia, constructed the Antonine Wall.",
"Glasgow itself was founded by the Christian Missionary Saint Mungo in the 6th century. He established a church on the Molendinar Burn, where the present Glasgow Cathedral stands, and in the following years Glasgow became a religious centre.",
"After 1860 the Clydeside shipyards specialised in steamships made of iron (after 1870, made of steel), which rapidly replaced the wooden sailing vessels of both the merchant fleets and the battle fleets of the world. It became the world's pre-eminent shipbuilding centre.",

"In the late 17th century, Scottish linen was a major export to England. In 1680, the linen industry employed about 12,000 people in the Glasgow area, and the industry was heavily promoted by the government. " ,
"Thanks to a series of government acts and beneficial tax measures, by 1770, Glasgow had become the largest linen manufacturer in Britain.",
"Glasgow is the capital of contemporary music in Scotland, and has many venues and clubs such as the Barrowlands, Barfly and King Tut's Wah Wah Hut that promote new bands and DJs. Additionally, it is home to some artists well known in the UK such as Franz Ferdinand and Belle & Sebastian.",}

        {"marker_id":2 ,"text2":"From Edinburgh Castle down the Royal Mile to the Palace of Holyroodhouse, Edinburgh spans centuries of Scottish history, and continues to this day, as the capital of Scotland. It's a city that captures the imagination.",
        "J.K. Rowling wrote the first Harry Potter books in Edinburgh cafes",
        "Traveling around Edinburgh, cobbled streets and narrow lanes lead into unexpected places, where a dog, unicorns, Mary Queen of Scots, fairy cakes, and the Stone of Destiny await.",
    "Look for unicorns – Unicorns are a central theme of the Royal Arms of Scotland.",
    "See how many unicorns you can find. There are plenty to see around the Palace of Holyroodhouse, also in Edinburgh Castle, in St. Giles' Cathedral, on the Mercat Cross.",
    "In shops look for old fashioned sweets (also the gift shop at the National Museum of Scotland) – sour plooms, black and white humbugs, iron brew creams, fried eggs, saltire (blue and white like flag of Scotland), butterscotch, pan drops, Edinburgh rock.",
    "There's also Haggis Poo – chocolate covered raisins, and Nessie Poo – toffee on the outside, a raisin inside.",
            "The city has a very interesting history, but what is most important to know is that it was established by King David 1 in 1130 and as one of Scotland's earliest royal burghs, protected by his royal fortress, on the slope below the castle rock, which still is present and it is open for visitors.",}

    {"marker_3":3,"text3":"Loch Ness is magical place to visit.",
     "It is beautiful lake in the North part of Scotland and is famous with different legends about a monster called Nessie.",
    "St. Columba commanded Nessie to drop the guy and the monster obeyed.",
    "Nessie may not put in an appearance, but you'll have a great afternoon cruising this lovely loch.",
    "On the edge of the Loch Ness sits the ruins of Urquhart castle.",
    "It hasn't crumbled all on its own – part of it was blown up in 1692."
    "Don't be surprised if you hear a bagpiper piping tunes that evoke the ghosts of clans past – he's real."
    "You can run up and down the grassy ruined rooms or just sit peacefully on the stone ramparts, watching the wind ruffle waves on Loch Ness.",
    }

    {"marker_id":4,"text4":"Dundee (Scottish Gaelic: Dùn Dèagh) is the fourth-largest city in Scotland.",
     "Its history begins with the Picts in the Iron Age. ",
     "The name Dundee is of uncertain etymology." 
    "It incorporates the place - name element dùn, fort, present in both Gaelic and in Brythoniclanguages such as Pictish.",
    "The remainder of the name is less obvious.",
    "One possibility is that it comes from the Gaelic Deagh meaning fire",
    "Two very important places should be remembered.",
    "The first one is the Discovery Ship and the second one is the Barry Mill.",
     "The Royal Research Ship Discovery was built in Dundee for the 1901 expedition of Scott and Shackleton to Antarctica.",
    "This tall masted ship spent two winters locked in the ice, but now is restored and sitting dockside in Dundee.",
    "Barry Mill is a water mill invented in the 19th century, still grinding corn.",
    "All the moving mechanical stuff, elevators, sieves and sack hoists, is fascinating.",
    " city was also industrial centre in Scotland.Dundee's location on a major estuary allowed for the easy importation of jute from the Indian subcontinent as well as whale oil—needed for the processing of the jute—from the city's large whaling industry.",
    "A substantial coastal marine trade also developed, with inshore shipping working between the city of Dundee and the port of London.",
    "The industry began to decline in the 20th century as it became cheaper to process the cloth on the Indian subcontinent.",
    "The city's last jute mill closed in the 1970s.",
"In addition to jute the city is also known for jam and journalism.",
" The jam association refers to marmalade, which was purportedly invented in the city by Janet Keiller in 1797 (although in reality, recipes for marmalade have been found dating back to the 16th century)." ,
" Keiller's marmalade became a famous brand because of its mass production and its worldwide export."}

    {"marker_id":5,"text5":"Aberdeen, the third largest city in Britain, is called The Granite City, but it has some of the best gardens – roses are a local specialty.",
     "But there's more than gardens for kids in Aberdeen – this is an ocean-going city and you're never far away from its rich martime heritage.",
    "Aberdeen is one of Britain's busiest harbors, and has a long maritime history.",
    "In the Maritime Museum, you can't miss a three stories high re - creation of an oil rig in the North Sea.",
    "The museum has hundreds of ship models, and exhibits about shipbuilding, whaling, life and work at sea.",
   "Since the discovery of North Sea oil in the 1970 s, other nicknames have been the Oil Capital of the World or theEnergy Capital of the World.",
    "During the Wars of Scottish Independence, Aberdeen was under English rule, so Robert the Bruce laid siege to Aberdeen Castle before destroying it in 1308.",
    "The city was burned by Edward III of England in 1336, but was rebuilt and extended, and called New Aberdeen.The city was strongly fortified to prevent attacks by neighbouring lords, but the gates were removed by 1770.",
    "Aberdeen is a host of Aberdeen International Youth Festival, a major international event of young performers.",}

    {"marker_id":6,"text6":"Stirling is the site of two great battles in Scottish history:"
     "Stirling Bridge and Bannockburn. During the Middle Ages, the Scots and English fought for 60 years – Stirling Castle was a prize for both sides.",
     "In 1297, William Wallace had a small force, but he lured English knights across Stirling Bridge, split their army, and won the day."
    "Robert the Bruce, King of the Scots, set the scene for the English army to get bogged down, literally, at Bannockburn.",
    "Traveling to Stirling with kids, step into Scotland centuries ago.",
    "Not at all a crumbly castle, Stirling Castle is a jewel of Scottish castle construction.",
   "It sits on rock overlooking the valley below, and was attacked over and over in the MiddleAges."
   "William Wallace took the castle from the English, but seven years later King Edward I successfully besieged the great fortresswith a huge war machine, called War Wolf.",
    "The moto of the city is Bon Accord, which means good agreement and has been used in the past as a password for entering the city.",}]

    if __name__ == '__main__':
        print("Starting Textfield population script...")
    populate()
#the markers on the map are going to be called by Jquery with coordinates to be easily connected later with the database
# in this way the markers and the textfields could be easily connected and displayed on the web page
