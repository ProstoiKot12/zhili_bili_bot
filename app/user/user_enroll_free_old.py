from aiogram import F
from aiogram.types import CallbackQuery
from aiogram import Router

from content.text.enroll_free_text import *

from app.keyboards.user_keyboards import (old_one_one_six_kb, one_one_six_two_kb,
                                          two_three_kb, three_four_kb, four_five_page_1_kb, four_five_page_2_kb,
                                          five_six_page_1_kb, five_six_page_2_kb, five_six_page_3_kb,
                                          six_seven_page_1_kb, six_seven_page_2_kb, six_seven_page_3_kb,
                                          seven_plus_page_1_kb, seven_plus_page_2_kb, seven_plus_page_3_kb)


router = Router()


@router.callback_query(F.data == 'old_1-1,6')
async def old_one_one_six_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()

    await call.message.answer(old_one_one_six_text, reply_markup=old_one_one_six_kb)


@router.callback_query(F.data == 'old_1,6-2')
async def old_one_six_two_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()

    await call.message.answer(old_one_six_two_text, reply_markup=one_one_six_two_kb)


@router.callback_query(F.data == 'old_2-3')
async def old_two_three_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()

    await call.message.answer(old_two_three_text, reply_markup=two_three_kb)


@router.callback_query(F.data == 'old_3-4')
async def old_three_four_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()

    await call.message.answer(old_three_four_text, reply_markup=three_four_kb)


@router.callback_query(F.data == 'old_4-5_page_1')
async def old_four_five_page_1_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()

    await call.message.answer(old_four_five_text, reply_markup=four_five_page_1_kb)


@router.callback_query(F.data == 'old_4-5_page_2')
async def old_four_five_page_1_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()

    await call.message.answer(old_four_five_text, reply_markup=four_five_page_2_kb)


@router.callback_query(F.data == 'old_5-6_page_1')
async def old_five_six_page_1_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()

    await call.message.answer(old_five_six_text, reply_markup=five_six_page_1_kb)


@router.callback_query(F.data == 'old_5-6_page_2')
async def old_five_six_page_2_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()

    await call.message.answer(old_five_six_text, reply_markup=five_six_page_2_kb)


@router.callback_query(F.data == 'old_5-6_page_3')
async def old_five_six_page_3_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()

    await call.message.answer(old_five_six_text, reply_markup=five_six_page_3_kb)


@router.callback_query(F.data == 'old_6-7_page_1')
async def old_six_seven_page_1_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()

    await call.message.answer(old_six_seven_text, reply_markup=six_seven_page_1_kb)


@router.callback_query(F.data == 'old_6-7_page_2')
async def old_six_seven_page_2_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()

    await call.message.answer(old_six_seven_text, reply_markup=six_seven_page_2_kb)


@router.callback_query(F.data == 'old_6-7_page_3')
async def old_six_seven_page_3_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()

    await call.message.answer(old_six_seven_text, reply_markup=six_seven_page_3_kb)


@router.callback_query(F.data == 'old_7+_page_1')
async def old_seven_plus_page_1_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()

    await call.message.answer(old_seven_plus_text, reply_markup=seven_plus_page_1_kb)


@router.callback_query(F.data == 'old_7+_page_2')
async def old_seven_plus_page_2_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()

    await call.message.answer(old_seven_plus_text, reply_markup=seven_plus_page_2_kb)


@router.callback_query(F.data == 'old_7+_page_3')
async def old_seven_plus_page_3_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()

    await call.message.answer(old_seven_plus_text, reply_markup=seven_plus_page_3_kb)
