import sys
import logging

from src.exceptions import ParamsError
from tests.benchmarks.timeit_once import timeit_once_cli

from src.cli.command import Command
from src.cli.constants import SORTES, ALGOS, STACK, QUEUE, COMMANDS
from src.cli.manager import CliManager


cli_manager = CliManager()

def tokenize_list(text: str, typ: type = int) -> list:
    return [typ(token) for token in text.split(',')]


def start_sort(command: Command) -> None:

    sort_func, dig_type = SORTES[command.command]['func'], SORTES[command.command]['type']

    if dig_type == 'float':
        if command.params:
            test_list = tokenize_list(command.params[0], float)

        else:
            test_list = cli_manager.test_float_list

    else:
        if command.params:
            test_list = tokenize_list(command.params[0], int)

        else:
            test_list = cli_manager.test_int_list

    if command.flags:
        if '-b' in command.flags:
            sort_time, sorted_list = timeit_once_cli(sort_func, test_list)
            print(f'{sorted_list}\nВремя выполнения -> {sort_time} сек.')

    else:
        print(sort_func(test_list))


def start_algos(command: Command) -> None:

    algos_func = ALGOS[command.command]

    if command.params:
        test_num = int(command.params[0])

    else:
        test_num = 3

    if command.flags:
        if '-b' in command.flags:
            algos_time, algos_result = timeit_once_cli(algos_func, test_num)
            print(f'Входное число -> {test_num}\nРезультат -> {algos_result}\nВремя исполнения -> {algos_time} сек.')

    else:
        print(algos_func(test_num))


def start_stack_cmd(command: Command) -> None:
    if not command.params:
        print('Доступные команды для stack:\nstack push 1\nstack pop\nstack peek\nstack is_empty\nstack min\nstack len')
        return

    cmd = command.params[0]

    if cmd == 'push':
        if len(command.params) < 2:
            raise ParamsError('Вы не ввели элемент, который хотите добавить в стек')

        value = int(command.params[1])
        cli_manager.stack.push(value)

        print(f'{value} добавлен в стек')
        return

    if cmd == 'clear':
        cli_manager.clear_stack()
        print('Стек успешно очищен')
        return

    if cmd == 'len':
        print(f'Длинна стека {len(cli_manager.stack)}')
        return

    if cmd in STACK:
        method = getattr(cli_manager.stack, cmd)

        result = method()

        if cmd == 'pop':
            print(f'Элемент {result} успешно взят из стека')

        else:
            print(result)

    else:
        print('Доступные команды для стека\nstack push 1\nstack pop\nstack peek\nstack is_empty\nstack min')


def start_queue_cmd(command: Command) -> None:
    if not command.params:
        print('Доступные команды для очереди:\nqueue enqueue 1\nqueue dequeue\nqueue front\nqueue is_empty\nqueue len')
        return

    cmd = command.params[0]

    if cmd == 'enqueue':
        if len(command.params) < 2:
            raise ParamsError('Вы не ввели элемент, который хотите добавить в очередь')

        value = int(command.params[1])
        cli_manager.queue.enqueue(value)

        print(f'{value} добавлен в очередь')
        return

    if cmd == 'clear':
        cli_manager.clear_queue()
        print('Очередь успешно очищена')
        return

    if cmd == 'len':
        print(f'Длинна очереди {len(cli_manager.queue)}')
        return

    if cmd in QUEUE:
        method = getattr(cli_manager.queue, cmd)

        result = method()

        if cmd == 'dequeue':
            print(f'Элемент {result} успешно взят из очереди')

        else:
            print(result)

    else:
        print('Доступные команды для очереди:\nqueue enqueue 1\nqueue dequeue\nqueue front\nqueue is_empty\nqueue len')


def formating(text: str) -> str:
    return text.lower().strip()


def main_loop():
    print('Интерфейс "Андрюшка" успешно запушен, чтобы посмотреть доступный функционал, введите "help".')
    print('>', end='')

    for inpt in sys.stdin:
        try:
            inpt = formating(inpt)

            command = Command(inpt)

            if command.command == '':
                print('>', end='')
                continue

            elif command.command in ['break', 'stop', 'exit', 'quit']:
                print('Интерфейс "Андрюшка" успешно остановлен.')
                break

            elif command.command == 'help':
                print(COMMANDS)

            elif command.command == 'lists':
                print(f'Список целых чисел: {cli_manager.test_int_list}\nСписок вещественных чисел: {cli_manager.test_float_list}')

            elif command.command == 'rc':
                cli_manager.generate_float_test_list()
                cli_manager.generate_int_test_list()
                print(f'Тестовые списки перегенерированы!')

            elif command.command in SORTES:
                start_sort(command)

            elif command.command in ALGOS:
                start_algos(command)

            elif command.command == 'stack':
                start_stack_cmd(command)

            elif command.command == 'queue':
                start_queue_cmd(command)

            print('>', end='')

        except Exception as error:
            logging.error(f'Ошибка исполнения команды "{inpt}": {error}')
            print('>', end='')