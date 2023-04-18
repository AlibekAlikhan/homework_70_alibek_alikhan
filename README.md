# homework_70_alibek_alikhan
### когда вы загрузите себе fixtures, у меня tasks начинаются с 7мого pk
##Пример детального просмотра tasks "url":
GET```{
 http://127.0.0.1:8000/api/tasks/detail/8
}```

##Пример обновления tasks "url":
PUT```{
 http://127.0.0.1:8000/api/tasks/resources/8
}```
## Дефолдные данные для обновления

 {
    "id": 8,
    "status": 3,
    "teg": [
        2
    ],
    "text": "aыыыыsdfsdsfsdd",
    "detail_text": "sdfsfdssdsf",
    "project": 3,
    "create_at": "2023-03-10T19:13:52.569000+06:00",
    "iis_deleted": true
}

##Пример детального просмотра project "url":
GET  http://127.0.0.1:8000/api/project/detail/2


##Пример обновления project "url":
PUT http://127.0.0.1:8000/api/project/resources/2
## Дефолдные данные для обновления
{
    "id": 2,
    "start_at": "2023-03-17",
    "end_at": "2023-03-11",
    "name": "ASD",
    "text_project": "fd fgdgfdfdfgdf dg fdgfgfghfh gfhggdfsd",
    "iis_deleted": false,
    "deleted_project_at": null
}


