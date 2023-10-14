document.addEventListener("DOMContentLoaded", function () {
            const priceElement = document.getElementById("price1");
            const priceLinkElement = document.getElementById("price-link1");
            const initialPrice = 1500; // Изначальная цена
            const delta = 500; // Дельта между тарифами
            const baseUrl = '/tariff/checkout/?tariff=Тариф Для небольшой команды (на 1 мес.)&tariff_id=1&payment_amount='

            // Функция для обновления цены и ссылки на основе выбранного тарифа
            function updatePrice() {
                const selectedTariff = document.querySelector('input[name="tariff1"]:checked').value;
                const newPrice = initialPrice + (selectedTariff - 1) * delta;
                priceElement.textContent = `${newPrice} ₽`;
                priceLinkElement.href = `${baseUrl}${newPrice}`;
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
            const initialPrice = 20; // Изначальная цена
            const delta = 10; // Дельта между тарифами

            // Функция для обновления цены и ссылки на основе выбранного тарифа
            function updatePrice() {
                const selectedTariff = document.querySelector('input[name="tariff2"]:checked').value;
                const newPrice = initialPrice + (selectedTariff - 1) * delta;
                priceElement.textContent = `${newPrice} ₽`;
                priceLinkElement.href = `https://example.com/tariff?price=${newPrice}`;
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
            const initialPrice = 40; // Изначальная цена
            const delta = 10; // Дельта между тарифами

            // Функция для обновления цены и ссылки на основе выбранного тарифа
            function updatePrice() {
                const selectedTariff = document.querySelector('input[name="tariff3"]:checked').value;
                const newPrice = initialPrice + (selectedTariff - 1) * delta;
                priceElement.textContent = `${newPrice} ₽`;
                priceLinkElement.href = `https://example.com/tariff?price=${newPrice}`;
            }

            // Обработчик события изменения radiobutton
            const radioButtons = document.querySelectorAll('input[name="tariff3"]');
            radioButtons.forEach((radioButton) => {
                radioButton.addEventListener('change', updatePrice);
            });

            // Установка начальной цены и ссылки при загрузке страницы
            updatePrice();
        });

