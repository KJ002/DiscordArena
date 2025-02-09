from discord.ext.commands import Cog, command, Context

from arena_bot import ArenaBot
from models import ItemFactory, ItemType


class Development(Cog):
    """
    Cog that holds development tools, this isn't loaded in Production.

    Feel free to add any useful commands that will help with development.
    """

    def __init__(self, bot: ArenaBot):
        self.bot = bot

    @command()
    async def random_item(self, ctx: Context):
        """Generate a random item for the author."""
        item = await ItemFactory.random(ctx.author.id, item_type=ItemType.Weapon.value)
        await ctx.reply(embed=await item.embed)

    @command()
    async def random_chest(self, ctx: Context):
        """Generate a random item for the author."""
        item = await ItemFactory.random(ctx.author.id, name="RandomChest", item_type=ItemType.Chest.value)
        await ctx.reply(embed=await item.embed)

    @command()
    async def reload_tables(self, ctx: Context) -> None:
        """Drop and create all the tables."""
        self.bot.database.drop_all_tables()
        self.bot.database.create_all_tables()

    @command()
    async def ping(self, ctx: Context) -> None:
        """Sends the ping in ms."""
        await ctx.send(f"Ping is {round(self.bot.latency * 1000)}ms")


def setup(bot: ArenaBot) -> None:
    """Add the cog"""
    bot.add_cog(Development(bot))


def teardown(bot: ArenaBot) -> None:
    """Remove the cog"""
    bot.remove_cog("Development")
