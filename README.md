<div style="
    position: relative; 
    width: 100%; 
    height: 330px; 
    border-radius: 16px; 
    overflow: hidden; 
    background-color: #0b1a2e;
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.6);
">
    <!-- Фоновое изображение (городской пейзаж / недвижимость) -->
    <div style="
        position: absolute; 
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: url('https://images.unsplash.com/photo-1568605117036-5fe5e7b4b5e5?q=80&w=2070&auto=format&fit=crop'); 
        background-size: cover; 
        background-position: center;
        filter: brightness(0.35) contrast(1.1);
    "></div>
    <!-- Дополнительная тёмная вуаль -->
    <div style="
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(5, 15, 25, 0.4);
    "></div>
    <!-- Карточка с заголовком -->
    <div style="
        position: absolute; 
        top: 50%; 
        left: 50%; 
        transform: translate(-50%, -50%);
        background: rgba(20, 30, 45, 0.5); 
        backdrop-filter: blur(12px); 
        -webkit-backdrop-filter: blur(12px); 
        border: 1px solid rgba(255, 255, 255, 0.15);
        padding: 40px 60px; 
        border-radius: 28px; 
        text-align: center;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5), 
                    inset 0 1px 1px rgba(255, 255, 255, 0.1);
        width: 75%;
        max-width: 750px;
    ">
        <h1 style="
            margin: 0; 
            font-family: 'Inter', 'Segoe UI', system-ui, sans-serif; 
            font-weight: 800; 
            font-size: 3.4em; 
            letter-spacing: -1.5px;
            line-height: 1.1;
            color: #ffffff;
            text-shadow: 0 4px 20px rgba(0,0,0,0.5);
        ">
            🏡 <span style="color: #ffb347; text-shadow: 0 0 12px rgba(255, 180, 70, 0.6);">House Price</span> Prediction
        </h1>
        <div style="
            width: 70px; 
            height: 4px; 
            background: linear-gradient(90deg, #ffb347, #ff7f50); 
            margin: 18px auto;
            border-radius: 4px;
            box-shadow: 0 0 12px rgba(255, 140, 0, 0.6);
        "></div>
        <p style="
            margin: 0; 
            font-family: 'Courier New', monospace; 
            font-size: 1.05em; 
            font-weight: 600; 
            letter-spacing: 3.5px; 
            color: rgba(255, 255, 255, 0.95);
            text-transform: uppercase;
        ">
            EDA <span style="color: #ffb347;">✦</span> Cleaning <span style="color: #ffb347;">✦</span> Feature Engineering 
            <br style="display: none;"> <!-- для адаптивности на маленьких экранах -->
            <span style="color: #ffb347;">✦</span> CatBoost <span style="color: #ffb347;">✦</span> XGBoost <span style="color: #ffb347;">✦</span> LightGBM
        </p>
    </div>
</div>



# 🏠 Прогнозирование цены недвижимости

Проект по разработке модели машинного обучения для предсказания стоимости объектов недвижимости на основе их характеристик, локации и инфраструктуры.

## 📋 Оглавление
- [Этапы проекта](#этапы-проекта)
- [Результаты](#результаты)
- [Используемые технологии](#используемые-технологии)
- [Структура репозитория](#структура-репозитория)
- [Запуск веб-сервиса](#запуск-веб-сервиса)
- [Рекомендации по улучшению](#рекомендации-по-улучшению)

---

## Этапы проекта

### 1. Подготовка данных
- Загрузка и первичный анализ данных, выявление пропусков и дубликатов.
- Десериализация сложных полей `homeFacts` и `schools` – извлечено 13 новых признаков (год постройки, рейтинг школ, системы отопления/охлаждения, тип парковки и др.).
- Унификация жаргонных сокращений и синонимов в категориальных признаках.
- Обработка пропусков по иерархической стратегии (по типу парковки, типу недвижимости, медиане, агрегации по почтовому индексу).
- Выявление и удаление выбросов с помощью метода Тьюки, `IsolationForest` и визуального анализа.

**Ключевые результаты:**
- Унифицировано 31 категория `propertyType`, 7 – `status`, 15 – `heating`, 10 – `cooling`, 14 – `parking`.
- Пропуски в `parking_counts` (248k) восстановлены по трёхуровневой схеме; `lotsize`, `beds`, `baths` – по типу недвижимости; `year_built` – по zipcode + типу.
- Удалены 1665 пропусков в целевой переменной `target`.

### 2. Разведывательный анализ и отбор признаков
- Построена корреляционная матрица. Наиболее сильная связь с ценой у `sqft` (0.56), `baths` (0.46), `average_rating_schools` (0.36).
- Географические факторы показали высокую вариативность: медианная цена в штате NY – 715k $, в топовых zip-кодах – до 4.7M $.
- Созданы новые признаки: `property_age`, `lot_utilization`, `school_access_score`, `amenities_weighted`, `sqft_per_room`, `bath_to_beds_ratio`, `total_living_rooms`, `effective_age`, `school_density`, частотные кодировки (`city_freq`, `state_freq`, `zipcode_freq`), таргет-кодирование `zipcode_target` (с KFold-сглаживанием, корреляция 0.74 по Spearman).
- Проведён статистический тест: наличие бассейна значимо повышает цену (p-value < 0.05).
- Отбор лучших признаков выполнен методом RFE на RandomForest.

### 3. Моделирование и оценка качества
**Метрики:** MAE (абсолютная ошибка), MAPE (относительная ошибка), R².

| Модель | MAE ($) | MAPE (%) | R² |
|--------|---------|----------|-----|
| RandomForest | 126 291 | 26 | 0.75 |
| CatBoost | 97 482 | 20 | 0.84 |
| XGBoost | 92 737 | 19 | 0.85 |
| **LightGBM** | **87 720** | **18** | **0.86** |

> **Важно:** Несмотря на разрыв между тренировочными и тестовыми метриками у бустингов, валидационная ошибка монотонно снижалась до последней итерации – модели **не переобучаются**, а обладают высокой ёмкостью и продолжают улучшать обобщение.

**Лучшие предсказания** (ошибка 0$):
- LightGBM: 207 990 $
- XGBoost: 51 400 $
- CatBoost: 875 000 $
- RandomForest: 388 314 $

**Худшие предсказания:** модели недооценивают аномально дорогие объекты (ошибка ~5 млн $ для домов ценой 5,6 млн $) – предсказание смещается к медиане.

### 4. Веб-сервис
Реализован сервер (`server.py`), загружающий сериализованную модель `lgb.pkl` и принимающий POST-запросы по эндпоинту `/predict`. Входные данные – JSON-формат (DataFrame), ответ – предсказанная цена.

---

## Результаты

- **Лучшая модель:** LightGBM  
- **MAE:** 87 720 $  
- **MAPE:** 18%  
- **R²:** 0.86  

Модель устойчива, быстро обучается, равномерно использует физические характеристики, инфраструктурные факторы и географию, не переобучаясь под конкретный почтовый индекс.

---

## Используемые технологии

- Python 3.10
- Pandas, NumPy – обработка данных
- Matplotlib, Seaborn – визуализация
- Scikit-learn – предобработка, RFE, метрики
- Optuna – подбор гиперпараметров
- LightGBM, XGBoost, CatBoost, RandomForest – модели
- SHAP – интерпретируемость
- Flask – веб-сервис
- Pickle – сериализация модели

---

## Структура репозитория
