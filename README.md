# StacheBot
StacheBot is a Discord made in python for the Handlebar Community from
Lords of Minecraft.

## Commands
Commands are broken down into categories, aka 'cogs' by the Discord.py package.
### Minecraft
#### status [optional: server ip]
The status command provided without any additional arguments provides
the status for the default Minecraft server defined in the
`DEFAULT_MC` environmental variable. The `server ip` argument when
provided will provide the status for any Minecraft server.
### WolframAlpha
#### WolframAlpha [query]
This command utilizes the Wolfram Alpha Short answer API to provide a (usually) suitable response.

## Moderation Tools
### Automove on Deafen
Per the request of Chicka, self deafening in any channel other than
the AFK channel will automatically move the user to the AFK channel.
Users will also be automatically moved back to the AFK channel if they
move to any channel from AFK while still deafened.

## Planned Additions
 - Image and message moderation tools
