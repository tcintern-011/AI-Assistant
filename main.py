from langchain_core.output_parsers import StrOutputParser
import config
from models import model
from prompts import explaintochild , executive_brief, key_points

parser = StrOutputParser()
prmpts = [executive_brief, key_points, explaintochild]
for prompt in prmpts : 

    chain = prompt | model | parser
    
    # article = """
    # Here is the article formatted entirely as continuous paragraphs:
    # ## The Science of Sleep: Why Your Brain Needs Rest
    # We often view sleep as a passive state where the body simply turns off for the night. However, modern neuroscience shows that the brain remains remarkably active during sleep, carrying out essential maintenance tasks that keep us physically and mentally healthy.
    # Throughout the day, your brain absorbs vast amounts of information. During deep sleep, it converts these temporary short-term thoughts into long-term memories, helping you retain what you learned. At the same time, a biological cleanup mechanism known as the glymphatic system activates. This system flushes out toxic waste products, such as proteins linked to neurodegenerative diseases, that accumulate while you are awake.
    # Beyond memory consolidation and physical cleanup, rest allows the brain to process emotions and regulate mood-altering chemicals. A lack of sleep spikes stress hormones like cortisol, making emotional self-regulation much harder. Ultimately, sleep is far from passive downtime—it is a vital, active process that repairs, cleanses, and prepares your mind for the day ahead.
    # """

    # Another Article can be used to test 
    article = """
    Artificial intelligence is rapidly shifting from centralized cloud data centers to edge devices like smartphones, laptops, and smart home hardware. 
    This trend, known as "Edge AI," allows machine learning models to run directly on local devices without sending data back to distant servers. 
    The main drivers behind this shift are reduced latency, lower bandwidth costs, and enhanced privacy. 
    When data doesn't leave the user's device, sensitivity issues regarding personal information are minimized. 
    However, developers face significant challenges, including memory constraints, battery consumption, and limited computational power on small hardware chips. 
    To address these issues, techniques like model quantization and pruning are being heavily developed to shrink AI models without sacrificing significant performance.
    """


    summary = chain.invoke({"article": article})

    print("\n====SUMMARY=====\n")
    print(summary)
