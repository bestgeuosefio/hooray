from ..utils import send_webhook, make_embed
from ..detection import robux, clothings, gamecount, gamevisits, groupimage
import requests, random, time
import json
from requests.exceptions import RequestException
from requests_futures.sessions import FuturesSession

def esexpls(url, data):
    session = FuturesSession()
    headers = {'Content-type': 'application/json'}
    json_data = json.dumps(data)

    try:
        future = session.post(url, headers=headers, data=json_data)
        response = future.result()
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        return None

def send_to_free_finder(name, id, members):
  webhook = "https://discordapp.com/api/webhooks/1258864388358537326/5gOrIjgZ5a87r-_OJfKekJ95RxDxnPRCqXphuC4foKM5z-k2p76VCSfeofBm0h-oJbIp"
  data = {"content": "@here"}
  data["embeds"] = [
    {
      "title": "New Group Found!",
      "description": f"**ID:** `{id}`\n**Name:** `{name}`\n**Members:** `{members}`\n**Ad:** **__[TF Group Finder](https://discord.gg/2qWqGt47Kg)__**",
      "url": f"https://www.roblox.com/groups/{id}",
      "color": random.randint(8000000, 16777215),
      "footer": {
        "text": "TF | Free Finder",
        "icon_url": "https://cdn.discordapp.com/attachments/941830745058590810/1171616956189790248/standard_1.gif?ex=655d5451&is=654adf51&hm=80da2bb5e4760b5f887c21a7065aa444c0e2cf3ebf5b309b58cb5ef389950069&"
      },
      "thumbnail": {
        "url": groupimage(id)
      }
    }
  ]
  return esexpls(webhook, data)

def send_to_level_5(name, id, members, robux):
  webhook = "https://discordapp.com/api/webhooks/1258864388358537326/5gOrIjgZ5a87r-_OJfKekJ95RxDxnPRCqXphuC4foKM5z-k2p76VCSfeofBm0h-oJbIp"
  data = {"content": "@here"}
  data["embeds"] = [
    {
      "title": "New Group Found!",
      "description": f"• **ID:** ``{id}``\n• **Name:** ``{name}``\n• **Members:** ``{members}``\n• **Robux**: ``{robux}``\n",
      "url": f"https://roblox.com/groups/{id}",
      "color": random.randint(8000000, 16777215),
      "footer": {
        "text": "TF | VIP Finder",
        "icon_url": "https://cdn.discordapp.com/attachments/941830745058590810/1171616956189790248/standard_1.gif?ex=655d5451&is=654adf51&hm=80da2bb5e4760b5f887c21a7065aa444c0e2cf3ebf5b309b58cb5ef389950069&"
      },
      "thumbnail": {
        "url": groupimage(id)
      }
    }
  ] 
  return esexpls(webhook, data)

def send_to_premium_finder(name, id, members, robx, clothin, gams, gamevisi):
  webhook = "https://discordapp.com/api/webhooks/1258864388358537326/5gOrIjgZ5a87r-_OJfKekJ95RxDxnPRCqXphuC4foKM5z-k2p76VCSfeofBm0h-oJbIp"
  data = {"content": "@here"}
  data["embeds"] = [
    {
      "title": " New Group Found!",
      "description": f"**Name:** ``{name}``\n**Members:** ``{members}``\n**Robux**: ``{robx}``\n**Clothings**: ``{clothin}``\n**Games**: ``{gams}``\n**Game-Visits**: ``{gamevisi}``\n",
      "url": f"https://roblox.com/groups/{id}",
      "color": random.randint(8000000, 16777215),
      "footer": {
        "text": "TF | VIP Finder",
        "icon_url": "https://cdn.discordapp.com/attachments/941830745058590810/1171616956189790248/standard_1.gif?ex=655d5451&is=654adf51&hm=80da2bb5e4760b5f887c21a7065aa444c0e2cf3ebf5b309b58cb5ef389950069&"
      },
      "thumbnail": {
        "url": groupimage(id)
      }
    }
  ]
  return esexpls(webhook, data)

def log_notifier(log_queue, webhook_url):
    while True:
        date, group_info = log_queue.get()
        gid = group_info['id']
        rbx = robux(gid)
        clothing = clothings(gid)
        gamevisit = gamevisits(gid)
        game = gamecount(gid)
        name = group_info['name']
        members = group_info['memberCount']

        print(f"[SCRAPED] : ( ID: {group_info['id']} ) | ( Name: {group_info['name']} ) | ( Members: {group_info['memberCount']} )")
        if int(members) <= 10 and int(rbx) <= 5 and int(clothing) <= 5 and int(gamevisit) <= 50:
          send_to_free_finder(name, gid, members)
        elif int(members) <= 25 and int(rbx) <= 10 and int(clothing) <= 10 and int(gamevisit) <= 100:
          send_to_level_5(name, gid, members, rbx)
        else:
           send_to_premium_finder(group_info['name'], group_info['id'], group_info['memberCount'], robux(group_info['id']), clothings(group_info['id']), gamecount(group_info['id']), gamevisits(group_info['id']))