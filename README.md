# WGClient
## under construction
## Usage
```py
import WGClient
client=WGClient.Client(application_id,"en")
client.wows.get_player
. . .
```
### Client
`application_id`:str: literal

`lang`:str: your language (country code)

`conv`:bool:
If `True` passed,convert dictionary to `convdict.Dict`.

You can use like this.
```py
get_ship("yamato").origin
>>>{"name":"yamato","details":{"some":"aaaa"}}
get_ship("yamato").value.details.some
>>>aaaa
```
Default is `False`.

### WowsApp
#### get_user
:return: Player object

You can get original returned dict from WGapi by `get_user.origin`
#### get_ship
:return: Ship object

same
#### get_arena
:return: Arena object

same
### Player
#### get_ships
