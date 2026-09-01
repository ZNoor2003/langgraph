from dotenv import load_dotenv
load_dotenv()
from langchain_core.tools import StructuredTool
from langchain_community.tools import DuckDuckGoSearchResults
from langgraph.prebuilt import ToolNode
from schemas import AnswerQuestion, ReviseAnswer

duckduckgo_tool = DuckDuckGoSearchResults(num_results=5)

def run_queries(search_queries: list[str], **kwargs):
    """Run the generated queries."""
    return duckduckgo_tool.batch(search_queries)

execute_tools = ToolNode(
    [
        StructuredTool.from_function(run_queries, name=AnswerQuestion.__name__),
        StructuredTool.from_function(run_queries, name=ReviseAnswer.__name__),
    ]
)