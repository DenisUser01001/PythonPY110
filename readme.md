# Практический курс знакомства с Django в рамках модуля "Основы разработки WEB приложений на языке Python"

Подробнее про работу с репозиториями через `github` можно прочитать в данном 
[руководстве](https://colab.research.google.com/drive/1H6Y52wD_8jOvS6kdvythcUNg7Vqf7mmZ)
(но ввиду постоянного обновления функционала и визуальной части github - 
некоторые названия могут быть другими и находиться в другом месте, но концепция 
взаимодействия останется той же)

Всегда самая актуальная информация находится в официальной [документации](https://docs.github.com/ru) 
`github`

А про взаимодействие `PyCharm` и `github` можно прочитать в данном 
[руководстве](https://colab.research.google.com/drive/1ydW7BYK2EUfgaRo49S8NwAHoKy7OIXrW)


## Шаги для работы с репозиторием через PyCharm 
Для работы с модулем можно использовать другое IDE, однако описание в шагах 2-9 
приведены применительно к IDE PyCharm

### Установка клиента Git (не нужно делать для тех кто ранее взаимодействовал с github и PyCharm) 

#### 1. Установка git клиента

Установить [git клиент](https://git-scm.com/downloads) (если он ещё не установлен)
в зависимости от вашей операционной системы.

![1.png](https://hse-labs.github.io/static/PythonPY110/pic_for_readme/1.png)

Для **Windows** необходимо скачать установочный exe файл. Сайт git сам подскажет какая версия нужна или можно скачать под определённую архитектуру

![2.png](https://hse-labs.github.io/static/PythonPY110/pic_for_readme/2.png)

Для Linux или MacOS скачивание идёт через системный терминал по соответствующим 
командам

![3.png](https://hse-labs.github.io/static/PythonPY110/pic_for_readme/3.png)

![4.png](https://hse-labs.github.io/static/PythonPY110/pic_for_readme/4.png)


### Настройка локального проекта

#### 2. Клонирование репозитория

Cкопируйте ссылку для клонирования репозитория 

![5.png](https://hse-labs.github.io/static/PythonPY110/pic_for_readme/5.png)

Откройте окно клонирования в PyCharm. В вашем проекте PyCharm 
(можно новом проекте, можно уже ранее используемом в курсе PY100)
зайдите в `VCS` (Version Control System, VCS вкладка появится в случае 
правильно установленного git клиента с 1-го шага) и далее `Get from Version Control` 

![6.png](https://hse-labs.github.io/static/PythonPY110/pic_for_readme/6.png)


Внесите скопированную ранее ссылку в поле `URL` и нажмите кнопку `Clone` 

![7.png](https://hse-labs.github.io/static/PythonPY110/pic_for_readme/7.png)

Далее появятся окна с вопросами о доверии к загружаемому репозиторию, где нужно нажать `Trust Project`.
Следующее окно будет с выбором места, где раскрыть окно с проектом, в текущем окне, или новом. Выбор за вами.

#### 3. Восстановление параметров (библиотек проекта) окружения

Затем `PyCharm` заметит в проекте файл `requirements.txt` со списком зависимостей 
проекта и предложит вам загрузить зависимости в ваше окружение. Для упрощения работы согласитесь. 

![8.png](https://hse-labs.github.io/static/PythonPY110/pic_for_readme/8.png)

через некоторое время все зависимости подгрузятся. 

#### 3.1 Если зависимости не подгрузились автоматически

Если зависимости не подгрузились, допустим из-за блокировок фаервола, то можно 
вручную загрузить зависимости, достаточно в консоле прописать команду 

```
pip install -r requirements.txt
``` 

(обратите внимание, что для корректной работы с проектом у вас должна быть активирована виртуальная среда, для этого в консоле 
должно быть написано `(venv)` у каретки в консоле) 

![9.png](https://hse-labs.github.io/static/PythonPY110/pic_for_readme/9.png)

Требование активированной среды гарантирует, что все зависимости установятся в данную среду.
Если не увидели данную надпись, то попробуйте создать новый терминал (нажав на `+`),
если надпись до сих пор не появилась, то попросите помощи преподавателя (возможно все нормально, просто не отображается)

#### 4. Загрузка проекта на ваш github аккаунт

Загрузите ваш проект на `github`. Для этого перейдите по вкладке `Git` далее
`GitHub` далее `Share Project on GitHub`

![10.png](https://hse-labs.github.io/static/PythonPY110/pic_for_readme/10.png)

#### 4.1 Авторизация github при интеграции через PyCharm (пропустите этот пункт, что уже ранее связывал PyCharm и github)

Если до текущего моменты если вы ни разу не работали с `github` через `PyCharm`, то будет необходимо 
связать `PyCharm` с `github`, чтобы иметь возможность вносить изменения в репозиторий
на `github` через `PyCharm`. 

Чтобы связать можно выбрать `Log In via GitHub` (связь через авторизацию 
на сайте jetbrains (разработчик PyCharm)) или `Log In with Token` (авторизация 
через создание и использование токена доступа с сайта `github`). 

![11.png](https://hse-labs.github.io/static/PythonPY110/pic_for_readme/11.png)

Выберем `Log In with Token` и нажмем `Generate`

![12.png](https://hse-labs.github.io/static/PythonPY110/pic_for_readme/12.png)

PyCharm перебросит на сайт `github`, где автоматически заполнит имя токена и необходимые права,
останется только выбрать срок действия токена, по умолчанию это 30 дней, но можно 
увеличить срок, выбираем `Custom` и выставляем срок на 1 год от текущей даты 
(предельно допустимый срок).

Листаем вниз нажимаем `Generate token`

![13.png](https://hse-labs.github.io/static/PythonPY110/pic_for_readme/13.png)

Скопируйте ваш токен (данный токен снова нельзя будет увидеть, если перезагрузить страницу,
а вы не успели воспользоваться токеном и его забыли, то
нужно будет снова создавать токен. Если планируете его использовать повторно, 
то храните его в надежном месте он даёт доступ к вашему аккаунту на `github`)

![14.png](https://hse-labs.github.io/static/PythonPY110/pic_for_readme/14.png)

Затем используйте этот токен в форме `PyCharm`, что была ранее

![15.png](https://hse-labs.github.io/static/PythonPY110/pic_for_readme/15.png)

В `Share by` увидите, что произошла связь с аккаунтом и наконец отправляет на 
`github` нажав `Share`.

![16.png](https://hse-labs.github.io/static/PythonPY110/pic_for_readme/16.png)

#### 4.2 Проверка создания репозитория

Можете проверить, что теперь на сайте `github.com` появился репозиторий с проектом, 
для это зайдите на `Git` далее `GitHub` далее `Open on GitHub`, откроется браузер с 
вашим репозиторием. Возможно нужно будет подождать некоторое время, чтобы вкладка отобразилась. 

![17.png](https://hse-labs.github.io/static/PythonPY110/pic_for_readme/17.png)

Или всегда можно проверить вручную на вашем аккаунте github


#### 5. Работа с практическим материалом

После загрузки проекта на github, начнём подготовку к лабораторной. Вся ваша работа 
на данном модуле будет проходить в ветке `master`, а по мере продвижения в модуле 
будете сливать новый материал из необходимой ветки с лабораторной работой в `master` ветку.

Загрузите вспомогательные данные для первой лабораторной работы (необходимо слить 
ветку `lab1` в ветку `master`). Слияние можно произвести в `PyCharm` несколькими 
способами. 

> Существует одно правило. Так как мы хотим слить ветку с лабораторной в `master` ветку, то
для этого мы должны находиться именно в `master` ветке. Т.е. если хотим слить все изменения из ветки
`B` в ветку `A`, то мы должны находиться в ветке `A`, такая же аналогия с веткой `master`(`main`) в которой 
на протяжении модуля вы работаете и именно в которую будете загружать все  

Выберете способ слияния удобный для себя:

#### 5.1 Слияние веток. Вариант 1. Через вкладку Git

> Через вкладку `Git`, далее `Merge` и далее выбираем какую ветку будем вливать в `master`
в нашем случае это ветка `origin/lab1` (приставка origin означает, что ветка `lab1`
находится на `github`)

![18.png](https://hse-labs.github.io/static/PythonPY110/pic_for_readme/18.png)

![19.png](https://hse-labs.github.io/static/PythonPY110/pic_for_readme/19.png)

#### 5.2 Слияние веток. Вариант 2. Через панель переключения веток

> Другой способ - это использовать панель переключения веток внизу справа в `PyCharm`.
Для этого нажимаем на ветку `master` далее нажимаем на `origin/lab1`, где в 
выпадающем окне выбираем `Merge 'origin/lab1' into 'master'`

![20.png](https://hse-labs.github.io/static/PythonPY110/pic_for_readme/20.png)


#### 5.3 Отправка веток с лабораторными на github

К сожалению, когда вы поделились проектом на github, то перенеслась только ваша `master` (`main`) ветка, так как
на момент переноса с локального проекта (на вашем компьютере) на github была только одна ветка 
`master` (`main`) и если бы до переноса проекта зашли бы на все ветки, то они бы перенеслись на github одним действием.

Поэтому сейчас для будущей тренировки перенесем вручную каждую ветку. Для этого

1. Перейдем на ветку lab1 (переход делается при помощи `Checkout`)

![21.png](https://hse-labs.github.io/static/PythonPY110/pic_for_readme/21.png)


2. Затем отправим эту ветку на github. Для этого нажмем на `Push`

![22.png](https://hse-labs.github.io/static/PythonPY110/pic_for_readme/22.png)

3. Зайдите на остальные ветки `lab2`, `lab3`, `lab4`, `lab5` и отправьте их на гитхаб. Помните, 
что отправить за раз можно только одну ветку, поэтому как только перешли на ветку (`Checkout`), то отправьте её (`Push`)

4. После того как отправили все ветки, то вернитесь в вашу основную ветку `master` (`main`)

#### 5.4 Выполнение заданий практики

После слияния `master` и `lab1` появятся папки `files` и `tasks`. 
В папке `tasks` в соответствующей 
папке с лабораторной работой (папки в `tasks` с лабораторными работами будут 
подгружаться с вашими последующими слияниями с ветками lab2, lab3, lab4, lab5)
находится файл `readme.md` в котором содержатся задания для лабораторной работы.
В папке `files` находится дополнительный материал необходимый для выполнения
лабораторной работы.

Откройте файл `readme.md` в папке `tasks/lab1` и начните выполнять первую 
лабораторную работу.