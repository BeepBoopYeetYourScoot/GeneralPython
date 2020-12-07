# Для отлавливания ошибок в Питоне существует стандартный блок:

try:
    pass
except Exception:
    pass
# else:
#     pass
# finally:
#     pass

# Исключения нужно располагать следующим образом: сначала должны идти более специфичные,
# затем - более общие. В одном блоке можно обрабатывать несколько исключений

try:
    pass
except FileNotFoundError:
    pass
except ModuleNotFoundError:
    pass
except NotImplementedError:
    pass

# Блок 'else' выполняется в том случае, если блок 'try' не выдаёт исключения

try:
    f = open('test_file.txt')
except FileNotFoundError as err:
    print(err)
except ModuleNotFoundError as err:
    print(err)
except NotImplementedError as err:
    print(err)
else:
    print(f.read())
    f.close()

# Блок 'finally' выполняется в любом случае:

try:
    f = open('testfile.txt')
except FileNotFoundError as err:
    print(err)
except ModuleNotFoundError as err:
    print(err)
except NotImplementedError as err:
    print(err)
else:
    print(f.read())
    f.close()
# finally:
#     print('Testing Finally Block')


# Исключения можно вызывать самому - не обязательно, чтобы их выдавала только сама программа
# Попробуем создать кастомный exception

class CorruptDataException(Exception):

    def __init__(self, message='Data in the file is corrupted!'):
        self.message = message
        super().__init__(self.message)


try:
    f = open('corrupt_file.txt')
    if f.read() == 'Corrupt data':
        raise CorruptDataException
except FileNotFoundError as err:
    print(err)
except CorruptDataException as exc:
    print(exc)
except Exception as exc:
    print(exc)
else:
    print(f.read())
    f.close()
# finally:
#     print('Testing Finally Block')












