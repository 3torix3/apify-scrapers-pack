"""LangGraph ReAct agent that can search the web (as Markdown) and read YouTube transcripts.

Usage: APIFY_API_TOKEN=... ANTHROPIC_API_KEY=... python langchain_agent.py "your question"
"""
import sys

from langchain_anthropic import ChatAnthropic
from langchain_apify import ApifyActorsTool
from langgraph.prebuilt import create_react_agent

tools = [
    ApifyActorsTool("murch1k/rag-web-search"),             # web search results with page content as Markdown
    ApifyActorsTool("murch1k/youtube-transcript-scraper"),  # transcripts of videos, channels, playlists
]
agent = create_react_agent(ChatAnthropic(model="claude-sonnet-5-5"), tools)

question = " ".join(sys.argv[1:]) or "What are people saying about pgvector vs Qdrant? Cite sources."
for step in agent.stream({"messages": [("user", question)]}, stream_mode="values"):
    step["messages"][-1].pretty_print()
