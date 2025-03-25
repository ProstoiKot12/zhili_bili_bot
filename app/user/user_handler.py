import asyncio
import os

from aiogram import Bot, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from dotenv import load_dotenv
from aiogram import Router

from content.text.main_text import start_text, answers_questions_text, special_offer_text

from app.keyboards.user_keyboards import main_menu_kb, return_main_menu_kb

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(start_text, reply_markup=main_menu_kb)


@router.callback_query(F.data == 'return_main_menu')
async def answers_questions_handler(call: CallbackQuery):
    await call.answer()

    await call.message.edit_text(start_text, reply_markup=main_menu_kb)


@router.callback_query(F.data == 'back_main_menu')
async def answers_questions_handler(call: CallbackQuery):
    await call.answer()

    await call.message.answer(start_text, reply_markup=main_menu_kb)


@router.callback_query(F.data == 'answers_questions')
async def answers_questions_handler(call: CallbackQuery):
    await call.answer()

    await call.message.edit_text(answers_questions_text, reply_markup=return_main_menu_kb)


@router.callback_query(F.data == 'special_offer')
async def special_offer_handler(call: CallbackQuery):
    await call.answer()

    await call.message.edit_text(special_offer_text, reply_markup=return_main_menu_kb)


