import streamlit as st

st.set_page_config(page_title="Birthday Journey ❤️", page_icon="🎂")

st.title("Happy 21st Birthday Ana ❤️")

# Initialize step
if "step" not in st.session_state:
    st.session_state.step = 0

# Initialize answers in session_state
for key in ["answer1", "answer3", "answer5", "answer7", "answer9", "answer11"]:
    if key not in st.session_state:
        st.session_state[key] = ""

# Function to check answer and move step
def check_answer(answer_key, correct_answers, next_step):
    user_answer = st.session_state[answer_key].strip().lower()
    correct_answers_lower = [a.lower() for a in correct_answers]
    if user_answer in correct_answers_lower:
        st.success("Correct! ❤️")
        st.session_state.step = next_step
    elif user_answer:
        st.error("Try again 😏")

# ---------------- STEP 0 (INTRO) ----------------
if st.session_state.step == 0:
    st.image("C:/Users/User/Desktop/Shenaal/Shen Personal/Ana 21st/Ana 21st/Intro.png")
    st.write("An unforgettable birthday journey awaits you... ❤️")

    if st.button("Start Your Journey 💌"):
        st.session_state.step = 1

# ---------------- STEP 1 ----------------
elif st.session_state.step == 1:
    st.header("First Clue 🌸")
    st.write("Where did our journey first begin?")

    st.text_input("Your answer:", key="answer1", on_change=check_answer,
                  args=("answer1", ["university", "iit", "Uni"], 2))

# ---------------- STEP 2 (SWEET START) ----------------
elif st.session_state.step == 2:
    st.image("C:/Users/User/Desktop/Shenaal/Shen Personal/Ana 21st/Ana 21st/sweet_start.png")
    st.write("A sweet start to your day 🍰")

    if st.button("Unlock Next Stop 😏"):
        st.session_state.step = 3

# ---------------- STEP 3 (OUTFIT RIDDLE) ----------------
elif st.session_state.step == 3:
    st.header("Next Clue 👗")
    st.write("Where do you always go when you want to look your best?")

    st.text_input("Your answer:", key="answer3", on_change=check_answer,
                  args=("answer3", ["mimosa", "ogf"], 4))

# ---------------- STEP 4 (OUTFIT STOP) ----------------
elif st.session_state.step == 4:
    st.image("C:/Users/User/Desktop/Shenaal/Shen Personal/Ana 21st/Ana 21st/outfit.png")

    if st.button("Next Surprise 👀"):
        st.session_state.step = 5

# ---------------- STEP 5 (SUSHI RIDDLE) ----------------
elif st.session_state.step == 5:
    st.header("Food Time ")
    st.write("What’s your go-to food that you can never say no to?")

    st.text_input("Your answer:", key="answer5", on_change=check_answer,
                  args=("answer5", ["Sushi","sushi kai"], 6))

# ---------------- STEP 6 (SUSHI STOP) ----------------
elif st.session_state.step == 6:
    st.image("C:/Users/User/Desktop/Shenaal/Shen Personal/Ana 21st/Ana 21st/sushi.png")

    if st.button("But wait... 😏"):
        st.session_state.step = 7

# ---------------- STEP 7 (DESSERT RIDDLE) ----------------
elif st.session_state.step == 7:
    st.header("Something Missing 🍨")
    st.write("A perfect day isn’t complete without something...?")

    st.text_input("Your answer:", key="answer7", on_change=check_answer,
                  args=("answer7", ["Jagro", "Waffles"], 8))

# ---------------- STEP 8 (DESSERT STOP) ----------------
elif st.session_state.step == 8:
    st.image("C:/Users/User/Desktop/Shenaal/Shen Personal/Ana 21st/Ana 21st/dessert.png")

    if st.button("Time to spoil you 😌"):
        st.session_state.step = 9

# ---------------- STEP 9 (SHOPPING RIDDLE) ----------------
elif st.session_state.step == 9:
    st.header("Shopping Time 🛍️")
    st.write("Where would you go if you could buy anything today?")

    st.text_input("Your answer:", key="answer9", on_change=check_answer,
                  args=("answer9", ["one galle face", "mall"], 10))

# ---------------- STEP 10 (SHOPPING STOP) ----------------
elif st.session_state.step == 10:
    st.image("C:/Users/User/Desktop/Shenaal/Shen Personal/Ana 21st/Ana 21st/shopping.png")

    if st.button("Final Stop ❤️"):
        st.session_state.step = 11

# ---------------- STEP 11 (FINAL RIDDLE) ----------------
elif st.session_state.step == 11:
    st.header("Last Clue 🍽️")
    st.write("Where are we ending this perfect day?")

    st.text_input("Your answer:", key="answer11", on_change=check_answer,
                  args=("answer11", ["cinnamon life", "buffet"], 12))

# ---------------- STEP 12 (FINAL PAGE) ----------------
elif st.session_state.step == 12:
    st.image("C:/Users/User/Desktop/Shenaal/Shen Personal/Ana 21st/Ana 21st/final.png")

    st.title("Happy Birthday My Love ❤️")
    st.write("""
    To ana,
I hope your journey around you favourite places was the best 21st you ever wanted my lovee and happy birthday to the most beautiful, intelligent, and extraordinary individual I have ever seen my manikaaa!! I hope all ur dreams come true this year as you are working soo hard for all your goals, and always know that i will have your back no matter what and i will support you in everything you do my lovee !! I lovee youu bubsyyy and you are the prettiest girl out there, my lovee and still from day one your smile gives me butterflies every single time !!

I have known you since you were 17 and now ur 21 girlyy and its amazing to see wt kind of individual you have become my loveee !! I know we have had our ups and downs and somehow we have overcome them and gotten here my lovee !! So i hope you have the bestest 21st birthday !!
from suri.💕
    """)

    st.balloons()