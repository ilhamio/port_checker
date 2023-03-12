from application.pkg.entities import commands

__all__ = ['nothing']


async def nothing(_: commands.NotValidRowCommand, *args, **kwargs):
    """
    Function for invalid rows in csv file
    :param _:
    :return:
    """
    return None
