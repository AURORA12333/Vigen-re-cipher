# Шифровка текста с использованием метода Vigenère

## Краткое описание программного обеспечения

Эта программа реализует шифрование и дешифрование текста с использованием **шифра Виженера**. Пользователь может выбрать режим работы (шифрование или дешифрование), ввести текст и ключ, после чего программа выведет результат.

## Инструкция по установке и запуску

1. Перейдите в папку `dist` в репозитории.
2. Найдите и нажмите на файл `main.exe`.
4. Нажмите на три точки в правом верхнем углу экрана и выберите **Download** для скачивания `main.exe`.
5. Запустите `main.exe` на своём компьютере. Программа не требует установки Python или других дополнительных файлов.

## Инструкция по использованию

1. При запуске программы вам будет предложено выбрать:
   - Нажмите `1`, чтобы **зашифровать** текст.
   - Нажмите `2`, чтобы **дешифровать** текст.
2. Введите текст для шифрования или дешифрования (буквы на английском языке) и нажмите `Enter`.
   - **Пример текста**: `HELLO`
3. Введите ключ для шифрования/дешифрования (буквы на английском языке) и нажмите `Enter`.
   - **Пример ключа**: `KEY`

### Пример работы программы

- Выберите режим работы, нажав `1` для шифрования текста.
- Введите текст, например: `HELLO`
- Введите ключ, например: `KEY`
- Программа выведет зашифрованное сообщение.

Для дешифрования:
- Перезапустите программу и выберите `2`.
- Введите зашифрованный текст, который вы получили, и используйте тот же ключ для расшифровки.

## Документация

- **Функция `keycode(s)`**: принимает символ `s` и возвращает его индекс в алфавите. Используется для преобразования символов в числовые значения.
- **Функция `encode(text, key)`**: принимает текст `text` и ключ `key`, возвращает зашифрованное сообщение.
- **Функция `decode(text, key)`**: принимает текст `text` и ключ `key`, возвращает расшифрованное сообщение.
- **Функция `main()`**: предоставляет пользовательский интерфейс для выбора шифрования/дешифрования и ввода текста и ключа.

## Инструкция по совместной работе

Если вы хотите внести изменения в код или предложить улучшения:
1. Форкните репозиторий.
2. Создайте новую ветку для своих изменений:
```bash
   git checkout -b feature-branch-name
```
3.Внесите изменения и закоммитьте их.
4.Отправьте изменения в свою ветку:
```bash
git push origin feature-branch-name
```
5.Создайте Pull Request в оригинальный репозиторий.

## Информация об авторских правах и лицензировании
Данный проект доступен под лицензией MIT. Вы можете использовать, копировать, изменять и распространять код на условиях данной лицензии.

Автор: Нарежнев Александр, группа 22исп7
