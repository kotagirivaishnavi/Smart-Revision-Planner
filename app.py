import streamlit as st
import ollama

st.set_page_config(
    page_title="Smart Revision Planner",
    page_icon="📚"
)

st.title("📚 Smart Revision Planner")
st.write("Create an AI-powered revision plan using Ollama.")

subject = st.text_input("Enter Subject")

if st.button("Generate Plan"):

    if subject.strip() == "":
        st.warning("Please enter a subject.")

    else:
        with st.spinner("Creating your revision plan..."):

            try:
                response = ollama.chat(
                    model="llama3.2",
                    messages=[
                        {
                            "role": "user",
                            "content": (
                                f"Create a simple and practical revision plan "
                                f"for the subject {subject}. "
                                "Include topics, study time, breaks, "
                                "and revision activities."
                            )
                        }
                    ]
                )

                plan = response["message"]["content"]

                st.subheader("Your Revision Plan")
                st.write(plan)

            except Exception as e:
                st.error("Unable to connect to Ollama.")
                st.write("Error:", e)
import streamlit as st
import ollama
from datetime import date

st.set_page_config(
    page_title="Smart Revision Planner",
    page_icon="📚",
    layout="centered"
)

st.title("📚 Smart Revision Planner")
st.write("AI-powered revision planning using Ollama")

# Inputs
st.header("Enter Your Study Details")

subjects = st.text_area(
    "📖 Enter your subjects",
    placeholder="Example:\nPython\nData Structures\nOperating Systems\nMathematics"
)

exam_date = st.date_input(
    "📅 Exam Date",
    min_value=date.today()
)

hours = st.number_input(
    "⏰ Available study hours per day",
    min_value=1,
    max_value=12,
    value=3
)

difficulty = st.selectbox(
    "🎯 Overall difficulty",
    ["Easy", "Medium", "Hard"]
)

# Generate plan
if st.button("🤖 Generate Revision Plan"):

    if not subjects.strip():
        st.warning("Please enter at least one subject.")

    else:
        prompt = f"""
Create a detailed and practical revision plan for a student.

Subjects:
{subjects}

Exam date:
{exam_date}

Available study hours per day:
{hours}

Overall difficulty:
{difficulty}

Create the plan in a clear format.

Include:
1. Daily study schedule
2. Subject allocation
3. Important topics
4. Short breaks
5. Revision sessions
6. Practice/test sessions
7. Final revision before the exam

Make the plan realistic and easy to follow.
"""

        with st.spinner("🤖 AI is creating your revision plan..."):

            try:
                response = ollama.chat(
                    model="llama3.2",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                plan = response["message"]["content"]

                st.success("Revision plan created successfully! 🎉")

                st.subheader("📋 Your AI Revision Plan")

                st.write(plan)

            except Exception as e:
                st.error("Could not connect to Ollama.")
                st.write("Error:", e)