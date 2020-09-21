
def words_text(funk):
    print(funk().split())

@words_text
def text_funk():
    return input("введите текст:")
