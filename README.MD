# Answer Sheet Evaluator

An LLM-based tool that compares a student's descriptive answer with a model answer, suggests a score out of the maximum marks, lists the key points covered and missed, and gives short constructive feedback.

**Problem Statement:** PS24 - Checking descriptive answers is slow. Compare a student answer with a model answer and suggest a score with feedback.

## Features

- Accepts a question, model answer, student answer and maximum marks
- Breaks the model answer into weighted key points
- Judges each key point as covered or not covered
- Calculates the score in Python from the weights, so the marks are consistent
- Gives a list of covered points, missing points and short feedback
- Simple Streamlit web interface

## Tools Used

- Python 3
- Streamlit (user interface)
- OpenAI Python SDK (used as a client for the Groq API)
- Groq API with Llama 3.1 8B Instant (free tier)
- python-dotenv (loads the API key from `.env`)

## Project Structure

```
answer-sheet-evaluator/
├── evaluator.py      # core logic: prompt, LLM call, scoring
├── app.py            # Streamlit user interface
├── test_samples.py   # test cases for the evaluator
├── requirements.txt  # Python dependencies
├── .gitignore        # files excluded from Git (.env, venv/)
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/<username>/llm-ps24-<RollNo>.git
cd llm-ps24-<RollNo>
```

### 2. Create and activate a virtual environment

On Windows PowerShell:
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

On Mac or Linux:
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install the requirements

```bash
pip install -r requirements.txt
```

### 4. Add your API key

Get a free key from [console.groq.com/keys](https://console.groq.com/keys), then create a file named `.env` in the project folder:

```
GROQ_API_KEY=your_key_here
```

Do not commit this file. It is already listed in `.gitignore`.

## How to Run

Start the web app:

```bash
python -m streamlit run app.py
```

Open the local URL shown in the terminal (usually http://localhost:8501), enter the question, model answer and student answer, set the maximum marks, and click **Evaluate**.

To run the test cases in the terminal:

```bash
python test_samples.py
```

## How It Works

1. The prompt asks the LLM to list 3 to 6 key points from the model answer, each with a weight from 1 to 3.
2. For each key point, the LLM returns `covered: true` or `covered: false` and short feedback.
3. `evaluator.py` calculates the score:

   `score = (sum of weights of covered points / total weight) × maximum marks`

4. The app displays the score, covered points, missing points and feedback.

Blank student answers are scored 0 without calling the API.

## Changing the Model

The model name is set near the top of `evaluator.py`:

```python
MODEL = "llama-3.1-8b-instant"
```

To see which models your key can access, run:

```bash
python -c "from openai import OpenAI; import os; from dotenv import load_dotenv; load_dotenv(); c=OpenAI(api_key=os.getenv('GROQ_API_KEY'), base_url='https://api.groq.com/openai/v1'); [print(m.id) for m in c.models.list().data]"
```

## Screenshots

*Add screenshots here, for example:*

![Full marks result](screenshots/full_marks.png)

## Limitations

- The LLM's judgment of borderline points can still vary between runs.
- Small models may miss subtle errors in technical answers.
- The key points are generated automatically from the model answer, so a poorly written model answer gives weaker results.

## Future Improvements

- Let teachers define a fixed rubric with key points and weights for each question.
- Support handwritten answers through OCR.
- Export results to a CSV or PDF file for record keeping.

## Author

- **Name:** Kushal Vijay Patil
- **Roll Number:** 24
- **Enrollment Number:** ADT23SOCB0556
- **Class:** LY CORE 06