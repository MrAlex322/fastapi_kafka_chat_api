import pytest

from domain.entities.messages import Chat
from infra.repositories.message import BaseChatRepository
from logic.commands.messages import CreateChatCommand
from logic.mediator import Mediator

@pytest.mark.asyncio
async def create_test_chat_command_success(
    chat_repository: BaseChatRepository, 
    mediator: Mediator
):
    chat: Chat = (await mediator.handle_command(CreateChatCommand(title='testTitle')))[0]
    
    assert chat_repository.check_chat_exists_by_title(title=chat.title.as_generic_type())