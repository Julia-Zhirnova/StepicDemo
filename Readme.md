Данные для входа

1	Менеджер login1	pass1

2	Мастер login2	pass2

3	Оператор login4	pass4

4	Заказчик login11	pass11

Данные для проверки добавления:

Заходим под логином 1 и любым паролем и вносим данные

VALUES (
    12,        -- IDrequest (INTEGER)
    "2024-11-09",        -- startDate (TEXT)
    1,        -- orgTechTypeID (INTEGER)
    "DEXP Atlas H388",        -- orgTechModel (TEXT)
    "Перестал работать",        -- problemDescryption (TEXT)
    1,        -- requestStatusID (INTEGER)
    "2024-11-11",        -- completionDate (TEXT)
    "запчасти",        -- repairParts (TEXT)
    1,        -- masterID (INTEGER)
    1         -- clientID (INTEGER)
);