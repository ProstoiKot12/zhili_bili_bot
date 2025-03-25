from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


main_menu_but = [
    [
        InlineKeyboardButton(text='📝Записаться на пробное занятие', callback_data='start_enroll_free')
    ],
    [
        InlineKeyboardButton(text='❓ЧаВо', callback_data='answers_questions')
    ],
    [
        InlineKeyboardButton(text='❗Акции', callback_data='special_offer')
    ]
]

main_menu_kb = InlineKeyboardMarkup(inline_keyboard=main_menu_but)

return_main_menu_but = [
    [
        InlineKeyboardButton(text='◀️Назад', callback_data='return_main_menu')
    ]
]

return_main_menu_kb = InlineKeyboardMarkup(inline_keyboard=return_main_menu_but)

how_old_but = [
    [
        InlineKeyboardButton(text='1-1,6', callback_data='old_1-1,6'),
        InlineKeyboardButton(text='1,6-2', callback_data='old_1,6-2'),
    ],
    [
        InlineKeyboardButton(text='2-3', callback_data='old_2-3'),
        InlineKeyboardButton(text='3-4', callback_data='old_3-4'),
    ],
    [
        InlineKeyboardButton(text='4-5', callback_data='old_4-5_page_1'),
        InlineKeyboardButton(text='5-6', callback_data='old_5-6_page_1'),
    ],
    [
        InlineKeyboardButton(text='6-7', callback_data='old_6-7_page_1'),
        InlineKeyboardButton(text='7+', callback_data='old_7+_page_1'),
    ],
    [InlineKeyboardButton(text='◀️Назад', callback_data='return_main_menu')]
]

how_old_kb = InlineKeyboardMarkup(inline_keyboard=how_old_but)


old_one_one_six_but = [
    [
        InlineKeyboardButton(text='Мама и малыш', callback_data='mother_and_son/old_1-1,6')
    ],
    [
        InlineKeyboardButton(text='Семейный психолог', callback_data='family_psychologist/old_1-1,6')
    ],
    [InlineKeyboardButton(text='◀️Назад', callback_data='start_enroll_free')]
]

old_one_one_six_kb = InlineKeyboardMarkup(inline_keyboard=old_one_one_six_but)


one_one_six_two_but = [
    [
        InlineKeyboardButton(text='Мама и малыш', callback_data='mother_and_son/old_1,6-2')
    ],
    [
        InlineKeyboardButton(text='Семейный психолог', callback_data='family_psychologist/old_1,6-2')
    ],
    [
        InlineKeyboardButton(text='Говорилка', callback_data='speech_launch/old_1,6-2')
    ],
    [
        InlineKeyboardButton(text='Baby fitnes', callback_data='baby_fitness/old_1,6-2')
    ],
    [InlineKeyboardButton(text='◀️Назад', callback_data='start_enroll_free')]
]

one_one_six_two_kb = InlineKeyboardMarkup(inline_keyboard=one_one_six_two_but)


two_three_but = [
    [
        InlineKeyboardButton(text='Мама и малыш', callback_data='mother_and_son/old_2-3')
    ],
    [
        InlineKeyboardButton(text='Семейный психолог', callback_data='family_psychologist/old_2-3')
    ],
    [
        InlineKeyboardButton(text='Baby fitnes', callback_data='baby_fitness/old_2-3')
    ],
    [
        InlineKeyboardButton(text='Тяп-Ляп', callback_data='tyap_lyap/old_2-3')
    ],
    [InlineKeyboardButton(text='◀️Назад', callback_data='start_enroll_free')]
]

two_three_kb= InlineKeyboardMarkup(inline_keyboard=two_three_but)


three_four_but = [
    [
        InlineKeyboardButton(text='Мама и малыш', callback_data='mother_and_son/old_3-4')
    ],
    [
        InlineKeyboardButton(text='Детская хореография', callback_data='child_dance/old_3-4')
    ],
    [
        InlineKeyboardButton(text='Песочный стол', callback_data='sand_table/old_3-4')
    ],
    [
        InlineKeyboardButton(text='Тяп-Ляп', callback_data='tyap_lyap/old_3-4')
    ],
    [
        InlineKeyboardButton(text='Семейный психолог', callback_data='family_psychologist/old_3-4')
    ],
    [InlineKeyboardButton(text='◀️Назад', callback_data='start_enroll_free')]
]

three_four_kb = InlineKeyboardMarkup(inline_keyboard=three_four_but)


four_five_page_1_but = [
    [
        InlineKeyboardButton(text='Подготовка к школе', callback_data='school_preparation/old_4-5_page_1')
    ],
    [
        InlineKeyboardButton(text='Здоровье спины и стопы', callback_data='health_spine/old_4-5_page_1')
    ],
    [
        InlineKeyboardButton(text='Логопед', callback_data='speech_pathologist/old_4-5_page_1')
    ],
    [
        InlineKeyboardButton(text='Детская хореография', callback_data='child_dance/old_4-5_page_1')
    ],
    [
        InlineKeyboardButton(text='Школа живописи', callback_data='school_art/old_4-5_page_1')
    ],
    [
        InlineKeyboardButton(text='◀️Назад', callback_data='start_enroll_free'),
        InlineKeyboardButton(text='Вперед▶️', callback_data='old_4-5_page_2'),
    ]
]

four_five_page_1_kb = InlineKeyboardMarkup(inline_keyboard=four_five_page_1_but)


four_five_page_2_but = [
    [
        InlineKeyboardButton(text='Изолепка', callback_data='iso_modeling/old_4-5_page_2')
    ],
    [
        InlineKeyboardButton(text='Песочный стол', callback_data='sand_table/old_4-5_page_2')
    ],
    [
        InlineKeyboardButton(text='Кукловедение', callback_data='dool_training/old_4-5_page_2')
    ],
    [
        InlineKeyboardButton(text='Новый год', callback_data='new_year/old_4-5_page_2')
    ],
    [
        InlineKeyboardButton(text='Семейный психолог', callback_data='family_psychologist/old_4-5_page_2')
    ],
    [
        InlineKeyboardButton(text='Малышники и полянки', callback_data='baby_and_glade/old_4-5_page_2')
    ],
    [
        InlineKeyboardButton(text='◀️Назад', callback_data='old_4-5_page_1')
    ]
]

four_five_page_2_kb = InlineKeyboardMarkup(inline_keyboard=four_five_page_2_but)


five_six_page_1_but = [
    [
        InlineKeyboardButton(text='Подготовка к школе', callback_data='school_preparation/old_5-6_page_1')
    ],
    [
        InlineKeyboardButton(text='Здоровье спины и стопы', callback_data='health_spine/old_5-6_page_1')
    ],
    [
        InlineKeyboardButton(text='Логопед', callback_data='speech_pathologist/old_5-6_page_1')
    ],
    [
        InlineKeyboardButton(text='Современные танцы', callback_data='modern_dance/old_5-6_page_1')
    ],
    [
        InlineKeyboardButton(text='Чтение', callback_data='reading/old_5-6_page_1')
    ],
    [
        InlineKeyboardButton(text='◀️Назад', callback_data='start_enroll_free'),
        InlineKeyboardButton(text='Вперед▶️', callback_data='old_5-6_page_2')
    ]
]

five_six_page_1_kb = InlineKeyboardMarkup(inline_keyboard=five_six_page_1_but)


five_six_page_2_but = [
    [
        InlineKeyboardButton(text='Математическая академия', callback_data='math_academy/old_5-6_page_2')
    ],
    [
        InlineKeyboardButton(text='Английский язык', callback_data='english/old_5-6_page_2')
    ],
    [
        InlineKeyboardButton(text='Школа живописи', callback_data='school_art/old_5-6_page_2')
    ],
    [
        InlineKeyboardButton(text='Акробатика', callback_data='acrobatics/old_5-6_page_2')
    ],
    [
        InlineKeyboardButton(text='Песчаный стол', callback_data='sand_table/old_5-6_page_2')
    ],
    [
        InlineKeyboardButton(text='◀️Назад', callback_data='old_5-6_page_1'),
        InlineKeyboardButton(text='Вперед▶️', callback_data='old_5-6_page_3')
    ]
]

five_six_page_2_kb = InlineKeyboardMarkup(inline_keyboard=five_six_page_2_but)


five_six_page_3_but = [
    [
        InlineKeyboardButton(text='Изолепка', callback_data='iso_modeling/old_5-6_page_3')
    ],
    [
        InlineKeyboardButton(text='Кукловедение', callback_data='dool_training/old_5-6_page_3')
    ],
    [
        InlineKeyboardButton(text='Новый год', callback_data='new_year/old_5-6_page_3')
    ],
    [
        InlineKeyboardButton(text='Летний клуб', callback_data='summer_club/old_5-6_page_3')
    ],
    [
        InlineKeyboardButton(text='Семейный психолог', callback_data='family_psychologist/old_5-6_page_3')
    ],
    [
        InlineKeyboardButton(text='◀️Назад', callback_data='old_5-6_page_2')
    ]
]

five_six_page_3_kb = InlineKeyboardMarkup(inline_keyboard=five_six_page_3_but)


six_seven_page_1_but = [
    [
        InlineKeyboardButton(text='Будущий первоклассник', callback_data='future_first_schoolboy/old_6-7_page_1')
    ],
    [
        InlineKeyboardButton(text='Готов к школе', callback_data='ready_for_school/old_6-7_page_1')
    ],
    [
        InlineKeyboardButton(text='Чтение', callback_data='reading/old_6-7_page_1')
    ],
    [
        InlineKeyboardButton(text='Математическая академия', callback_data='math_academy/old_6-7_page_1')
    ],
    [
        InlineKeyboardButton(text='Здоровье спины и стопы', callback_data='health_spine/old_6-7_page_1')
    ],
    [
        InlineKeyboardButton(text='◀️Назад', callback_data='start_enroll_free'),
        InlineKeyboardButton(text='Вперед▶️', callback_data='old_6-7_page_2'),
    ]
]

six_seven_page_1_kb = InlineKeyboardMarkup(inline_keyboard=six_seven_page_1_but)


six_seven_page_2_but = [
    [
        InlineKeyboardButton(text='Логопед', callback_data='speech_pathologist/old_6-7_page_2')
    ],
    [
        InlineKeyboardButton(text='Английский язык', callback_data='english/old_6-7_page_2')
    ],
    [
        InlineKeyboardButton(text='Современные танцы', callback_data='modern_dance/old_6-7_page_2')
    ],
    [
        InlineKeyboardButton(text='Акробатика', callback_data='acrobatics/old_6-7_page_2')
    ],
    [
        InlineKeyboardButton(text='Школа живописи', callback_data='school_art/old_6-7_page_2')
    ],
    [
        InlineKeyboardButton(text='◀️Назад', callback_data='old_6-7_page_1'),
        InlineKeyboardButton(text='Вперед▶️', callback_data='old_6-7_page_3'),
    ]
]

six_seven_page_2_kb = InlineKeyboardMarkup(inline_keyboard=six_seven_page_2_but)


six_seven_page_3_but = [
    [
        InlineKeyboardButton(text='Песочный стол', callback_data='sand_table/old_6-7_page_3')
    ],
    [
        InlineKeyboardButton(text='Театральная студия', callback_data='theatre_studio/old_6-7_page_3')
    ],
    [
        InlineKeyboardButton(text='Семейный психолог', callback_data='family_psychologist/old_6-7_page_3')
    ],
    [
        InlineKeyboardButton(text='Новый год', callback_data='new_year/old_6-7_page_3')
    ],
    [
        InlineKeyboardButton(text='Летний клуб', callback_data='summer_club/old_6-7_page_3')
    ],
    [
        InlineKeyboardButton(text='◀️Назад', callback_data='old_6-7_page_2'),
    ]
]

six_seven_page_3_kb = InlineKeyboardMarkup(inline_keyboard=six_seven_page_3_but)


seven_plus_page_1_but = [
    [
        InlineKeyboardButton(text='Продленка', callback_data='after_school_program/old_7+_page_1')
    ],
    [
        InlineKeyboardButton(text='Готов к школе', callback_data='ready_for_school/old_7+_page_1')
    ],
    #[
    #    InlineKeyboardButton(text='Скорочтение', callback_data='speed_reading/old_7+_page_1')
    #],
    [
        InlineKeyboardButton(text='Таблица умножения', callback_data='table_multiplication/old_7+_page_1')
    ],
    [
        InlineKeyboardButton(text='Грамотность', callback_data='literacy/old_7+_page_1')
    ],
    [
        InlineKeyboardButton(text='◀️Назад', callback_data='start_enroll_free'),
        InlineKeyboardButton(text='Вперед▶️', callback_data='old_7+_page_2'),
    ]
]

seven_plus_page_1_kb = InlineKeyboardMarkup(inline_keyboard=seven_plus_page_1_but)


seven_plus_page_2_but = [
    [
        InlineKeyboardButton(text='Математическая академия', callback_data='math_academy/old_7+_page_2')
    ],
    [
        InlineKeyboardButton(text='Здоровье спины и стопы', callback_data='health_spine/old_7+_page_2')
    ],
    [
        InlineKeyboardButton(text='Логопед', callback_data='speech_pathologist/old_7+_page_2')
    ],
    [
        InlineKeyboardButton(text='Английский язык', callback_data='english/old_7+_page_2')
    ],
    [
        InlineKeyboardButton(text='Современные танцы', callback_data='modern_dance/old_7+_page_2')
    ],
    [
        InlineKeyboardButton(text='◀️Назад', callback_data='old_7+_page_1'),
        InlineKeyboardButton(text='Вперед▶️', callback_data='old_7+_page_3'),
    ]
]

seven_plus_page_2_kb = InlineKeyboardMarkup(inline_keyboard=seven_plus_page_2_but)


seven_plus_page_3_but = [
    [
        InlineKeyboardButton(text='Акробатика', callback_data='acrobatics/old_7+_page_3')
    ],
    [
        InlineKeyboardButton(text='Школа живописи', callback_data='school_art/old_7+_page_3')
    ],
    [
        InlineKeyboardButton(text='Театральная студия', callback_data='theatre_studio/old_7+_page_3')
    ],
    [
        InlineKeyboardButton(text='Семейный психолог', callback_data='family_psychologist/old_7+_page_3')
    ],
    [
        InlineKeyboardButton(text='Новый год', callback_data='new_year/old_7+_page_3')
    ],
    [
        InlineKeyboardButton(text='Летный клуб', callback_data='summer_club/old_7+_page_3')
    ],
    [
        InlineKeyboardButton(text='◀️Назад', callback_data='old_7+_page_2')
    ]
]

seven_plus_page_3_kb = InlineKeyboardMarkup(inline_keyboard=seven_plus_page_3_but)


success_enroll_free_but = [
    [
        InlineKeyboardButton(text='✅Все верно - записаться', callback_data='success_enroll_free')
    ],
    [InlineKeyboardButton(text='🏠Главное меню', callback_data='return_main_menu')]
]

success_enroll_free_kb = InlineKeyboardMarkup(inline_keyboard=success_enroll_free_but)


back_main_menu_but = [
    [InlineKeyboardButton(text='🏠Главное меню', callback_data='back_main_menu')]
]

back_main_menu_kb = InlineKeyboardMarkup(inline_keyboard=back_main_menu_but)

specify_phone_but = [
    [
        KeyboardButton(text="☎️Указать номер телефона", request_contact=True)
    ]
]

specify_phone_kb = ReplyKeyboardMarkup(
    keyboard=specify_phone_but,
    resize_keyboard=True,
    input_field_placeholder="Укажите номер телефона"
)


async def create_enroll_free_kb(call_data, return_data):
    enroll_free_but = [
        [
            InlineKeyboardButton(text='📝Записаться на пробное занятие', callback_data=f'enroll_free {call_data}')
        ],
        [InlineKeyboardButton(text='◀️Назад', callback_data=f'{return_data}')]
    ]

    enroll_free_kb = InlineKeyboardMarkup(inline_keyboard=enroll_free_but)
    return enroll_free_kb