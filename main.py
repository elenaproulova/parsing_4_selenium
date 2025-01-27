from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Инициализация веб-драйвера
browser = webdriver.Chrome()


def search_wikipedia(query):
    browser.get(f"https://ru.wikipedia.org/wiki/{query}")
    time.sleep(2)

def read_paragraphs():
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
    print("\n")


def get_related_links():
    links = browser.find_elements(By.XPATH, "//a[@href and not(contains(@href, ':')) and not(contains(@href, '#'))]")
    related_links = []
    for link in links:
        if link.text and link.text not in related_links:
            related_links.append(link)
    return related_links


def main():
    print("Добро пожаловать в поисковик Википедии!")

    # Переход на главную страницу
    browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")
    time.sleep(2)

    initial_query = input("Введите запрос для поиска: ").replace(" ", "_")
    search_wikipedia(initial_query)

    while True:
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")

        choice = input("Ваш выбор (1/2/3): ")

        if choice == '1':
            read_paragraphs()
        elif choice == '2':
            get_related_links()
            # if not link:
            #     print("Связанные страницы не найдены.")
            #     continue

            print("Выберите связанную страницу:")
            # get_related_links()
            print (related_links)
            for i, link in enumerate(related_links[:5]):  # Выводим первые 5 связанных ссылок
                print(f"{i + 1}. {link.text}")

            link_choice = int(input("Введите номер страницы для перехода: ")) - 1

            if 0 <= link_choice < len(related_links):
                related_link = related_links[link_choice]
                related_link.click()
                time.sleep(2)
                while True:
                    print("\nВыберите действие:")
                    print("1. Листать параграфы статьи")
                    print("2. Перейти на одну из внутренних статей")
                    print("3. Выйти из программы")

                    inner_choice = input("Ваш выбор (1/2/3): ")

                    if inner_choice == '1':
                        read_paragraphs()
                    elif inner_choice == '2':
                        related_links = get_related_links()
                        if not related_links:
                            print("Внутренние статьи не найдены.")
                            continue

                        print("Выберите внутреннюю статью:")
                        for i, link in enumerate(related_links[:5]):
                            print(f"{i + 1}. {link.text}")

                        inner_link_choice = int(input("Введите номер статьи для перехода: ")) - 1

                        if 0 <= inner_link_choice < len(related_links):
                            related_link = related_links[inner_link_choice]
                            related_link.click()
                            time.sleep(2)
                        else:
                            print("Неверный выбор.")
                    elif inner_choice == '3':
                        break
                    else:
                        print("Неверный выбор. Пожалуйста, выберите еще раз.")
            else:
                    print("Неверный выбор.")

        elif choice == '3':
                print("Выход из программы.")
                break
        else:
                print("Неверный выбор. Пожалуйста, выберите еще раз.")

    browser.quit()

if __name__ == "__main__":
    main()