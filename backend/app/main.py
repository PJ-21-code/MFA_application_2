from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.api.deps import get_current_user

app= FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173","http://127.0.0.1:5173","http://localhost:5174"], # frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/dashboard-data")
async def get_dashboard_data(user_payload: dict= Depends(get_current_user)):
    return {
        "message": "Yor are authorized",
        "user_id": user_payload.get("sub"),
        "data": "Here is your dashboard data"
    }
