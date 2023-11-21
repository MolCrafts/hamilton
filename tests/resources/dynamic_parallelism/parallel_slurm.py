from hamilton.htypes import Collect, Parallelizable
from hamilton.execution.executors import SlurmTask


def num() -> int:
    return 10


def par(num: int) -> Parallelizable[int]:
    for i in range(num):
        yield i


def identity(par: int) -> SlurmTask:
    
    slurmTask = SlurmTask('/tmp')
    slurmTask.configs = {
        '-J': 'identity',
        '-o': 'identity.out',
        '-e': 'identity.err',
    }
    slurmTask.cmd = f'echo {par}'
    slurmTask.otuputs = ['identity.out', 'identity.err']
    return slurmTask


def foo() -> int:
    return 1


def collect(identity: Collect[SlurmTask], foo: int) -> int:
    list(identity)
    return foo


def collect_plus_one(collect: int) -> int:
    return collect + 1
