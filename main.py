from selenium import webdriver
from selenium.webdriver.common.by import By
import time


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
    links = browser.find_elements(By.TAG_NAME, "a")

    related_links = []
    for link in links:
        href = link.get_attribute('href')
        title = link.get_attribute('title')

        if title and href:
            related_links.append((title, href))

    return related_links


def main():
    print("Добро пожаловать в поисковик Википедии!")

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
            related_links = get_related_links()

            if not related_links:
                print("Связанные страницы не найдены.")
                continue

            print("Выберите связанную страницу:")
            for i, (title, href) in enumerate(related_links[:15]):
                print(f"{i + 1}. {title}")

            link_choice = int(input("Введите номер страницы для перехода: ")) - 1

            if 0 <= link_choice < len(related_links):
                _, href = related_links[link_choice]
                browser.get(href)
                time.sleep(2)
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