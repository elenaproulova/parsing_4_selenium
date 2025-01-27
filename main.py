from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Инициализация веб-драйвера
browser = webdriver.Chrome()


def search_wikipedia(query):
    browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")
    time.sleep(2)
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(1)

def read_paragraphs():
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
    print("\n")


def get_related_links():
    hatnotes = []
    for element in browser.find_elements(By.TAG_NAME, "div"):
    # Чтобы искать атрибут класса
        cl = element.get_attribute("class")
        if cl == "hatnote navigation-not-searchable":
            hatnotes.append(element)
        return hatnotes

   # hatnote = random.choice(hatnotes)

    # Для получения ссылки мы должны найти на сайте тег "a" внутри тега "div"
    # link = hatnote.find_element(By.TAG_NAME, "a").get.attribute("href")
    # browser.get(link)







    # links = browser.find_elements(By.XPATH, "//a[@href and not(contains(@href, ':')) and not(contains(@href, '#'))]")
    # related_links = []
    # for link in links:
    #     if link.text and link.text not in related_links:
    #         related_links.append(link)
    # return related_links


def main():
    print("Добро пожаловать в поисковик Википедии!")

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
            link = get_related_links()
            if not link:
                print("Связанные страницы не найдены.")
                continue

            print("Выберите связанную страницу:")
            for i, link in enumerate(hatnotes[:5]):  # Выводим первые 5 связанных ссылок
                print(f"{i + 1}. {link.text}")

            link_choice = int(input("Введите номер страницы для перехода: ")) - 1

            if 0 <= link_choice < len(related_links):
                related_link = related_links[link_choice]
                related_link.click()
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