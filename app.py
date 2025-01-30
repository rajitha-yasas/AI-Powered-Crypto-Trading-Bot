import os
import requests
import time
import ollama
from web3 import Web3
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
DEXSCREENER_API_URL = "https://api.dexscreener.com/latest/dex/tokens/"
INFURA_API_KEY = os.getenv("INFURA_API_KEY")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
TOKEN_ADDRESS = os.getenv("TOKEN_ADDRESS")

app = Flask(__name__)

# Connect to Ethereum blockchain
w3 = Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{INFURA_API_KEY}"))

def get_token_data(token_address):
    response = requests.get(f"{DEXSCREENER_API_URL}{token_address}")
    if response.status_code == 200:
        return response.json()
    return None

def filter_token_data(token_info):
    try:
        liquidity = float(token_info["pairs"][0]["liquidity"]["usd"])
        volume_24h = float(token_info["pairs"][0]["volume"]["h24"])
        if liquidity > 50000 and volume_24h > 100000:
            return True
    except:
        return False
    return False

def analyze_trading_pattern(trade_history):
    prompt = f"Analyze this trading history and check if the volume looks manipulated: {trade_history}"
    response = ollama.chat(model="deepseek-coder", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]

def detect_rug_pull(token_info):
    liquidity_change = float(token_info["pairs"][0]["liquidity"]["usd_change"])
    return liquidity_change < -50

def execute_trade(token_address, amount_eth):
    # Implement trade execution using Web3
    pass

@app.route("/api/check", methods=["GET"])
def check_token():
    token_info = get_token_data(TOKEN_ADDRESS)
    if not token_info:
        return jsonify({"error": "Invalid token or API error"}), 400

    if filter_token_data(token_info) and not detect_rug_pull(token_info):
        trade_decision = analyze_trading_pattern(token_info)
        return jsonify({"status": "Safe to trade" if "safe to trade" in trade_decision.lower() else "Risky trade"})
    return jsonify({"status": "Not meeting trade criteria"})

@app.route("/api/trade", methods=["POST"])
def trade():
    data = request.json
    amount_eth = data.get("amount_eth", 0.1)
    execute_trade(TOKEN_ADDRESS, amount_eth)
    return jsonify({"status": "Trade executed"})

if __name__ == "__main__":
    app.run(debug=True)
