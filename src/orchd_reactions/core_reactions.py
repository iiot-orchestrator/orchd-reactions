from orchd_sdk.event import ReactionHandler
from orchd_sdk.models import ReactionTemplate, Event
from orchd_sdk.logging import logger

from rx.subject import Subject


class HttpEventStreamerReactionHandler(ReactionHandler):
    """
    Capture all events and publishes on a Singleton subject.

    This Handler is responsible for forwarding events to event stream requests.
    When a event stream requests arrives a subscription to
    HttpEventStreamerReactionHandler.events is made, then the request
    handler can access the events in the system.
    """
    events = Subject()

    template = ReactionTemplate(
        id='4d3aba04-a303-4793-b35a-afcf60668d58',
        name='io.orchd.reactions.core.HttpEventStreamer',
        version='1.0',
        handler='orchd_reactions.core.HttpEventStreamerReactionHandler',
        triggered_on=[''],
        handler_parameters=dict(),
        active=True
    )

    def handle(self, event: Event, reaction: ReactionTemplate) -> None:
        """
        Handles the event by publishing it on the Subject.
        :param event: The event being handled
        :param reaction: The reaction template.
        """
        logger.info(f"{self.__class__.__name__}: Event {event.id} captured and handled.")
        HttpEventStreamerReactionHandler.events.on_next(event)
