# Документация API Кулинарной Книги

## Обзор
API Кулинарной Книги позволяет управлять коллекцией рецептов. Оно предоставляет эндпоинты для получения списка рецептов, получения детальной информации о конкретном рецепте и добавления новых рецептов в базу данных. Сервис построен с использованием **FastAPI** и **SQLAlchemy**.

---

## Функционал

### Эндпоинты
1. **GET /recipes**
   - Возвращает список всех рецептов.
   - **Данные ответа**:
     - `title` (string): Название блюда.
     - `views` (integer): Количество просмотров рецепта.
     - `preparation_time` (integer): Время приготовления (в минутах).
   - **Сортировка**:
     - По количеству просмотров (убывание).
     - По времени приготовления (возрастание), если количество просмотров совпадает.

2. **GET /recipes/{recipe_id}**
   - Возвращает детальную информацию о рецепте.
   - **Параметр пути**:
     - `recipe_id` (integer): Уникальный идентификатор рецепта.
   - **Данные ответа**:
     - `title` (string): Название блюда.
     - `preparation_time` (integer): Время приготовления (в минутах).
     - `ingredients` (list of strings): Список ингредиентов.
     - `description` (string): Описание рецепта.
     - `views` (integer): Количество просмотров рецепта.

3. **POST /recipes**
   - Создает новый рецепт.
   - **Тело запроса** (JSON):
     - `title` (string, обязательное): Название блюда.
     - `preparation_time` (integer, обязательное): Время приготовления (в минутах).
     - `ingredients` (list of strings, обязательное): Список ингредиентов.
     - `description` (string, обязательное): Описание рецепта.
   - **Ответ**:
     - Возвращает созданный объект рецепта.

---

## Модели

### Recipe
- **Атрибуты**:
  - `id` (integer, primary key): Уникальный идентификатор рецепта.
  - `title` (string): Название блюда.
  - `preparation_time` (integer): Время приготовления (в минутах).
  - `ingredients` (string): Список ингредиентов (строка, разделенная запятыми).
  - `description` (string): Описание рецепта.
  - `views` (integer, default = 0): Количество просмотров рецепта.

---

## Документация

Этот API документирован с использованием **OpenAPI**. Документация доступна по следующим адресам:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## Экраны

### 1. Экран списка рецептов
- Отображает таблицу со следующими колонками:
  - `title`: Название блюда.
  - `views`: Количество просмотров рецепта.
  - `preparation_time`: Время приготовления (в минутах).
- **Сортировка**:
  - По количеству просмотров (убывание).
  - По времени приготовления (возрастание), если просмотры равны.

### 2. Экран детальной информации о рецепте
- Отображает детальную информацию о рецепте:
  - `title`: Название блюда.
  - `preparation_time`: Время приготовления.
  - `ingredients`: Список ингредиентов.
  - `description`: Описание рецепта.

---

## Используемые технологии
- **FastAPI**: Фреймворк для разработки API.
- **SQLAlchemy**: ORM для работы с базой данных.
- **SQLite**: База данных для хранения рецептов.

---

## Как запустить
1. Склонируйте репозиторий.
2. Установите зависимости с помощью команды:
   ```bash
   pip install -r requirements.txt
   ```
3. Запустите приложение:
   ```bash
   uvicorn main:app --reload
   ```
4. Откройте API по адресу [http://localhost:8000](http://localhost:8000).
