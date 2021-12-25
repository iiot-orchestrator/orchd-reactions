import docker
import asyncio

from orchd_sdk.reaction import Event, ReactionHandler, Reaction


class ContainerRunReactionHandler(ReactionHandler):

    def handle_error(self) -> None:
        pass

    async def handle(self, event: Event, reaction: Reaction):
        def task():
            client = docker.from_env()
            client.containers.run('alpine', 'echo Hello World!')
            client.close()

        await asyncio.get_running_loop().run_in_executor(None, task)
