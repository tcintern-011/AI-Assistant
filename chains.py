from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from prompts import executive_brief, key_points, explaintochild, executive_brief_reviewer, key_points_reviewer, childexp_reviewer
from models import model
from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()

exec_chain = (
    RunnablePassthrough.assign(draft = executive_brief|model|parser)
    |executive_brief_reviewer|model|parser)
kp_chain = (
    RunnablePassthrough.assign(draft = key_points|model|parser)
    |key_points_reviewer|model|parser)
child_chain = (
    RunnablePassthrough.assign(draft = explaintochild|model|parser)
    |childexp_reviewer|model|parser)

parallel_chain = RunnableParallel(
    executive = exec_chain, 
    keypoints = kp_chain, 
    child = child_chain
)



