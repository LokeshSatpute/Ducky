from typing import Optional

import aitools_autogen.utils as utils
from aitools_autogen.agents import WebPageScraperAgent
from aitools_autogen.blueprint import Blueprint
from aitools_autogen.config import llm_config_openai as llm_config, config_list_openai as config_list, WORKING_DIR
from autogen import ConversableAgent

class CodeSolvingBlueprint(Blueprint):

    def __init__(self, work_dir: Optional[str] = WORKING_DIR):
        super().__init__([], config_list=config_list, llm_config=llm_config)
        self._work_dir = work_dir or "code"
        self._summary_result: Optional[str] = None

    @property
    def summary_result(self) -> str | None:
        """The getter for the 'summary_result' attribute."""
        return self._summary_result

    @property
    def work_dir(self) -> str:
        """The getter for the 'work_dir' attribute."""
        return self._work_dir

    async def initiate_work(self, message: str):
        utils.clear_working_dir(self._work_dir)
        agent0 = ConversableAgent("a0",
                                  max_consecutive_auto_reply=0,
                                  llm_config=False,
                                  human_input_mode="NEVER")

        scraper_agent = WebPageScraperAgent()

        summary_agent = ConversableAgent("summary_agent",
                                         max_consecutive_auto_reply=6,
                                         llm_config=llm_config,
                                         human_input_mode="NEVER",
                                         code_execution_config=False,
                                         function_map=None,
                                         system_message="""
You are an automated summary agent designed to assist in summarizing tasks and outcomes related to coding and website tasks.

Your role is to provide concise summaries of tasks and results for clarity and easy understanding.

When receiving a message, analyze the content and generate a summary that captures the key points or results related to coding problems, website cloning, and sitemap generation.

Your summaries should be clear, informative, and tailored to the context of the task at hand, whether it's solving coding problems or automating website-related tasks.

Avoid unnecessary details and focus on presenting the most relevant information.

Your primary goal is to facilitate communication and decision-making by providing effective summaries of coding tasks, website cloning processes, and sitemap generation outcomes.

""")

        coder_agent = ConversableAgent("coder_agent",
                                                max_consecutive_auto_reply=6,
                                                llm_config=llm_config,
                                                human_input_mode="NEVER",
                                                code_execution_config=False,
                                                function_map=None,
                                                system_message="""
        You are a developer proficient in Programming, with experience in solving coding problems from platforms like LeetCode or HackerRank.

You're tasked with solving the coding problem provided in the URL and generating two coding files.

When you receive a URL pointing to a coding problem, you should solve the problem and generate two Python files one with the main solution and other with an alternative solution.

Also generate two files splitting the solution into two parts based on different functionalities or components of the solution

Write a complete implementation of the solution before saving it into a file. Make sure to include comments for clarity and readability.

Ensure that each Python file contains the necessary imports and functions to execute the solution independently.

You must indicate the script type in the code block. Do not suggest incomplete code which requires users to modify. Always put `# filename: <directory>/<filename>` as the first line of each code block.

Feel free to include multiple code blocks in one response. Do not ask users to copy and paste the result.""")

        agent0.initiate_chat(scraper_agent, True, True, message=message)

        message = agent0.last_message(scraper_agent)

        agent0.initiate_chat(summary_agent, True, True, message=message)

        message = agent0.last_message(summary_agent)

        agent0.initiate_chat(coder_agent, True, True, message=message)

        llm_message = agent0.last_message(coder_agent)["content"]
        utils.save_code_files(llm_message, self.work_dir)

        self._summary_result = utils.summarize_files(self.work_dir)


if __name__ == "__main__":
    import asyncio

    task = """
    I want to get the solution for the following coding question.
    https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
    """
    blueprint = CodeSolvingBlueprint()
    asyncio.run(blueprint.initiate_work(task))
    print(blueprint.summary_result)

