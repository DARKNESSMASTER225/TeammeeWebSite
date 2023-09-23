document.addEventListener("DOMContentLoaded", function () {
    const monthlyRadio = document.querySelector('input[name="subscription"][value="monthly"]');
    const yearlyRadio = document.querySelector('input[name="subscription"][value="yearly"]');
    const monthlyTariffs = document.querySelectorAll('.monthly-tariff');
    const yearlyTariffs = document.querySelectorAll('.yearly-tariff');

    // По умолчанию показываем месячные тарифы
    monthlyRadio.checked = true;
    yearlyTariffs.forEach(tariff => tariff.style.display = 'none');

    // Обработчик события изменения радиокнопки
    yearlyRadio.addEventListener('change', function () {
        if (yearlyRadio.checked) {
            monthlyTariffs.forEach(tariff => tariff.style.display = 'none');
            yearlyTariffs.forEach(tariff => tariff.style.display = 'block');
        }
    });

    monthlyRadio.addEventListener('change', function () {
        if (monthlyRadio.checked) {
            yearlyTariffs.forEach(tariff => tariff.style.display = 'none');
            monthlyTariffs.forEach(tariff => tariff.style.display = 'block');
        }
    });
});
