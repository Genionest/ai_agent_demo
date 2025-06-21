from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.agent import AgentRunResult
import tools
from dotenv import load_dotenv
import os 

load_dotenv()

model = OpenAIModel(
    "deepseek-chat",
    provider=OpenAIProvider(
        api_key = os.getenv("DEEPSEEK_API_KEY"),
        base_url = "https://api.deepseek.com"
    )
)

agent = Agent(
    model,
    system_prompt = "你是一个资深的程序员",
    tools = [
        tools.read_file,
        tools.list_files,
        tools.rename_file,
    ],
)

def main() -> None:
    print(tools.list_files())
    history:list[str] = []
    while True:
        user_input:str = input("Input: ")
        resp:AgentRunResult[str] = agent.run_sync(user_input,
                                                message_history=history)
        history = list(resp.all_messages())
        print(resp.output)

if __name__ == "__main__":
    main()
