from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper


load_dotenv()

@tool
def triple(num:float) -> float:
    """
    param num: a number to triple
    returns: the triple of the input number
    """
    return float(num) * 3

wrapper = DuckDuckGoSearchAPIWrapper(max_results=1)
search_tool = DuckDuckGoSearchRun(api_wrapper=wrapper)

tools = [search_tool, triple]

llm = ChatOpenAI(model="gpt-5.4-mini", temperature=0).bind_tools(tools)



