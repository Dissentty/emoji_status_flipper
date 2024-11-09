# emoji status flipper by dissenty
**emoji status flipper** - небольшая программа для постоянного изменения эмодзи статуса в Telegram.

### Запуск программы

Перед запуском игры необходимо создать файл .env, который будет выполнен в подобном формате:
```commandline
API_ID={ваш api_id без кавычек}
API_HASH={ваш api_hash без кавычек}
```
api_id и api_hash необходимо достать с сайта me.telegram.org.

При запуске программы необходимо ввести номер, код и пароль для входа на аккаунт, все данные сохранятся в файле session.session.

В список statuses необходимо внести все айди эмодзи, которые вы бы хотели видеть в своем статусе.

interval отвечает за время в секундах между сменой статуса, не советую ставить его слишком низким.
#### Внимание!

**Никому не пересылайте файл session.session, иначе имеете шанс потерять свой telegram аккаунт.**

**За безопасность вашего аккаунта не несу никакой ответственности никакой не несу, вопрос законности относительно правил telegram не изучался. Иногда программа ловит ограничение на 20 минут, в течении которых не работает, возможно стоит уменьшить интервал изменения**