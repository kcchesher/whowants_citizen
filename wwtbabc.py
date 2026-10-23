import streamlit as st
import random as rd
 
st.set_page_config(page_title="WWTBABC", page_icon=':uk:')

st.title("Who Wants To Be A British Citizen?")

#lists
prizes = ("£100", "£200", "£300", "£500", "£1,000", "£2,000", "£4,000", "£8,000", "£16,000", "£32,000", "£64,000", "£125,000", "£250,000", "£500,000", "£1,000,000")
milestone_prizes = ("£0", "£1000", "£32,000", "£1,000,000")

questions = [
    {
        'question': "What did Hadrian build to keep the Scottish away from England?",
        'option': ["A small pit", "A medium-sized electric fence", "A big castle", "A giant wall"],
        'answer': "A giant wall",
        'level': 0
    },
    {
        'question': "Who were the first people to arrive in Britain in what we call the Stone Age?",
        'option': ["Farmers", "Hunter-gatherers", "Warriors", "Pirates"],
        'answer': "Hunter-gatherers",
        'level': 0
    },
    {
        'question': "Which of the following statements regarding the Black Death is NOT true?",
        'option': ["One third of the population of England died and a similar proportion in Scotland and Wales", "It was one of the worst disasters ever to strike Britain", "It affected children and old people only", "Following the Black Death, there were labour shortages"],
        'answer': "It affected children and old people only",
        'level': 0
    },
    {
        'question': "The Elizabethan period is known for the richness of its poetry and drama, especially for the plays and poems of which playwright?",
        'option': ["Alexander Dumas", "William Shakespeare", "Charles Dickens", "Thomas Hardy"],
        'answer': "William Shakespeare",
        'level': 0
    },
        {
        'question': "When is Christmas Eve celebrated?",
        'option': ["24th of December", "25th of December", "26th of December", "27th of December"],
        'answer': "24th of December",
        'level': 0
    },
    {
        'question': "Where were the Vikings from?",
        'option': ["Russia", "Italy and Spain", "India", "Norway and Denmark"],
        'answer': "Norway and Denmark",
        'level': 1
    },
    {
        'question': "What were the first Women's Social and Political Union group members called?",
        'option': ["The House of Lords", "Rotten boroughs", "Slaves", "Suffragettes"],
        'answer': "Suffragettes",
        'level': 1
    },
    {
        'question': "Which of the following is NOT a fundamental principle of British life?",
        'option': ["Tolerance of those with different faiths and beliefs", "The rule of law", "Autocracy", "Democracy"],
        'answer': "Autocracy",
        'level': 1
    },
    {
        'question': "Who is married to the King of the United Kingdom?",
        'option': ["Kate, the Princess of Wales", "Camila, the Queen Consort", "Camila, the Princess of Wales", "Kate, the Queen Consort"],
        'answer': "Camila, the Queen Consort",
        'level': 1
    },
    {
        'question': "What is the official home of the Prime Minister?",
        'option': ["Buckingham Palace", "Windsor Castle", "10 Downing Street", "21 Oxford Street"],
        'answer': "10 Downing Street",
        'level': 1
    },
    {
        'question': "What is know as Lent?",
        'option': ["The 40 days before Easter", "The 40 days after Easter", "The 40 days before Christmas", "The 40 days after Christmas"],
        'answer': "The 40 days before Easter",
        'level': 2
    },
    {
        'question': "Who tells visitors about the history of the Tower of London?",
        'option': ["Instructors", "London Guides", "Beefeaters", "History Graduates"],
        'answer': "Beefeaters",
        'level': 2
    },
    {
        'question': "What was the system of land ownership used by the Normans known as?",
        'option': ["The Magna Carter", "Noble land", "Feudalism", "Democracy"],
        'answer': "Feudalism",
        'level': 2
    },
    {
        'question': "Who is the spiritual leader of the Church of England?",
        'option': ["The Pope", "The Archbishop of Canterbury", "St Augustine", "St Columba"],
        'answer': "The Archbishop of Canterbury",
        'level': 2
    },
    {
        'question': "Elizabeth I was the younger daughter of which King?",
        'option': ["James I", "William the Great", "Henry VII", "Henry VIII"],
        'answer': "Henry VIII",
        'level': 2
    },
    {
        'question': "What country's flag is not part of the Union Flag?",
        'option': ["England", "Wales", "Scotland", "Ireland"],
        'answer': "Wales",
        'level': 3
    },
    {
        'question': "Which country's national flower is a thistle?",
        'option': ["England", "Wales", "Scotland", "Northern Ireland"],
        'answer': "Scotland",
        'level': 3
    },
    {
        'question': "Roast beef is a traditional food of which country?",
        'option': ["England", "Wales", "Scotland", "Northern Ireland"],
        'answer': "England",
        'level': 3
    },
    {
        'question': "Ulster fry is a traditional food of which country?",
        'option': ["England", "Wales", "Scotland", "Northern Ireland"],
        'answer': "Northern Ireland",
        'level': 3
    },
    {
        'question': "Where is the city of Swansea located?",
        'option': ["England", "Wales", "Scotland", "The Isle of Man"],
        'answer': "Wales",
        'level': 3
    },
    {
        'question': "Which of the events is the bombing of English cities by the Germans?",
        'option': ["The Blitz", "The Dunkirk Spirit", "D-Day", "The Battle of Britain"],
        'answer': "The Blitz",
        'level': 4
    },
    {
        'question': "When did the UK leave the EU following the Brexit Vote?",
        'option': ["1987", "2001", "2020", "2024"],
        'answer': "2020",
        'level': 4
    },
    {
        'question': "What can 'Carry on' be associated with?",
        'option': ["Art", "Novels", "Music", "Films"],
        'answer': "Films",
        'level': 4
    },
    {
        'question': "Who is know as William the Conqueror?",
        'option': ["William, the Duke of Normandy", "William, the Duke of France", "William, the Duke of Edinburgh", "William, the Duke of Lion"],
        'answer': "William, the Duke of Normandy",
        'level': 4
    },
    {
        'question': "Which flag has a diagonal red cross on a white ground?",
        'option': ["The cross of St George, patron saint of England", "The cross of St Patrick, patron saint of Ireland", "The cross of St David, patron saint of Wales", "The cross of St Andrew, patron saint of Scotland"],
        'answer': "The cross of St Patrick, patron saint of Ireland",
        'level': 4
    },
    {
        'question': "Which of these venues are located in Greenwich?",
        'option': ["The SECC", "The O2", "Auditorio de Tenerife", "The Copenhagen Concert Hall"],
        'answer': "The O2",
        'level': 5
    },
    {
        'question': "Magistrates and Justices of the Peace (JPs) are members of what?",
        'option': ["The Law Society", "The local community", "The Police Force", "The Monarchy"],
        'answer': "The local community",
        'level': 5
    },
    {
        'question': "Who can get a 50% discount on their TV licence?",
        'option': ["Blind people", "Students", "Army Officers", "Deaf People"],
        'answer': "Blind people",
        'level': 5
    },
    {
        'question': "What does the term 'coalition' refer to?",
        'option': ["If no political party wins a majority, a new election is held to vote for one of the top two parties only", "The candidate who gets the most votes is elected", "If no political party wins a majority, two parties may join and govern together", "If an MP dies or resigns, there will be a fresh election"],
        'answer': "If no political party wins a majority, two parties may join and govern together",
        'level': 5
    },
    {
        'question': "What are the judiciary responsible for?",
        'option': ["Deciding on a person's guilt", "Supervising a jury", "Putting people in prison", "Interpreting the law"],
        'answer': "Interpreting the law",
        'level': 6
    },
    {
        'question': "Who developed ideas about economics during the Enlightenment period which are still referred to today?",
        'option': ["David Hume", "Adam Smith", "James Watt", "Isaac Newton"],
        'answer': "Adam Smith",
        'level': 6
    },
    {
        'question': "What is the name of the centrepiece to the Remembrance Day service located in Whitehall, London?",
        'option': ["Cenotaph", "Stonehenge", "Grimsby", "Scunthorpe"],
        'answer': "Cenotaph",
        'level': 6
    },
    {
        'question': "Who was the inventor of the World Wide Web?",
        'option': ["Sir Tim Berners-Lee", "Sir Peter Mansfield", "Sir Ian Wilmut", "Sir Bernard Lovell"],
        'answer': "Sir Tim Berners-Lee",
        'level': 6
    },
    {
        'question': "What is the minimum age requirement in the UK to drink wine or beer with a meal provided you are with someone over 18?",
        'option': ["14 years old", "15 years old", "16 years old", "17 years old"],
        'answer': "16 years old",
        'level': 6
    },
    {
        'question': "Why is 'The Glorious Revloution' called that?",
        'option': ["Because women were given the right to vote", "Because of new technological advances", "Because there was no fighting", "Because of new achievements"],
        'answer': "Because there was no fighting",
        'level': 7
    },
    {
        'question': "When did the first farmers arrive in Britain?",
        'option': ["10,000 years ago", "8,000 years ago", "6,000 years ago", "4,000 years ago"],
        'answer': "6,000 years ago",
        'level': 7
    },     
    {
        'question': "Which Scottish city is known as the home of golf?",
        'option': ["Dundee", "Edinburgh", "Aberdeen", "St Andrews"],
        'answer': "St Andrews",
        'level': 7
    },
    {
        'question': "What awards event celebrates British theatre?",
        'option': ["The Turner Prize", "The Mecury Prize", "The Brit Awards", "The Laurence Olivier Awards"],
        'answer': "The Laurence Olivier Awards",
        'level': 7
    },
    {
        'question': "After the Black Death, new social classes appeared in England, including owners of large areas of land known as:",
        'option': ["Judiciary", "Gentry", "Clans", "Nobility"],
        'answer': "Gentry",
        'level': 7
    },
    {
        'question': "Who is credited with the introduction of the National Health Service (NHS) in 1948?",
        'option': ["Florence Nightingale", "David Hume", "Aneurin Bevan", "Winston Churchill"],
        'answer': "Aneurin Bevan",
        'level': 8
    },
    {
        'question': "Who was the 'Iron Duke' that defeated the Emperor Napoleon?",
        'option': ["Churchill", "Sir Christopher Wren", "Wellington", "Admiral Nelson"],
        'answer': "Wellington",
        'level': 8
    },
    {
        'question': "Which court deals with the most serious cases of children aged 10 to 17 in England, Wales and Northern Ireland?",
        'option': ["The High Court", "The Youth Court", "The Magistrates' Court", "The Crown Court"],
        'answer': "The Crown Court",
        'level': 8
    },
    {
        'question': "Which British sportsman won five consecutive gold medals at the Olympic Games in the rowing category?",
        'option': ["Sir Chris Hoy", "Christopher Dean", "Bradley Wiggins", "Sir Steve Redgrave"],
        'answer': "Sir Steve Redgrave",
        'level': 8
    },
    {
        'question': "What was the population of the UK in 2010?",
        'option': ["Just under 50 million", "Just over 50 million", "Just under 60 million", "Just over 62 million"],
        'answer': "Just over 62 million",
        'level': 8
    },
    {
        'question': "In England & Wales, the small claims procedure is an informal way of helping people to settle minor disputes claims of less than?",
        'option': ["£3,000", "£5,000", "£10,000", "£20,000"],
        'answer': "£10,000",
        'level': 9
    },
    {
        'question': "Which of Henry VIII's Wives was Anne Boleyn's Cousin?",
        'option': ["Catherine of Aragon", "Anne of Cleves", "Catherine Howard", "Katherine Parr"],
        'answer': "Catherine Howard",
        'level': 9
    },
    {
        'question': "Where is Loch Lomond and the Trossachs National Park located?",
        'option': ["East of Wales", "West of Wales", "West of Scotland", "East of Scotland"],
        'answer': "West of Scotland",
        'level': 9
    },
    {
        'question': "What time do pubs usually open on Sundays in the UK?",
        'option': ["10 am", "11 am", "12 pm", "1 pm"],
        'answer': "12 pm",
        'level': 9
    },
    {
        'question': "What percentage of the total British population is located in England alone?",
        'option': ["58%", "60%", "79%", "84%"],
        'answer': "84%",
        'level': 9
    },
    {
        'question': "Which tribes invaded Britain after the Romans had left?",
        'option': ["The Vikings", "The Jutes and the Anglo-Saxons", "The Celtics", "The Normans"],
        'answer': "The Jutes and the Anglo-Saxons",
        'level': 10
    },
    {
        'question': "When did the Irish Free State become a republic?",
        'option': ["1922", "1931", "1937", "1949"],
        'answer': "1949",
        'level': 10
    },
    {
        'question': "When did Ireland split into two countries?",
        'option': ["1916", "1921", "1922", "1959"],
        'answer': "1922",
        'level': 10
    },
    {
        'question': "What did Henry VII do?",
        'option': ["Restricted King's power", "Broke away from the Church of Rome", "Increased the power of the nobles", "Reduced the power of the nobles"],
        'answer': "Reduced the power of the nobles",
        'level': 10
    },
    {
        'question': "What is the name of the building where the Scottish Parliament meet?",
        'option': ["Holyrood", "Senedd", "Westminster", "Sotrmont"],
        'answer': "Holyrood",
        'level': 10
    },
    {
        'question': "When was The First British Prime minister (Sir Robert Walpole) in power?",
        'option': ["1707-1714", "1714-1721", "1721-1742", "1742-1746"],
        'answer': "1721-1742",
        'level': 11
    },
    {
        'question': "In which British university did Isaac Newton study?",
        'option': ["University of Bolton", "University of Cambridge", "Cranfield University", "University of Dundee"],
        'answer': "University of Cambridge",
        'level': 11
    },
    {
        'question': "Who was the first British Prime Minister?",
        'option': ["Henry Pelham", "Sir Robert Walpole", "Admiral Nelson", "Oliver Cromwell"],
        'answer': "Sir Robert Walpole",
        'level': 11
    },
    {
        'question': "In which period did British Film studios flourish?",
        'option': ["1920s", "1930s", "1940s", "1950s"],
        'answer': "1930s",
        'level': 11
    },
    {
        'question': "Which court deals with cases involving personal injury, family matters, breaches of contract and divorce in England and Wales?",
        'option': ["The Crown Court", "The High Court", "County Courts", "The Sheriff Court"],
        'answer': "County Courts",
        'level': 11
    },
    {
        'question': "When did the Habeas Corpus Act become law?",
        'option': ["1679", "1683", "1685", "1687"],
        'answer': "1679",
        'level': 12
    },
    {
        'question': "What is the name of the best preserved prehistoric village in northern Europe and which origin traces back to the Stone Age?",
        'option': ["Maiden", "Skara Brae", "Stonehenge", "Bayeux"],
        'answer': "Skara Brae",
        'level': 12
    },
    {
        'question': "When did the Conservative government call a referendum on the UK's membership of the European Union?",
        'option': ["23rd June 2015", "23rd July 2015", "23rd June 2016", "23rd July 2016"],
        'answer': "23rd June 2016",
        'level': 12
    },
    {
        'question': "Who is the fastest person to have sailed around the world single-handed?",
        'option': ["Dame Kelly Holmes", "Dame Ellen MacArthur", "Jayne Torvill", "Bradley Wiggins"],
        'answer': "Dame Ellen MacArthur",
        'level': 12
    },
    {
        'question': "When did the First World War end?",
        'option': ["9th of November 1918", "11th of November 1918", "9th of December 1918", "11th of December 1918"],
        'answer': "11th of November 1918",
        'level': 12
    },
    {
        'question': "Which languages were the basis of modern English?",
        'option': ["Norman French and Anglo Saxon", "Gaelic and Celtic", "Norman French and Celtic", "Celtic and Anglo Saxon"],
        'answer': "Norman French and Anglo Saxon",
        'level': 13
    },
    {
        'question': "When did Britain become permanently separated from the continent by the Channel?",
        'option': ["50,000 years ago", "18,000 years ago", "15,000 years ago", "10,000 years ago"],
        'answer': "10,000 years ago",
        'level': 13
    },
    {
        'question': "When was the National Trust founded?",
        'option': ["1890", "1895", "1910", "1980"],
        'answer': "1895",
        'level': 13
    },
    {
        'question': "Which British sportswoman won two gold medals for running in the 2004 Olympic Games?",
        'option': ["Dame Ellen MacArthur", "Jayne Torvill", "Dame Kelly Holmes", "Jessica Ennis-Hill"],
        'answer': "Dame Kelly Holmes",
        'level': 13
    },
    {
        'question': "Who was reigning in England when Wales became formally united with England by the Act for the Government of Wales?",
        'option': ["Henry VII", "Henry VIII", "Elizabeth I", "James I"],
        'answer': "Henry VIII",
        'level': 13
    },
    {
        'question': "How many members does The Northern Ireland Assembly have?",
        'option': ["90", "110", "119", "129"],
        'answer': "90",
        'level': 14
    },
    {
        'question': "How many members does The Scottish Parliament have?",
        'option': ["90", "110", "119", "129"],
        'answer': "129",
        'level': 14
    },
    {
        'question': "How much can you be fined if you watch TV but do not have a TV licence?",
        'option': ["Up to £500", "Up to £1000", "Up to £2000", "Up to £3000"],
        'answer': "Up to £1000",
        'level': 14
    },
    {
        'question': "When did the Wars of the Roses start?",
        'option': ["1388", "1455", "1462", "1478"],
        'answer': "1455",
        'level': 14
    },
        {
        'question': "When did the Wars of the Roses end?",
        'option': ["1455", "1462", "1478", "1485"],
        'answer': "1485",
        'level': 11
    },
]

#variables
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'milestone' not in st.session_state:
    st.session_state.milestone = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False


#functions
def restart_game():
    st.session_state.current_question = 0
    st.session_state.milestone = 0
    st.session_state.game_over = False
    if 'current_question_data' in st.session_state:
        del st.session_state.current_question_data

#gameplay
#check if lost
if st.session_state.game_over:
    st.error(f"WRONG ANSWER! You walk away with {milestone_prizes[st.session_state.milestone]}")
    if st.button("Try Again"):
        restart_game()
        st.rerun()

#check if won
if st.session_state.milestone == 3:
    st.success("Congratulations! You have won £1,000,000 and also citizenship")
    if st.button("Try Again"):
        restart_game()
        st.rerun()

if 'current_question_data' not in st.session_state:
    level_question_list = [q for q in questions if q['level'] == st.session_state.current_question]
    st.session_state.current_question_data = rd.choice(level_question_list)

show_question = st.session_state.current_question_data

st.write(f"Your current milestone winnings are {milestone_prizes[st.session_state.milestone]}. Your question for {prizes[st.session_state.current_question]}:")

#show question
with st.form(key='quiz_form'):
    answer_selection = st.radio(show_question["question"], show_question["option"])
    final_answer = st.form_submit_button(label="Final Answer")

if final_answer:
    if answer_selection == show_question["answer"]:
        if st.session_state.current_question in (4, 9, 14):
            st.session_state.milestone +=1
        if st.session_state.current_question < 14:
            st.session_state.current_question += 1
            del st.session_state.current_question_data
    else:
        st.session_state.game_over = True

    st.rerun()
        
