Скрипт для выгрузки списка подписчиков из Instagram с использованием Instaloader и Python. Поддерживает 2FA и кэширование сессии.

---

## 🔧 Подготовка

### 1. Установи Python (>= 3.8)

- **Windows:** скачать с [python.org](https://www.python.org/downloads/windows/)
- **macOS:** через [Homebrew](https://brew.sh/): `brew install python`
- **Linux (Debian/Ubuntu):**
  ```bash
  sudo apt update && sudo apt install python3 python3-venv python3-pip
  ```

### 2. Клонируй репозиторий и создай виртуальное окружение
```bash
git clone https://github.com/yourname/instagrabber.git
cd instagrabber
python3 -m venv myvenv
source myvenv/bin/activate  # Windows: myvenv\Scripts\activate
```

### 3. Установи зависимости
```bash
pip install -r requirements.txt
```

### 4. Создай файл `.env`
```env
INSTAGRAM_USERNAME=your_username
INSTAGRAM_PASSWORD=your_password
```

> ⚠️ Пароль будет использоваться только один раз — затем сессия кэшируется локально.

---

## 🚀 Запуск
```bash
python instagrabber.py
```

### Что произойдёт:
- Скрипт попытается загрузить сохранённую сессию (`<username>_session`)
- Если файл не найден — запросит логин и 2FA-код
- Сохраняет сессию в файл и использует его при следующих запусках
- Выгружает подписчиков в `followers.csv` в формате:
  ```csv
  id,username,full_name
  1234567890,johndoe,John Doe
  ```

---

## ✅ Поддержка платформ
- [x] macOS
- [x] Linux
- [x] Windows (через `cmd` или `PowerShell`)

---

## 📦 Зависимости
- `instaloader`
- `python-dotenv`

Создай `requirements.txt` при необходимости:
```bash
pip freeze > requirements.txt
```

---

## 🛡️ Безопасность
- Не коммить файл `.env`
- Храни файл сессии (`<username>_session`) в защищённой папке

---

## 📄 Лицензия
MIT
