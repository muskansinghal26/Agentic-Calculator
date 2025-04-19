import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.graph import MessagesState, StateGraph, START  # Importing START
from langgraph.prebuilt import tools_condition, ToolNode
from langchain_core.messages import HumanMessage, SystemMessage
from src.utils import add, subtract, multiply, divide  # Importing arithmetic functions

# Load environment variables from .env file
load_dotenv()

# Retrieve API keys
groq_api_key = os.getenv('GROQ_API_KEY', 'your_default_groq_api_key')
langsmith_api_key = os.getenv('LANGSMITH_API_KEY', 'your_default_langsmith_api_key')

llm = ChatGroq(groq_api_key=groq_api_key, model_name="Gemma2-9b-It")

# Tools
tools = [add, subtract, multiply, divide]

llm_with_tools = llm.bind_tools(tools)

# System Message
sys_msg = SystemMessage(content="You are a helpful assistant tasked with using search and performing arithmetic on a set of inputs.")

# Node
def reasoner(state: MessagesState):
    return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]}

# Building the graph
builder = StateGraph(MessagesState)

# Add Nodes
builder.add_node("reasoner", reasoner)
builder.add_node("tools", ToolNode(tools))  # for the tools

# Add edges
builder.add_edge(START, "reasoner")
builder.add_conditional_edges("reasoner", tools_condition)
builder.add_edge("tools", "reasoner")

react_graph = builder.compile()