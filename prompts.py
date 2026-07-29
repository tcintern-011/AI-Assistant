from langchain_core.prompts import ChatPromptTemplate

executive_brief = ChatPromptTemplate.from_template(
    """
        You are a concise executive assistant. Summarize the following article in "
        exactly 2-3 high-level sentences focusing on business impact:
        
        Article: 
        {article}
        
        Example output: 
        
        Sleep is an active biological process essential for memory formation,
        brain maintenance, and emotional regulation...
        
        **STRICTLY FOLLOW THIS FORMAT**
        
        """
    )
key_points = ChatPromptTemplate.from_template(
    """
        Extract the top 3-5 key takeaways from this article using bullet points with "
        bold headers for each bullet:
        
        Article:
        {article}
        
        Example Output: 
        
        • Converts short-term memories into long-term memories

        • Removes toxic waste from the brain

        • Improves emotional regulation

        • Reduces stress hormone levels
        
        **STRICTLY FOLLOW THIS FORMAT**
        
        """
        
    )
explaintochild = ChatPromptTemplate.from_template(
        """ Summarize the main idea of this article using simple analogies and language
            a 10-year-old could easily understand:
            
            Article:  
            {article}
            
            Example Output:
             
            Think of your brain like a classroom that gets messy during the day.
            When you sleep, your brain cleans the classroom, organizes everything
            you learned, and gets ready for tomorrow.

            **STRICTLY FOLLOW THIS FORMAT**

        """
    )


executive_brief_reviewer = ChatPromptTemplate.from_template("""
You are an expert editor reviewing an executive brief.

Review the executive brief using the following criteria:

- Exactly 2-3 sentences.
- Focuses on business impact.
- Concise and professional.
- Factually accurate.
- Omits unnecessary technical details.

Article:
{article}

Example Output:
    
==============================
EXECUTIVE SUMMARY
==============================

Executive Brief:
{draft}

Return:

Score: /10

Strengths:
- ...

Weaknesses:
- ...

Suggested Improvements:

**STRICTLY FOLLOW THIS FORMAT**

- ...
""")

key_points_reviewer = ChatPromptTemplate.from_template("""
You are reviewing extracted key points.

Review using these criteria:

- Contains 3-5 bullet points.
- Includes the most important ideas.
- Each bullet is concise.
- No duplicate information.
- Uses bold headers.
- Factually correct.

Article:
{article}

Example Output:   
   
==============================
KEY POINTS
==============================

Key Points:
{draft}

Return:

Score: /10

Missing Points:
...

Redundant Points:
...

Suggestions:
...

**STRICTLY FOLLOW THIS FORMAT**

""")

childexp_reviewer = ChatPromptTemplate.from_template("""
You are reviewing an explanation written for a 10-year-old.

Review using these criteria:

- Easy for a child to understand.
- Uses simple words.
- Uses helpful analogies.
- Avoids technical jargon.
- Remains factually correct.
- Fun and engaging.

Article:
{article}

Example Output: 

==============================
EXPLAIN TO A CHILD
==============================

Explanation:
{draft}

Return:

Score: /10

Hard Words:
...

Confusing Parts:
...

Suggestions:
...

**STRICTLY FOLLOW THIS FORMAT**

""")