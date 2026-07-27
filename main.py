from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(
    model = "llama-3.3-70b-versatile", 
    temperature = 0
)

parser = StrOutputParser()

prompt = ChatPromptTemplate.from_template(
    """
    summarize the following article. 
    The summary needs to be: 
    - concise and Brief
    - keep only important facts and figures
    - give bullet points
    
    Article: 

    {article}
    """
)

chain = prompt | model | parser

article = """
Here is the article formatted entirely as continuous paragraphs:
## The Science of Sleep: Why Your Brain Needs Rest
We often view sleep as a passive state where the body simply turns off for the night. However, modern neuroscience shows that the brain remains remarkably active during sleep, carrying out essential maintenance tasks that keep us physically and mentally healthy.
Throughout the day, your brain absorbs vast amounts of information. During deep sleep, it converts these temporary short-term thoughts into long-term memories, helping you retain what you learned. At the same time, a biological cleanup mechanism known as the glymphatic system activates. This system flushes out toxic waste products, such as proteins linked to neurodegenerative diseases, that accumulate while you are awake.
Beyond memory consolidation and physical cleanup, rest allows the brain to process emotions and regulate mood-altering chemicals. A lack of sleep spikes stress hormones like cortisol, making emotional self-regulation much harder. Ultimately, sleep is far from passive downtime—it is a vital, active process that repairs, cleanses, and prepares your mind for the day ahead.
"""


summary = chain.invoke({"article": article})

print("====SUMMARY=====")
print(summary)
