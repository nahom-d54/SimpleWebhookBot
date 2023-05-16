from flask import Flask, request
import requests
import asyncio
import os

app = Flask(__name__)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_URL = os.environ.get("API_URL")


app.route("/webhook",methods=["POST"])
def webhook():
  json_data = request.get_json()["message"]
  text = json_data["text"]
  chat_id = json_data["chat"]["id"]
  asyncio.run(mezgebe_kalat(text,chat_id,API_URL,BOT_TOKEN))
  return "OK"
  
