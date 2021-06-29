# Тестовое задание для компании nlstar.
## **Условия**
1. Дана модель предметной области с сущностями:
   1. Страница (Page)
   2. Контент типа видео (Video)
      - специфичные атрибуты: ссылка на видеофайл, ссылка на файл субтитров
   3. Контент типа аудио (Audio)
      - специфичные атрибуты: битрейт в количестве бит в секунду
   4. Контент типа текст (Text)
      - специфичные атрибуты: поле для хранения текста произвольной длинны
2. Нужно учитывать, что специфичные атрибуты разных видов контента существенно различаются.
3. У всех видов контента присутствует атрибут "счетчик просмотров" (counter).
4. У всех видов контента и страниц есть атрибут "заголовок" (title).
5. Со страницей может быть связан любой вид контента в любом количестве. Семантика такая: "на страницу можно выложить любой вид контента в любом количестве". Например: на странице может быть 5 видео, 3 аудио и 7 текстов в любом порядке и в перемешку.
   - Следует учитывать, что будущем виды контента могут добавляться и функционал должен легко расширяться
***

## **Функциональные требования**
1. Сделать **API** для получения списка **всех страниц**.
   - Должна поддерживаться **пагинация** (постраничная выдача результатов)
   - В ответе должен содержаться **URL** на **API с детальной информацией** о странице (пункт №2).
2. Сделать **API** для получения **детальной информации** о странице.
   - Помимо атрибутов страницы в ответе **должны содержаться** все привязанные к странице **объекты контента** в виде вложенной структуры - упорядоченного списка привязанных к странице объектов контента со всеми атрибутами, включая специфичные.
3. При обращении к API с деталями о странице **счетчик просмотров** каждого объекта контента, привязанного к странице **должен увеличиваться на единицу**.
   - Нагрузка на данное API предполагается существенная, поэтому желательно непосредственно **изменение данных** в БД реализовать **в фоновой задаче**.
   - Важно обратить внимание, что **увеличение счетчика** должно происходить **строго атомарно**. То есть, если две задачи параллельно обновляют счетчик одного объекта, то на выходе сегда должно получаться "+2".
4. **Заведение страниц и привязка** к ним **контента** должна выполняться **через админку**.
   - Должен поддерживаться **поиск по заголовку (title)** страниц и контента по (частичному совпадению от начала).
   - Желательно для удобства **реализовать привязку и управление контентом** на странице **в виде inline-блоков** в разделе управления страницей (Page) в админке.
   - Желательно, чтобы была **возможность задавать порядок выдачи** в API объектов, привязанных к странице.
***

# TODO: 1. Добавить:
- [x] Пагинацию
- [x] URL на API с детальной информацией
# TODO: 2. Добавить:
- [x] Detail API, к странице должен быть привязан весь контент(обратный foreign key)
# TODO: 3. Добавить:
- [] Счетчик просмотров контента при выполнении вьюхи на просмотр detail'а страницы через таску
- [] Celery, выполняющий вьюху через очередь(RQ, Reddis)
# TODO: 4. Добавить:
- [x] Поиск по заголовкам + text от начала
- [x] Inline-блоки в админке
- [ ] Вьюху на порядок выдачи связанного с моделью Page контента

# TODO Final Part:
- [] Упаковать все в Docker
