from langchain_core.prompts import ChatPromptTemplate

executive_brief = ChatPromptTemplate.from_template(
    """
        You are a concise executive assistant. Summarize the following article in "
        exactly 2-3 high-level sentences focusing on business impact:
        
        Article: 
        {article}
        
        Example output: 
        ==============================
        EXECUTIVE BRIEF
        ==============================
        Sleep is an active biological process essential for memory formation,
        brain maintenance, and emotional regulation...
        """
    )
key_points = ChatPromptTemplate.from_template(
    """
        Extract the top 3-5 key takeaways from this article using bullet points with "
        bold headers for each bullet:
        
        Article:
        {article}
        
        Example Output: 
        ==============================
        KEY POINTS
        ==============================

        • Converts short-term memories into long-term memories

        • Removes toxic waste from the brain

        • Improves emotional regulation

        • Reduces stress hormone levels
        """
        
    )
explaintochild = ChatPromptTemplate.from_template(
        """ Summarize the main idea of this article using simple analogies and language
            a 10-year-old could easily understand:
            
            Article:  
            {article}
            
            Example Output: 
            
            ==============================
            EXPLAIN TO A CHILD
            ==============================

            Think of your brain like a classroom that gets messy during the day.
            When you sleep, your brain cleans the classroom, organizes everything
            you learned, and gets ready for tomorrow.
        """
    )