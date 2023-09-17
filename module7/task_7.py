card_count = int(input('Введите число карточек: '))
cards_left = input('Введите номера оставшихся карточек через запятую: ')
str_cards_left = [int(el) for el in cards_left.split(",")]
lost_card = 0
for card in range(1, card_count + 1):
    if card not in str_cards_left:
        lost_card = card
print(f'Номер утерянной карты: {lost_card}')
