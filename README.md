# TriviQ - Trivia Quiz Game

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

## 🚀 Quick Start

\`\`\`bash
# Clone the repository
git clone https://github.com/RichardOyelowo/CLI_QUIZ.git
cd CLI_QUIZ

# Install dependencies
pip install -r requirements.txt

# Run the game
python project.py
\`\`\`

#### Video Demo:  <https://www.youtube.com/watch?v=w7BfnOQqPwA&feature=youtu.be>

#### Description:
This is a simple **Trivia Quiz Game** I built using Python.
I decided to call it **TriviQ** (short for Trivia IQ) because it’s a fun little way to test how much you know.
It uses the [Open Trivia Database API](https://opentdb.com/) to fetch random True/False questions from different categories.
You can choose a topic, answer 10 questions, and get a grade at the end based on your score.


##### I hope this is easier to read and friendlier than the dcumentations you've read

### 🎮 How I Structured it
When you run the game:
1. It first shows a **grading table** so you know how scores are ranked.
```Grades
+---------+-----------+
| Score   | Grade     |
+=========+===========+
| 8-10    | Excellent |
+---------+-----------+
| 6-7     | Good      |
+---------+-----------+
| 4-5     | Average   |
+---------+-----------+
| 0-3     | Low       |
+---------+-----------+
```
2. Then it shows a list of topics (like History, Science, Geography, etc.).
```Topics
┌───────────┬───────────────────┐
│ OPTIONS   │ CHOICE            │
├───────────┼───────────────────┤
│ A         │ General Knowledge │
├───────────┼───────────────────┤
│ B         │ History           │
├───────────┼───────────────────┤
│ C         │ Mathematics       │
├───────────┼───────────────────┤
│ D         │ Geography         │
├───────────┼───────────────────┤
│ E         │ Mythology         │
├───────────┼───────────────────┤
│ F         │ Politics          │
├───────────┼───────────────────┤
│ G         │ Art               │
├───────────┼───────────────────┤
│ H         │ Vehicles          │
├───────────┼───────────────────┤
│ I         │ Sports            │
└───────────┴───────────────────┘
```

4. You choose one topic by typing its letter (like “A” for General Knowledge).
5. It pulls **10 True/False questions** from the API.
6. You answer each question and get **instant Validation** (✅ or ❌).
7. At the end, you’ll see your **total score and grade**.

---

### 💡 Why I Built It This Way

I made a lot of small choices along the way, so here’s how and why I did them.

#### 1. Using a Class(`Questions`)
I used a class to handle everything about setting up the quiz — the topics, category ID, and fetching the questions.
At first, I thought of writing all this using just functions, but it started looking messy.
So I went with a class to keep things **organized and reusable** and in case i need to change the API because it seems to not have enough questions so i had to settle for 10.

#### 2. Topics and IDs
Each topic has a letter (like “A”, “B”, “C”) and a matching ID that the API uses.
I stored them as a list and a dictionary so I can easily print them and look them up.

#### 3. Showing Tables with `tabulate`
I used the **tabulate** module to make things look nice in the terminal.
With it, everything is in a table format, which looks **cleaner and easier to read**.

#### 4. Input Validation
For user input, I used loops so it keeps asking again if you type something wrong.
For example, if you don’t type “True” or “False”, it reminds you and asks again.
Earlier, I tried using try/except and seems to be returning unnecassary errors, but a simple `if`  to check and `continue` to restart the loop if it deosn't meak the condition made more sense and looked cleaner.

#### 5. HTML Decoding
When I first printed questions, I noticed weird characters like `&quot;` or `&#039;`.
So I did few google search and found out they are characters that gets formatted into codes from the API so i found out about the unescape method i can use in html `html.unescape()` to clean them up and show normal text.

#### 6. Instant Validation
After every question, the program tells you **“correct ✅”** or **“wrong ❌”**.
I felt it would be more fun and interactive than waiting until the end to see how you did.

#### 7. Grading System
Instead of percentages, I used score ranges just to make it a bit more friendly(learning format):

- `8–10` → **Excellent**
- `6–7` → **Above Average**
- `4–5` → **Average**
- `0–3` → **Low**

---

### My Code Structure

Here’s a rough breakdown of how everything works:

**Questions class**- Handles topics, getting user’s choice, and fetching questions from the API
    - ***check_options()*** - Makes sure user picks a valid topic
    - ***get_questions()*** - Sends the request to the API using the selected topic ID, cleans up the question text with html.unescape(), and stores them in a list.
```
- **question_data()** - Loops through all 10 questions
- **validate_answer()** - Checks your answer and adds points
- **check_grade()** - Turns your score into a grade
```
---

## 🛠️ Technologies Used
- **Python 3.x**
- **requests** - HTTP library for API calls
- **tabulate** - Creates formatted tables
- **Open Trivia Database API** - Question source
