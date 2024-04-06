from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

big_button_1 = InlineKeyboardButton(
    text='Оплата',
    callback_data='https://payform.ru/ft3op8M/',
    url='https://payform.ru/ft3op8M/'
)

# Создаем объект инлайн-клавиатуры
keyboard1 = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_1]]
)

big_button_2 = InlineKeyboardButton(
    text='Оплата',
    callback_data='https://payform.ru/qs3os62/',
    url='https://payform.ru/qs3os62/'
)

# Создаем объект инлайн-клавиатуры
keyboard2 = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_2]]
)

big_button_3 = InlineKeyboardButton(
    text='Оплата',
    callback_data='https://payform.ru/rj3OhOS/',
    url='https://payform.ru/rj3OhOS/'
)

# Создаем объект инлайн-клавиатуры
keyboard3 = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_3]]
)

big_button_4 = InlineKeyboardButton(
    text='Оплата',
    callback_data='https://payform.ru/cj3wFRl/',
    url='https://payform.ru/cj3wFRl/'
)

# Создаем объект инлайн-клавиатуры
keyboard4 = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_4]]
)
@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(
        text='<b>Лекция по составлению карты желания и чека изобилия</b>\n\n' +

        'Как правильно составлять карту желаний и чек изобилия, чтобы они реально работали. Полная информация от А до Я. Как создать свою карту по всем правилам энергетического мира, также шаблоны для чека изобилия и список аффирмаций 💫!',
        reply_markup=keyboard1
    )
    await msg.answer(
        text='<b>Чек-лист "Подарки для каждого элемента личности</b>\n\n' +

             'Подбирай подарки, которые раскачают энергию твоих близких людей. Около 200 вариантов крутых и необычных подарков на все случаи жизни 🌟!',
        reply_markup=keyboard2
    )
    await msg.answer(
        text='<b>Рекомендации на апрель по китайскому календарю</b>\n\n' +

             'Описание энергий апрель: как стоит себя вести, чтобы февраль прошел благоприятно. Также советы для каждого элемента личности - что принесет апрель именно вам 🌟!',
        reply_markup=keyboard3
    )
    await msg.answer(
        text='<b>Рекомендации по китайскому календарю на 2024 год</b>\n\n' +

             'Описание основных тенденций 2024 года. Как себя вести, чтобы максимально позитивно использовать силу энергий года. Что делать, если в карте есть собака, дракон, кролик или бык. Советы для каждого элемента личности 💫',
        reply_markup=keyboard4
    )
