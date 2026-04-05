from a2a.types import AgentCard, AgentSkill, AgentCapabilities
from agent_executor import GreetingAgentExecutor
import uvicorn


def main():

    greeting_skill = AgentSkill(
        id = "hello_world",
        name = "Greet",
        description = "Return a greeting",
        tags = ["Hey", "Hii", "Hello"]
    )

    agent_card = AgentCard(
        name = "Greeting Agent",
        description = "A Simple agent that returns a greeting",
        url="http://localhost:9999/",
        default_input_modes=["text"],
        default_output_modes=["text"],
        skills=[greeting_skill],
        version="1.0.0",
        capabilities=AgentCapabilities()
    )
    
    # request handler (waiter)
    from a2a.server.request_handlers import DefaultRequestHandler
    from agent_executor import GreetingAgentExecutor
    from a2a.server.tasks import InMemoryTaskStore

    request_handler = DefaultRequestHandler(
        agent_executor = GreetingAgentExecutor(),
        task_store = InMemoryTaskStore()
    )

    # server
    from a2a.server.apps import A2AStarletteApplication
    server = A2AStarletteApplication(
        http_handler = request_handler,
        agent_card = agent_card
    )

    uvicorn.run(server.build(), host="0.0.0.0", port=9999)

if __name__ == "__main__":
    main()