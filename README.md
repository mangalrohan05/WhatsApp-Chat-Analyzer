# 📊 WhatsApp Chat Analyzer

A data-driven NLP project that transforms raw WhatsApp chat exports into meaningful insights, statistics, and visualizations.

---

## 🚀 Project Overview

This project analyzes WhatsApp chat data to extract useful information such as:

- 📈 Message statistics (total messages, words, media, links)  
- 👤 Most active users  
- 📅 Timeline analysis (daily/monthly activity)  
- 🔤 Word frequency and common words  
- 😂 Emoji analysis  
- ☁️ WordCloud visualization  
- 📊 Activity heatmaps  

The goal of this project was not just to build something functional, but to **learn by building** — applying concepts from Python, Data Analysis, and NLP in a real-world scenario.

---

## 🧠 Learning Objective

This project was built while learning:

- Python (Data handling & scripting)  
- Pandas & NumPy (Data analysis)  
- Matplotlib & Seaborn (Visualization)  
- NLP basics (Text preprocessing, TF-IDF, sentiment)  
- Regular Expressions (Chat parsing)  

Instead of just studying theory, I focused on **hands-on implementation**, solving real problems step-by-step.

---

## ⚙️ Features

- ✔️ Clean parsing of WhatsApp chat export (.txt)  
- ✔️ Handles media messages & system messages  
- ✔️ User-wise analysis  
- ✔️ Hinglish text handling (basic level)  
- ✔️ Emoji extraction and analysis  
- ✔️ Visual dashboards  

---

## 🏗️ Project Structure

```
Whatsapp-Chat-Analyzer/
│
├── app.py                  # Main application
├── helper.py               # Core logic functions
├── preprocessor.py         # Chat cleaning & parsing
├── requirements.txt        # Dependencies
├── chat.txt                # Sample dataset
└── README.md               # Project documentation
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/Whatsapp-Chat-Analyzer.git
cd Whatsapp-Chat-Analyzer
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the project
```bash
streamlit run app.py
```

---

## 📊 How It Works

1. Export WhatsApp chat as `.txt`  
2. Upload it into the app  
3. The system:
   - Parses messages using regex  
   - Cleans text (removes media/system messages)  
   - Converts into structured DataFrame  
   - Applies analysis functions  
4. Displays insights using charts & visuals  

---

## 🧪 Sample Insights

- Who texts the most?  
- Which day is most active?  
- Most used words and emojis  
- Monthly activity trends  
- Peak chatting hours  

---

## 💡 My Learning Approach

This project reflects my approach to learning:

- I **did not just copy code** — I tried to understand each step  
- Broke the project into smaller problems:
  - Parsing text  
  - Cleaning data  
  - Analysis  
  - Visualization  
- Faced real issues like:
  - Regex errors  
  - Handling Hinglish text  
  - Missing libraries (like stopwords, emoji, etc.)  

---

## 🤖 Use of ChatGPT

During development, I used ChatGPT as a **learning assistant**, not a shortcut.

### How I used it:
- Understanding concepts like:
  - TF-IDF  
  - Word2Vec differences  
  - Sentiment analysis  
- Debugging errors (e.g., missing modules, regex issues)  
- Improving code structure  
- Getting guidance on next steps  

### Important:
- The **core implementation and integration were done by me**  
- ChatGPT helped me **learn faster**, not skip learning  

This project represents a **build-with-learning mindset**, not copy-paste development.

---

## ⚠️ Challenges Faced

- Handling inconsistent chat formats  
- Dealing with Hinglish/mixed language data  
- Extracting emojis properly  
- Optimizing DataFrame operations  
- Understanding NLP concepts deeply  

---

## 🔮 Future Improvements

- Advanced NLP (better sentiment analysis)  
- Hinglish → English normalization  
- Chat clustering & topic modeling  
- Deployment (Web hosting)  
- Real-time chat analytics  

---

## 🙌 Conclusion

This project is more than just a tool — it’s a **learning journey**.

It demonstrates:
- Practical application of concepts  
- Problem-solving skills  
- Ability to learn independently with guidance  

---

## 📌 Author

**Rohan Mangal**  
3rd Year BE Student, MBM University, Jodhpur  
