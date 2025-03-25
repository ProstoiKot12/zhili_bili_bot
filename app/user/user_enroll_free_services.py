from aiogram import F
from aiogram.types import CallbackQuery, FSInputFile
from aiogram import Router

from content.text.enroll_free_text import *

from app.keyboards.user_keyboards import (how_old_kb, create_enroll_free_kb)

router = Router()


async def create_photo_path(photo_name):
    photo_path = FSInputFile(f"content/images/{photo_name}.jpg")
    return photo_path


@router.callback_query(F.data == 'start_enroll_free')
async def start_enroll_free_handler(call: CallbackQuery):
    await call.answer()

    await call.message.edit_text(text=how_old_text, reply_markup=how_old_kb)


@router.callback_query(F.data.startswith('mother_and_son'))
async def mother_and_son_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    return_data = call.data.split('/')[1]
    kb = await create_enroll_free_kb(f'mother_and_son/{return_data}', return_data)

    photo = await create_photo_path(call.data.split('/')[0])
    await call.message.answer_photo(photo=photo, caption=mother_and_son_text, reply_markup=kb)


@router.callback_query(F.data.startswith('family_psychologist'))
async def family_psychologist_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    return_data = call.data.split('/')[1]
    kb = await create_enroll_free_kb(f'family_psychologist/{return_data}', return_data)

    photo = await create_photo_path(call.data.split('/')[0])
    await call.message.answer_photo(photo=photo, caption=family_psychologist_text, reply_markup=kb)


@router.callback_query(F.data.startswith('speech_launch'))
async def speech_launch_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    return_data = call.data.split('/')[1]
    kb = await create_enroll_free_kb(f'speech_launch/{return_data}', return_data)

    photo = await create_photo_path(call.data.split('/')[0])
    await call.message.answer_photo(photo=photo, caption=speech_launch_text, reply_markup=kb)


@router.callback_query(F.data.startswith('baby_fitness'))
async def baby_fitness_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    return_data = call.data.split('/')[1]
    kb = await create_enroll_free_kb(f'baby_fitness/{return_data}', return_data)
    
    photo = await create_photo_path(call.data.split('/')[0])
    await call.message.answer_photo(photo=photo, caption=baby_fitness_text, reply_markup=kb)


@router.callback_query(F.data.startswith('tyap_lyap'))
async def tyap_lyap_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    return_data = call.data.split('/')[1]
    kb = await create_enroll_free_kb(f'tyap_lyap/{return_data}', return_data)
    
    photo = await create_photo_path(call.data.split('/')[0])
    await call.message.answer_photo(photo=photo, caption=tyap_lyap_text, reply_markup=kb)


@router.callback_query(F.data.startswith('sand_table'))
async def sand_table_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    return_data = call.data.split('/')[1]
    kb = await create_enroll_free_kb(f'sand_table/{return_data}', return_data)
    
    photo = await create_photo_path(call.data.split('/')[0])
    await call.message.answer_photo(photo=photo, caption=sand_table_text, reply_markup=kb)


@router.callback_query(F.data.startswith('child_dance'))
async def child_dance_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    return_data = call.data.split('/')[1]
    kb = await create_enroll_free_kb(f'child_dance/{return_data}', return_data)
    
    photo = await create_photo_path(call.data.split('/')[0])
    await call.message.answer_photo(photo=photo, caption=child_dance_text, reply_markup=kb)


@router.callback_query(F.data.startswith('school_preparation'))
async def school_preparation_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    return_data = call.data.split('/')[1]
    kb = await create_enroll_free_kb(f'school_preparation/{return_data}', return_data)

    photo = await create_photo_path(call.data.split('/')[0])
    await call.message.answer_photo(photo=photo, caption=school_preparation_text, reply_markup=kb)


@router.callback_query(F.data.startswith('health_spine'))
async def health_spine_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    return_data = call.data.split('/')[1]
    kb = await create_enroll_free_kb(f'health_spine/{return_data}', return_data)

    photo = await create_photo_path(call.data.split('/')[0])
    await call.message.answer_photo(photo=photo, caption=health_spine_text, reply_markup=kb)


@router.callback_query(F.data.startswith('speech_pathologist'))
async def health_spine__handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    return_data = call.data.split('/')[1]
    kb = await create_enroll_free_kb(f'speech_pathologist/{return_data}', return_data)

    photo = await create_photo_path(call.data.split('/')[0])
    await call.message.answer_photo(photo=photo, caption=speech_pathologist_text, reply_markup=kb)


@router.callback_query(F.data.startswith('school_art'))
async def school_art_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    return_data = call.data.split('/')[1]
    kb = await create_enroll_free_kb(f'school_art/{return_data}', return_data)

    photo = await create_photo_path(call.data.split('/')[0])
    await call.message.answer_photo(photo=photo, caption=school_art_text, reply_markup=kb)


@router.callback_query(F.data.startswith('iso_modeling'))
async def iso_modeling_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    return_data = call.data.split('/')[1]
    kb = await create_enroll_free_kb(f'iso_modeling/{return_data}', return_data)

    photo = await create_photo_path(call.data.split('/')[0])
    await call.message.answer_photo(photo=photo, caption=iso_modeling_text, reply_markup=kb)


@router.callback_query(F.data.startswith('dool_training'))
async def dool_training_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    return_data = call.data.split('/')[1]
    kb = await create_enroll_free_kb(f'dool_training/{return_data}', return_data)

    photo = await create_photo_path(call.data.split('/')[0])
    await call.message.answer_photo(photo=photo, caption=dool_training_text, reply_markup=kb)


@router.callback_query(F.data.startswith('new_year'))
async def new_year_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    return_data = call.data.split('/')[1]
    kb = await create_enroll_free_kb(f'new_year/{return_data}', return_data)

    photo = await create_photo_path(call.data.split('/')[0])
    await call.message.answer_photo(photo=photo, caption=new_year_text, reply_markup=kb)


@router.callback_query(F.data.startswith('baby_and_glade'))
async def baby_and_glade_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    return_data = call.data.split('/')[1]
    kb = await create_enroll_free_kb(f'baby_and_glade/{return_data}', return_data)

    photo = await create_photo_path(call.data.split('/')[0])
    await call.message.answer_photo(photo=photo, caption=baby_and_glade_text, reply_markup=kb)


@router.callback_query(F.data.startswith('modern_dance'))
async def modern_dance_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    return_data = call.data.split('/')[1]
    kb = await create_enroll_free_kb(f'modern_dance/{return_data}', return_data)

    photo = await create_photo_path(call.data.split('/')[0])
    await call.message.answer_photo(photo=photo, caption=modern_dance_text, reply_markup=kb)


@router.callback_query(F.data.startswith('reading'))
async def reading_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    return_data = call.data.split('/')[1]
    kb = await create_enroll_free_kb(f'reading/{return_data}', return_data)

    photo = await create_photo_path(call.data.split('/')[0])
    await call.message.answer_photo(photo=photo, caption=reading_text, reply_markup=kb)


@router.callback_query(F.data.startswith('math_academy'))
async def math_academy_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    return_data = call.data.split('/')[1]
    kb = await create_enroll_free_kb(f'math_academy/{return_data}', return_data)

    photo = await create_photo_path(call.data.split('/')[0])
    await call.message.answer_photo(photo=photo, caption=math_academy_text, reply_markup=kb)


@router.callback_query(F.data.startswith('english'))
async def english_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    return_data = call.data.split('/')[1]
    kb = await create_enroll_free_kb(f'english/{return_data}', return_data)

    photo = await create_photo_path(call.data.split('/')[0])
    await call.message.answer_photo(photo=photo, caption=english_text, reply_markup=kb)


@router.callback_query(F.data.startswith('acrobatics'))
async def acrobatics_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    return_data = call.data.split('/')[1]
    kb = await create_enroll_free_kb(f'acrobatics/{return_data}', return_data)

    photo = await create_photo_path(call.data.split('/')[0])
    await call.message.answer_photo(photo=photo, caption=acrobatics_text, reply_markup=kb)


@router.callback_query(F.data.startswith('summer_club'))
async def summer_club_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    return_data = call.data.split('/')[1]
    kb = await create_enroll_free_kb(f'summer_club/{return_data}', return_data)

    photo = await create_photo_path(call.data.split('/')[0])
    await call.message.answer_photo(photo=photo, caption=summer_club_text, reply_markup=kb)


@router.callback_query(F.data.startswith('future_first_schoolboy'))
async def future_first_schoolboy_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    return_data = call.data.split('/')[1]
    kb = await create_enroll_free_kb(f'future_first_schoolboy/{return_data}', return_data)

    photo = await create_photo_path(call.data.split('/')[0])
    await call.message.answer_photo(photo=photo, caption=future_first_schoolboy_text, reply_markup=kb)


@router.callback_query(F.data.startswith('ready_for_school'))
async def ready_for_school_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    return_data = call.data.split('/')[1]
    kb = await create_enroll_free_kb(f'ready_for_school/{return_data}', return_data)

    photo = await create_photo_path(call.data.split('/')[0])
    await call.message.answer_photo(photo=photo, caption=ready_for_school_text, reply_markup=kb)


@router.callback_query(F.data.startswith('theatre_studio'))
async def theatre_studio_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    return_data = call.data.split('/')[1]
    kb = await create_enroll_free_kb(f'theatre_studio/{return_data}', return_data)

    photo = await create_photo_path(call.data.split('/')[0])
    await call.message.answer_photo(photo=photo, caption=theatre_studio_text, reply_markup=kb)


@router.callback_query(F.data.startswith('after_school_program'))
async def after_school_program_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    return_data = call.data.split('/')[1]
    kb = await create_enroll_free_kb(f'after_school_program/{return_data}', return_data)

    photo = await create_photo_path(call.data.split('/')[0])
    await call.message.answer_photo(photo=photo, caption=after_school_program_text, reply_markup=kb)


@router.callback_query(F.data.startswith('table_multiplication'))
async def table_multiplication_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    return_data = call.data.split('/')[1]
    kb = await create_enroll_free_kb(f'table_multiplication/{return_data}', return_data)

    photo = await create_photo_path(call.data.split('/')[0])
    await call.message.answer_photo(photo=photo, caption=table_multiplication_text, reply_markup=kb)


@router.callback_query(F.data.startswith('literacy'))
async def literacy_handler(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    return_data = call.data.split('/')[1]
    kb = await create_enroll_free_kb(f'literacy/{return_data}', return_data)

    photo = await create_photo_path(call.data.split('/')[0])
    await call.message.answer_photo(photo=photo, caption=literacy_text, reply_markup=kb)
