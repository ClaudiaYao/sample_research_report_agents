import asyncio

# import config
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.sessions import Session

import logging
from utils import pprint_events, call_agent
from agent_fleet.agent_team import interactive_planner_agent

logging.basicConfig(level=logging.ERROR)

app_name = "deep_research_agent"
session_id ="session12345"
user_id ="user12345"
    

async def create_session(runner, session_id) -> Session:
    session = await runner.session_service.create_session(app_name=app_name, user_id=user_id, session_id=session_id, state={"initial": "state"})
    return session


async def run():
    session_service = InMemorySessionService()
    
    runner = Runner(agent=interactive_planner_agent, app_name="deep_research_agent", session_service=session_service)
    session = await create_session(runner, session_id="session12345")

    print("call agent with query: hello")
    events = await call_agent(runner, "hello", user_id="user12345", session_id=session_id)
    pprint_events(events)
    session = await runner.session_service.get_session(app_name=app_name, user_id=user_id, session_id=session_id)
    print(session.state)

    print("----------------------------------")
    print("call agent with query: What can you do")
    events = await call_agent(runner, "What can you do", user_id="user12345", session_id=session_id)
    pprint_events(events)
    session = await runner.session_service.get_session(app_name=app_name, user_id=user_id, session_id=session_id)
    print(session.state)

    print("----------------------------------")
    print("call agent with query: Help me research the weather trend in Singapore")
    events = await call_agent(runner, "Help me research the weather trend in Singapore", user_id="user12345", session_id=session_id)
    pprint_events(events)
    session = await runner.session_service.get_session(app_name=app_name, user_id=user_id, session_id=session_id)   
    print(session.state)    
    
    print("----------------------------------")
    print("call agent with query: Simplify it, 3 research point and 1 deliverable will do")
    events = await call_agent(runner, "Simplify it, 3 research point and 1 deliverable will do", user_id="user12345", session_id=session_id)
    pprint_events(events)
    session = await runner.session_service.get_session(app_name=app_name, user_id=user_id, session_id=session_id)
    print(session.state)

    print("----------------------------------")
    print("call agent with query: Lets go")
    events = await call_agent(runner, "Lets go", user_id="user12345", session_id=session_id)
    pprint_events(events)   
    session = await runner.session_service.get_session(app_name=app_name, user_id=user_id, session_id=session_id)
    print(session.state)
    
if __name__ == "__main__":
    asyncio.run(run())