def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for item in items:
            value = item.get(args[0])
            if value is not None:
                yield value
    else:
        for item in items:
            result = {arg: item.get(arg) for arg in args if item.get(arg) is not None}
            if result:
                yield result

# Тестирование
if __name__ == "__main__":
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]
    print(list(field(goods, 'title')))
    print(list(field(goods, 'title', 'price')))

#