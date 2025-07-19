
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

model = joblib.load("ai_trading_model.pkl")
app = FastAPI(title="AI Trading Signal API")

class MarketData(BaseModel):
    open: float
    high: float
    low: float
    close: float
    volume: float
    sma_5: float
    sma_20: float
    rsi: float

@app.get("/status")
def read_root():
    return {"status": "AI Trading API is running"}

@app.post("/predict")
def predict_signal(data: MarketData):
    try:
        features = np.array([[data.open, data.high, data.low, data.close,
                              data.volume, data.sma_5, data.sma_20, data.rsi]])
        signal = model.predict(features)[0]
        meaning = {1: "BUY", 0: "HOLD", -1: "SELL"}[signal]
        return {"signal": signal, "meaning": meaning}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
