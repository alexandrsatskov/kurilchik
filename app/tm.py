"""Task manager for background tasks."""


async def usn():
    """Update-Save-Notify."""
    await update()
    await save()
    await notify()


async def update():
    """
    - Периодическое обновление данных по отслеживаемым адресам
    - Сохранение истории транзакций в реляционную базу данных
    - Простая система оповещений в телеграм о новых транзакциях
    """
    pass


async def save():
    """
    - Сохранение истории транзакций в реляционную базу данных
    """
    pass


async def notify():
    """
    - Простая система оповещений в телеграм о новых транзакциях
    """
    pass
