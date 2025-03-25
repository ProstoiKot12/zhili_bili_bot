import re

from aiogram import F
from aiogram.types import CallbackQuery
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from datetime import datetime
from aiogram.types import ReplyKeyboardRemove

from app.state.user_state import Enroll
from app.user.user_dict import services_dict
from content.text.enroll_free_text import *
from app.keyboards.user_keyboards import success_enroll_free_kb, back_main_menu_kb, specify_phone_kb
from app.request.crm_request import create_customer

router = Router()


@router.callback_query(F.data.startswith('enroll_free'))
async def user_enroll_free_handler(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.delete()
    await state.update_data(user_service=call.data.split()[1])

    await call.message.answer(what_parent_name_text)

    await state.set_state(Enroll.parent_name)


@router.message(Enroll.parent_name)
async def parent_name_handler(message: Message, state: FSMContext):
    name_pattern = re.compile(r'^[A-Za-zА-Яа-яЁё]+\s[A-Za-zА-Яа-яЁё]+\s[A-Za-zА-Яа-яЁё]+$')

    if name_pattern.match(message.text):
        await state.update_data(parent_name=message.text)

        await message.answer(what_child_name_text)

        await state.set_state(Enroll.child_name)
    else:
        await message.answer(what_parent_name_text)


@router.message(Enroll.child_name)
async def child_name_handler(message: Message, state: FSMContext):
    name_pattern = re.compile(r'^[A-Za-zА-Яа-яЁё]+\s[A-Za-zА-Яа-яЁё]+\s[A-Za-zА-Яа-яЁё]+$')

    if name_pattern.match(message.text):
        await state.update_data(child_name=message.text)

        await message.answer(how_old_child_text)

        await state.set_state(Enroll.child_age_old)
    else:
        await message.answer(what_child_name_text)


@router.message(Enroll.child_age_old)
async def child_age_old_handler(message: Message, state: FSMContext):
    date_pattern = re.compile(r"^\d{2}\.\d{2}\.\d{4}$")

    if date_pattern.match(message.text):
        try:
            input_date = datetime.strptime(message.text, "%d.%m.%Y")
            current_date = datetime.now()

            if input_date > current_date:
                await message.answer(future_date)
                return

            await state.update_data(child_age_old=message.text)
            await message.answer(what_parent_phone_text, reply_markup=specify_phone_kb)
            await state.set_state(Enroll.parent_phone)
        except ValueError:
            await message.answer(how_old_child_text)
    else:
        await message.answer(how_old_child_text)


@router.message(Enroll.parent_phone)
async def parent_phone_handler(message: Message, state: FSMContext):
    phone_pattern = re.compile(r"^\+7\d{10}$")

    if message.contact:
        await state.update_data(parent_phone=message.contact.phone_number)

    elif message.text:
        if phone_pattern.match(message.text):
            await state.update_data(parent_phone=message.text)
        else:
            await message.answer(what_parent_phone_text)
            return

    data = await state.get_data()
    service_and_old = data.get('user_service', 'Не указано')
    service = service_and_old.split('/')[0]
    age_old = service_and_old.split('/')[1].split('_')[1]

    service_name = services_dict.get(service, 'Не совпало')

    await state.update_data(service=service_name)
    await state.update_data(age_old=age_old)

    text = (f'<b>{check_data_text}</b>\n\n'
                f'ФИО Родителя: <b>{data.get("parent_name", 'Не указано')}</b>\n'
                f'ФИО Ребенка: <b>{data.get("child_name", 'Не указано')}</b>\n'
                f'Возраст ребенка: <b>{data.get("child_age_old", 'Не указано')}</b>\n'
                f'Номер телефона Родителя: <b>{data.get("parent_phone", 'Не указано')}</b>\n\n'
                f'Занятие: <b>{service_name} {age_old} лет</b>\n\n')

    await message.answer(text, reply_markup=success_enroll_free_kb)


@router.callback_query(F.data == 'success_enroll_free')
async def success_enroll_free_handler(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    data = await state.get_data()

    html_text = call.message.html_text

    text = (f"<b>Ваши данные</b>\n\n"
            f"{html_text.split('\n\n')[1]}\n\n"
            f"Занятие: <b>{data.get('service', 'Не указано')} {data.get('age_old', 'Не указано')}</b>")

    note = f"{data.get('parent_name', 'Не указано')} {data.get('service', 'Не указано')} {data.get('age_old', 'Не указано')}"

    customer_data = {
        'name': f'{data.get('child_name', 'Не указано')}',
        'branch_ids': 1,
        'is_study': 0,
        'legal_type': 1,
        "phone": f"{data.get('parent_phone', 'Не указано')}",
        "dob": f"{data.get('child_age_old', 'Не указано')}",
        "note": f"{note}",
        "comment": "Новый клиент"
    }

    await create_customer(customer_data)
    await state.clear()

    await call.message.answer(text, reply_markup=ReplyKeyboardRemove())
    await call.message.answer(success_enroll_free_text, reply_markup=back_main_menu_kb)
