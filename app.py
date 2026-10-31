
import streamlit as st
from difflib import SequenceMatcher

# Page configuration
st.set_page_config(
    page_title="AI College Enquiry Chatbot",
    page_icon="🎓",
    layout="centered"
)

# College information
college_name = "Chandigarh University"

# Frequently asked questions and answers
faq = {
    "courses": {
        "keywords": ["course", "courses", "program", "degree", "bca", "mca", "bba"],
        "answer": "We offer courses such as BCA, BBA, MCA, MBA and other undergraduate and postgraduate programs. Please check the official college website for the latest list."
    },
    "admission": {
        "keywords": ["admission", "apply", "application", "enroll", "registration"],
        "answer": "You can apply for admission through the college admission office or official admission portal."
    },
    "fees": {
        "keywords": ["fee", "fees", "cost", "payment", "scholarship"],
        "answer": "Course fees depend on the selected program. Please contact the college admission department for the latest fee structure."
    },
    "location": {
        "keywords": ["location", "address", "where", "campus"],
        "answer": "Please visit the official college website for the campus address and directions."
    },
    "timing": {
        "keywords": ["timing", "time", "hours", "schedule", "classes"],
        "answer": "Class timings depend on the course and timetable. Contact your department for exact timings."
    },
    "documents": {
        "keywords": ["documents", "certificate", "marksheet", "required", "papers"],
        "answer": "Generally, admission requires previous academic marksheets, identity proof, photographs and other course-specific documents."
    },
    "hostel": {
        "keywords": ["hostel", "accommodation", "room", "stay"],
        "answer": "Please contact the college hostel department for room availability, facilities and charges."
    },
    "contact": {
        "keywords": ["contact", "phone", "email", "number", "help"],
        "answer": "You can contact the college reception or visit its official website for verified contact details."
    }
}

# Chatbot response function
def get_response(user_message):
    message = user_message.lower().strip()

    if any(word in message for word in ["hello", "hi", "hey"]):
        return "Hello! 👋 Welcome to ABC College. How can I help you?"

    if "thank" in message:
        return "You're welcome! 😊 Feel free to ask another question."

    best_match = None
    highest_score = 0

    for category, data in faq.items():
        score = 0

        for keyword in data["keywords"]:
            if keyword in message:
                score += 1

        if score > highest_score:
            highest_score = score
            best_match = category

    if best_match:
        return faq[best_match]["answer"]

    return (
        "Sorry, I couldn't understand your question. "
        "Please ask about courses, admission, fees, "
        "hostel, documents or college location."
    )


# Main interface
st.title("🎓 AI College Enquiry Chatbot")
st.caption("Your virtual assistant for college information")

st.info("Welcome! Ask me anything about college enquiries.")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! Welcome to ABC College. How can I help you today?"
        }
    ]

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input("Ask your college question...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    response = get_response(user_input)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    st.rerun()

# Sidebar
with st.sidebar:
    st.header("🎓 College Help Desk")
    st.write("Available enquiry topics:")

    topics = [
        "Courses",
        "Admission",
        "Fees",
        "College Location",
        "Class Timings",
        "Required Documents",
        "Hostel",
        "Contact Information"
    ]

    for topic in topics:
        st.write("• " + topic)

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()
