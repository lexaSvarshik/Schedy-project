from aiogram import Router, F
from aiogram.types import Message, WebAppInfo, PreCheckoutQuery
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config_reader import config

from keyboards import main_markup
from db import User

router = Router(name="common")

markup = (
    InlineKeyboardBuilder()
    .button(text="Open Me", web_app=WebAppInfo(url=config.WEBAPP_URL))
).as_markup()


@router.message(CommandStart())
async def start(message: Message) -> None:
    user = await User.filter(id=message.from_user.id).exists()
    if not user:
        await User.create(id=message.from_user.id, name=message.from_user.first_name)
        
    await message.answer("Open the web app", reply_markup=main_markup)


@router.pre_checkout_query()
async def precheck(event: PreCheckoutQuery) -> None:
    await event.answer(True)


@router.message(F.successful_payment)
async def successful_payment(message: Message) -> None:
    await message.answer("Спасибо за покупку!!!")