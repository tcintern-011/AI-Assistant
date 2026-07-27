````markdown
# AI Article Summarizer (LangChain + Groq)

A lightweight Python application built with **LangChain** and **Groq AI** that automatically generates concise, bulleted summaries of long articles using the **Llama 3.3 70B Versatile** model.

---

# Features

- Generates concise, fact-focused summaries of long articles.
- Powered by **Llama 3.3 (70B Versatile)** running on Groq's high-performance inference engine.
- Built using the **LangChain Expression Language (LCEL)** for a clean and modular architecture.
- Uses **ChatPromptTemplate**, **ChatGroq**, and **StrOutputParser** to create an end-to-end summarization pipeline.
- Securely manages API keys using **python-dotenv**.
- Easily customizable prompts and model selection.

---

# Prerequisites

Before running this project, ensure you have:

- **Python 3.10** or later
- A **Groq API Key** (available from the Groq Console)

---

# Project Structure

```text
.
├── .env                # API keys and secret variables (Do not commit)
├── main.py             # Main Python summarizer script
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

---

# Installation

## 1. Clone or Create the Project

```bash
mkdir article-summarizer
cd article-summarizer
```

---

## 2. Create a Virtual Environment (Recommended)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Requirements

Create a `requirements.txt` file with the following dependencies:

```text
langchain-core
langchain-groq
python-dotenv
```

---

# Environment Configuration

Create a `.env` file in the project's root directory.

```env
GROQ_API_KEY=your_actual_groq_api_key_here
```

## Security Note

Never commit your `.env` file to GitHub.

Add it to your `.gitignore` file:

```gitignore
.env
```

---

# Running the Application

Run the application using:

```bash
python main.py
```

---

# How It Works

The application follows a simple LangChain pipeline:

1. **Load Environment Variables**

   - `load_dotenv()` loads the `GROQ_API_KEY` from the `.env` file.

2. **Initialize the Language Model**

   - Creates a `ChatGroq` instance using the `llama-3.3-70b-versatile` model.
   - Uses `temperature=0` to produce deterministic and factual summaries.

3. **Create the Prompt**

   - `ChatPromptTemplate` instructs the model to:
     - Read the article
     - Extract only the important information
     - Return concise bullet points

4. **Parse the Output**

   - `StrOutputParser` converts the model response into a plain string.

5. **Execute the Chain**

   - The components are connected using LCEL:

```python
prompt | model | parser
```

   - The chain is executed with:

```python
chain.invoke({"article": article})
```

---

# Customization

## Change the Model

Replace:

```python
llama-3.3-70b-versatile
```

with any Groq-supported model, for example:

- `llama3-8b-8192`
- `mixtral-8x7b-32768`
- `gemma2-9b-it`

---

## Modify the Prompt

You can customize the prompt to generate different types of outputs, such as:

- Executive summaries
- Beginner-friendly (ELI5) explanations
- Detailed summaries
- Technical summaries
- Numbered lists instead of bullet points

Simply edit the template passed to:

```python
ChatPromptTemplate.from_template(...)
```

---

# Technologies Used

- Python
- LangChain
- LangChain Expression Language (LCEL)
- Groq API
- Llama 3.3 70B Versatile
- python-dotenv

---
