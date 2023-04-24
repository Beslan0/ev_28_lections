from bs4 import BeautifulSoup
import requests
import csv

def get_html(url: str) -> str:
   
    response = requests.get(url)
    return response.text

def get_soup(html: str): # BeautifulSoup
    
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def get_last_page(soup: BeautifulSoup) -> int:
    pages = soup.find('ul', class_='pagination').find_all('li', class_='active')
    last_page = pages[-1].find("a").text
    return int(last_page)

def get_data(soup: BeautifulSoup) -> list:
    container = soup.find('div', class_ ='list-view')
    phones = container.find_all('div', class_='item product_listbox oh')
    result = []
    for phone in phones:
        name = phone.find('div', 'listbox_title').text.strip()
        try:
            img = phone.find('div', class_='listbox_img').find('img').get('src')
            
        except:
            img = 'No image!'
        price = phone.find('div', class_='listbox_price').find("strong").text
        
        
        desc =''.join(phone.find("div", class_="product_text").text.strip())
        data = {
            'name': name, 'desc': desc, 'price': price,
            'img': img
        }
        result.append(data)
    return result

def prepare_csv() -> None:
    '''Функция которая подготавливает csv файл!'''
    with open('phones.csv', 'w') as file:
        fieldnames = ['№', 'Name', 'Description', 'Price', 'Image Url']
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
            '№': '№',
            'Name': 'Name',
            'Description': 'Description',
            'Price': 'Price',
            'Image Url': 'Image Url'
        })
count = 1
def write_to_csv(data: list) -> None:
    '''Записывает все данные в csv файл'''
    with open('phones.csv', 'a') as file:
        fieldnames = ['№', 'Name', 'Description', 'Price', 'Image Url']
        writer = csv.DictWriter(file, fieldnames)
        global count
        for phone in data:
            writer.writerow({
                '№': count,
            'Name': phone['name'],
            'Description': phone ['desc'],
            'Price': phone ['price'],
            'Image Url': phone ['img']
            })

            count += 1





def main():
    i = 1
    prepare_csv()
    while True:
        url = f'https://www.kivano.kg/mobilnye-telefony?page={i}'
        html = get_html(url)
        soup = get_soup(html)
        last_page = get_last_page(soup)
        data = get_data(soup)
        write_to_csv(data)
        print(f'Спарсили {i}/{last_page} страницу')
        if i == 15:
            break
        i += 1

main()


        