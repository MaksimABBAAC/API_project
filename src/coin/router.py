from fastapi import APIRouter

from src.coin.init import cmc_client

router = APIRouter(
    prefix="/cryptocurrencies",
    tags=["Coin"]
)


@router.get("")
async def get_cryptocurrencies():
    return await cmc_client.get_listings()


@router.get("/{currency_id}")
async def get_cryptocurrencies(currency_id: int):
    return await cmc_client.get_currency(currency_id)
