import configs.config as config

def owner(ctx):
    return ctx.author.id == int(config.DISCORD_OWNER_ID)