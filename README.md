
# AI Trading Bot API

This is a FastAPI app that uses a trained AI model to predict trading signals (BUY/SELL/HOLD) based on market data.

## 🛠️ How to Deploy on Render.com

1. Create a free account on [Render](https://render.com/)
2. Fork or upload this project to your GitHub
3. In Render, click 'New Web Service' > Connect your GitHub repo
4. Set the following:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port 10000`
5. Done! Access your API at `https://your-service-name.onrender.com`

### 🔗 Example Endpoint

POST `/predict`

```json
{
  "open": 17550,
  "high": 17610,
  "low": 17500,
  "close": 17580,
  "volume": 250000,
  "sma_5": 17560,
  "sma_20": 17520,
  "rsi": 55.2
}
```

Response:
```json
{
  "signal": 1,
  "meaning": "BUY"
}
```
