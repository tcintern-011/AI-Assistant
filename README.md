# AI Article Summarizer (LangChain + Groq)

A lightweight Python application that demonstrates how to build **multiple AI-powered article summarizers** using **LangChain's LCEL (LangChain Expression Language)** and **Groq's Llama 3.3 model**.

The application generates multiple summaries of the same article using different prompt templates:

* **Executive Brief** – Professional summary for decision-makers.
* **Key Points** – Concise bullet-point summary.
* **Explain to a Child** – Simple explanation using easy language.

The project is intentionally modular to demonstrate good software organization practices when working with LangChain.

---

# Features

* Modular project architecture
* Powered by Groq's **Llama 3.3 70B Versatile** model
* Uses LangChain Expression Language (LCEL)
* Multiple Prompt Templates
* Output parsing using `StrOutputParser`
* Environment variable support with `.env`
* Clean and beginner-friendly codebase

---

# Project Structure

```text
article-summarizer/
│
├── .env
├── main.py
├── config.py
├── models.py
├── prompts.py
├── requirements.txt
├── README.md
│
└── __pycache__/
```

## File Responsibilities

### `main.py`

Application entry point.

* Creates the parser
* Builds the LangChain pipeline
* Invokes the model
* Displays generated summaries

---

### `config.py`

Loads environment variables.

Example responsibilities:

* Load `.env`
* Configure application settings

---

### `models.py`

Creates and exports the configured LangChain chat model.

Example:

* Initialize `ChatGroq`
* Configure model name
* Configure temperature

---

### `prompts.py`

Stores all prompt templates used by the application.

Current prompts include:

* Executive Brief
* Key Points
* Explain to a Child

Adding new summarization styles only requires creating another prompt here.

---

# How It Works

```
                Article
                   │
                   ▼
           Prompt Template
                   │
                   ▼
             ChatGroq Model
                   │
                   ▼
          StrOutputParser
                   │
                   ▼
            Final Summary
```

The application loops through multiple prompt templates and generates different summaries of the same article.

---

# Installation

## 1. Clone the Repository

```bash
git clone <repository-url>
```

```bash
cd article-summarizer
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

### Linux / macOS

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Create a `.env` File

```text
GROQ_API_KEY=your_groq_api_key_here
```

Replace the value with your Groq API key.

---

## 5. Run the Application

```bash
python main.py
```

---

# Example Output

```
==============================
EXECUTIVE BRIEF
==============================

Sleep is an active biological process essential for memory formation,
brain maintenance, and emotional regulation...

==============================
KEY POINTS
==============================

• Converts short-term memories into long-term memories

• Removes toxic waste from the brain

• Improves emotional regulation

• Reduces stress hormone levels

==============================
EXPLAIN TO A CHILD
==============================

Think of your brain like a classroom that gets messy during the day.
When you sleep, your brain cleans the classroom, organizes everything
you learned, and gets ready for tomorrow.
```

---

# Technologies Used

* Python 3.11+
* LangChain
* LangChain Core
* LangChain Groq
* Groq API
* python-dotenv

---

# LangChain Concepts Demonstrated

This project demonstrates several important LangChain concepts:

* Chat Models
* Prompt Templates
* LCEL Pipelines
* Runnable Interface
* `invoke()`
* Output Parsers
* Environment Variable Management

---

# Learning Objectives

This project is ideal for beginners learning:

* LangChain fundamentals
* LCEL syntax (`|`)
* Prompt engineering
* Modular Python architecture
* Working with LLM APIs
* Environment configuration using `.env`

---
