def song_input():
    song = input('Введите фразы песни, разделяя пробелами: \n')
    return song


def rhyme_pam(song_text):
    phrases = song_text.split()
    vowels = "ауоыиэяюеёАУОЫИЭЯЮЕЁ"
    cash = set()
    if len(phrases) > 0:
        for phrase in phrases:
            vowels_count = len(list(filter(lambda char: char in vowels, phrase)))
            cash.add(vowels_count)
        if len(cash) < 2:
            print('Парам пам-пам')
        else:
            print('Пам парам')
    else:
        print('Текст песни пуст')

rhyme_pam(song_input())