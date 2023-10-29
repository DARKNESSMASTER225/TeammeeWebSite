const volumes = (level) => {
              switch (level) {
                  case '1':
                      return 100
                  case '2':
                      return 200
                  case '3':
                      return 500
                  case '4':
                      return 1000
                  default:
                      return
              }
            }

document.addEventListener("DOMContentLoaded", function () {
            const priceElement = document.getElementById("price1");
            const priceLinkElement = document.getElementById("price-link1");
            const initialPrice = 1500; // Изначальная цена
            const delta = 500; // Дельта между тарифами
            const baseUrl = '/tariff/checkout/?tariff=Тариф Для небольшой команды (на 1 мес.)&tariff_exp=1&tariff_id=1&payment_amount='

            // Функция для обновления цены и ссылки на основе выбранного тарифа
            function updatePrice() {
                const selectedTariff = document.querySelector('input[name="tariff1"]:checked').value;
                const newPrice = initialPrice + (selectedTariff - 1) * delta;
                priceElement.textContent = `${newPrice} ₽`;
                priceLinkElement.href = `${baseUrl}${newPrice}&volume=${volumes(selectedTariff)}`;
            }

            // Обработчик события изменения radiobutton
            const radioButtons = document.querySelectorAll('input[name="tariff1"]');
            radioButtons.forEach((radioButton) => {
                radioButton.addEventListener('change', updatePrice);
            });

            // Установка начальной цены и ссылки при загрузке страницы
            updatePrice();
        });

document.addEventListener("DOMContentLoaded", function () {
            const priceElement = document.getElementById("price2");
            const priceLinkElement = document.getElementById("price-link2");
            const initialPrice = 2000; // Изначальная цена
            const delta = 1000; // Дельта между тарифами
            const baseUrl = '/tariff/checkout/?tariff=Тариф Для компактной команды (на 1 мес.)&tariff_exp=1&tariff_id=2&payment_amount='

            // Функция для обновления цены и ссылки на основе выбранного тарифа
            function updatePrice() {
                const selectedTariff = document.querySelector('input[name="tariff2"]:checked').value;
                const newPrice = initialPrice + (selectedTariff - 1) * delta;
                priceElement.textContent = `${newPrice} ₽`;
                priceLinkElement.href = `${baseUrl}${newPrice}&volume=${volumes(selectedTariff)}`;
            }

            // Обработчик события изменения radiobutton
            const radioButtons = document.querySelectorAll('input[name="tariff2"]');
            radioButtons.forEach((radioButton) => {
                radioButton.addEventListener('change', updatePrice);
            });

            // Установка начальной цены и ссылки при загрузке страницы
            updatePrice();
        });

document.addEventListener("DOMContentLoaded", function () {
            const priceElement = document.getElementById("price3");
            const priceLinkElement = document.getElementById("price-link3");
            const initialPrice = 4000; // Изначальная цена
            const delta = 1000; // Дельта между тарифами
            const baseUrl = '/tariff/checkout/?tariff=Тариф Для большой команды. (на 1 мес.)&tariff_exp=1&tariff_id=3&payment_amount='

            // Функция для обновления цены и ссылки на основе выбранного тарифа
            function updatePrice() {
                const selectedTariff = document.querySelector('input[name="tariff3"]:checked').value;
                const newPrice = initialPrice + (selectedTariff - 1) * delta;
                priceElement.textContent = `${newPrice} ₽`;
                priceLinkElement.href = `${baseUrl}${newPrice}&volume=${volumes(selectedTariff)}`;
            }

            // Обработчик события изменения radiobutton
            const radioButtons = document.querySelectorAll('input[name="tariff3"]');
            radioButtons.forEach((radioButton) => {
                radioButton.addEventListener('change', updatePrice);
            });

            // Установка начальной цены и ссылки при загрузке страницы
            updatePrice();
        });

document.addEventListener("DOMContentLoaded", function () {
            const priceElement = document.getElementById("price4");
            const priceLinkElement = document.getElementById("price-link4");
            const initialPrice = 1500; // Изначальная цена
            const delta = 500; // Дельта между тарифами
            const baseUrl = '/tariff/checkout/?tariff=Тариф Для небольшой команды (на год - 12 мес.)&tariff_exp=12&tariff_id=1&payment_amount='

            // Функция для обновления цены и ссылки на основе выбранного тарифа
            function updatePrice() {
                const selectedTariff = document.querySelector('input[name="tariff4"]:checked').value;
                const newPrice = (initialPrice + (selectedTariff - 1) * delta) * 12 * 0.8;
                priceElement.textContent = `${newPrice} ₽`;
                priceLinkElement.href = `${baseUrl}${newPrice}&volume=${volumes(selectedTariff)}`;
            }

            // Обработчик события изменения radiobutton
            const radioButtons = document.querySelectorAll('input[name="tariff4"]');
            radioButtons.forEach((radioButton) => {
                radioButton.addEventListener('change', updatePrice);
            });

            // Установка начальной цены и ссылки при загрузке страницы
            updatePrice();
        });

document.addEventListener("DOMContentLoaded", function () {
            const priceElement = document.getElementById("price5");
            const priceLinkElement = document.getElementById("price-link5");
            const initialPrice = 2000; // Изначальная цена
            const delta = 1000; // Дельта между тарифами
            const baseUrl = '/tariff/checkout/?tariff=Тариф Для компактной команды (на год - 12 мес.)&tariff_exp=12&tariff_id=2&payment_amount='

            // Функция для обновления цены и ссылки на основе выбранного тарифа
            function updatePrice() {
                const selectedTariff = document.querySelector('input[name="tariff5"]:checked').value;
                const newPrice = (initialPrice + (selectedTariff - 1) * delta) * 12 * 0.8;
                priceElement.textContent = `${newPrice} ₽`;
                priceLinkElement.href = `${baseUrl}${newPrice}&volume=${volumes(selectedTariff)}`;
            }

            // Обработчик события изменения radiobutton
            const radioButtons = document.querySelectorAll('input[name="tariff5"]');
            radioButtons.forEach((radioButton) => {
                radioButton.addEventListener('change', updatePrice);
            });

            // Установка начальной цены и ссылки при загрузке страницы
            updatePrice();
        });

document.addEventListener("DOMContentLoaded", function () {
            const priceElement = document.getElementById("price6");
            const priceLinkElement = document.getElementById("price-link6");
            const initialPrice = 4000; // Изначальная цена
            const delta = 1000; // Дельта между тарифами
            const baseUrl = '/tariff/checkout/?tariff=Тариф Для большой команды (на год - 12 мес.)&tariff_id=3&tariff_exp=12&payment_amount='

            // Функция для обновления цены и ссылки на основе выбранного тарифа
            function updatePrice() {
                const selectedTariff = document.querySelector('input[name="tariff6"]:checked').value;
                const newPrice = (initialPrice + (selectedTariff - 1) * delta) * 12 * 0.8;
                priceElement.textContent = `${newPrice} ₽`;
                priceLinkElement.href = `${baseUrl}${newPrice}&volume=${volumes(selectedTariff)}`;
            }

            // Обработчик события изменения radiobutton
            const radioButtons = document.querySelectorAll('input[name="tariff6"]');
            radioButtons.forEach((radioButton) => {
                radioButton.addEventListener('change', updatePrice);
            });

            // Установка начальной цены и ссылки при загрузке страницы
            updatePrice();
        });