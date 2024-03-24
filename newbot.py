import streamlit as st

# Function to answer questions
def get_answer(question):
    # You can implement more sophisticated logic here based on your use case
    if question.lower() == 'what is your name?':
        return "I am a chatbot."
    elif question.lower() == 'how are you?':
        return "I'm doing well, thank you!"
    else:
        return "Sorry, I don't understand that question."

# Streamlit UI
def main():
    st.title("Question-Answer Chatbot")
    st.write("Ask me anything!")

    # User input for question
    question = st.text_input("You:", "")

    # Button to submit question
    if st.button("Ask"):
        # Get answer and display
        answer = get_answer(question)
        st.text_area("Bot:", value=answer, height=100)


if __name__ == "__main__":
    main()
