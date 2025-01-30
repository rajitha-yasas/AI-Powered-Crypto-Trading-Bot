# AI-Powered Crypto Trading Bot

## Overview
This project is a **free AI-powered crypto trading bot** that uses **DeepSeek AI** and **DexScreener API** to analyze and automate cryptocurrency trading. It filters potential trading opportunities, detects fake volumes, prevents rug pulls, and executes trades automatically.

## Features
- 🛠 **Real-time Token Analysis** using DexScreener API
- 🤖 **AI-Powered Trade Analysis** via DeepSeek
- 🔍 **Fake Volume & Rug Pull Detection**
- 🔄 **Automated Trade Execution** with Web3
- 🌐 **Web API for Checking & Executing Trades**

## Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/rajitha-yasas/AI-Powered-Crypto-Trading-Bot.git
cd ai-crypto-trading-bot
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Create & Setup `.env` File
Create a `.env` file in the project directory and add the following:
```
INFURA_API_KEY=your_infura_api_key
PRIVATE_KEY=your_private_key
TOKEN_ADDRESS=your_token_address
```

### 4️⃣ Run the Bot
```sh
python app.py
```

## API Endpoints
| Endpoint       | Method | Description |
|---------------|--------|-------------|
| `/api/check`  | GET    | Checks token status |
| `/api/trade`  | POST   | Executes a trade |

## Future Enhancements 🚀
- Add Stop-Loss and Take-Profit mechanisms
- Implement Telegram notifications
- Create a Web UI Dashboard

## License
This project is open-source and available under the MIT License.

## Author
[Rajitha Pathiraja] - 2025
