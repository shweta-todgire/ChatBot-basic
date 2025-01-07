from flask import Flask, render_template, request, jsonify
import nltk
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

pairs = [
    (r'hello|hi', ['Hello! CodeAlpha this side! How can I assist you today?']),
    (r'about codealpha|about your company', ['CodeAlpha is an Indian Ed-Tech platform providing professional training through virtual internships and courses. We focus on hands-on learning to prepare students for the tech industry.']),
    (r'programs|courses', ['We offer programs in Web Development, App Development, Java Programming, Python Programming, Machine Learning, Data Science, Cyber Security, and C++ Programming.']),
    (r'internship|internships', ['Our internship program focuses on practical learning by involving students in live projects under the guidance of experienced mentors.']),
    (r'partners|partnerships', ['We have partnerships with leading tech firms to enhance our training programs and provide valuable learning opportunities.']),
    (r'achievements|statistics', ['Over 129,000 students have completed internships with us, and 95% of certified students have enhanced their practical tech skills.']),
    (r'contact|phone', ['You can contact us at 9336576683.']),
    (r'linkedin|profile', ['You can view our LinkedIn profile here: [CodeAlpha LinkedIn](https://www.linkedin.com/company/codealpha)']),
    (r'website|url', ['Visit our website here: [CodeAlpha](https://www.codealpha.tech)']),
    (r'location|located|where are you based', ['CodeAlpha is based in India.']),
    (r'established|founded', ['CodeAlpha was established in 2022.']),
    (r'address|office location', ['Our office is located at Lucknow, Uttar Pradesh in India.']),
    (r'famous for|aim', ['CodeAlpha is famous for providing hands-on learning experiences through virtual internships and courses aimed at preparing students for the tech industry.']),
    (r'bye|exit', ['Goodbye! Take care!']),
    (r'Thank you|Thanks|Thank',['You`re welcome! If you have any more questions or query, feel free to ask.']),
]

def get_response(user_input):
    user_input = user_input.lower()
    for pattern, responses in pairs:
        if any(keyword.lower() in user_input for keyword in pattern.split('|')):
            return responses[0]
    return "Sorry,I'm unable to assist with that specific question."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['GET'])
def chat():
    user_input = request.args.get('msg')
    chatbot_response = get_response(user_input)
    return jsonify({'response': chatbot_response})

if __name__ == '__main__':
    app.run(debug=True)
