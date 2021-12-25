import pytest

from orchd_sdk.reaction import Event, ReactionTemplate
from orchd_reactions.docker import ContainerRunReactionHandler


@pytest.fixture()
def sample_reaction():
    return ReactionTemplate(name="ContainerTestReaction",
                            handler="ContainerRunReactionHandler",
                            triggered_on=["some_event"],
                            handler_parameters=dict(), active=True)


class TestContainerRunReactionHandler:

    @pytest.mark.asyncio
    async def test_handler(self, sample_reaction):
        handler = ContainerRunReactionHandler()

        f = handler.handle(Event("SomeEvent", dict()), sample_reaction)
        print("Async checked!")
        await f

