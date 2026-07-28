from langchain_core.prompts import ChatPromptTemplate

executive_brief = ChatPromptTemplate.from_template(
        "You are a concise executive assistant. Summarize the following article in "
        "exactly 2-3 high-level sentences focusing on business impact:\n\n{article}"
    )
key_points = ChatPromptTemplate.from_template(
        "Extract the top 3-5 key takeaways from this article using bullet points with "
        "bold headers for each bullet:\n\n{article}"
    )
explaintochild = ChatPromptTemplate.from_template(
        "Summarize the main idea of this article using simple analogies and language "
        "a 10-year-old could easily understand:\n\n{article}"
    )