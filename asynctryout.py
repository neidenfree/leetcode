import asyncio
from typing import Any, Awaitable


async def some(ms: float, **kwargs) -> None:
    if "name" in kwargs:
        task_name = f'''Task {kwargs['name']}'''
    else:
        task_name = ""
    print(f"{task_name} started")
    await asyncio.sleep(ms)
    print(f"{task_name} is done!")


async def some2(ms: float, **kwargs) -> int:
    if "name" in kwargs:
        task_name = f'''Task {kwargs['name']}'''
    else:
        task_name = "Unnamed task"
    print(f"{task_name} started")
    await asyncio.sleep(ms)
    print(f"{task_name} is done!")
    return int(ms * 1000)


async def run_sequence(*functions: Awaitable[Any]) -> None:
    for function in functions:
        await function


async def run_parallel(*functions: Awaitable[Any]) -> None:
    await asyncio.gather(*functions)


async def main():
    value = 0
    # await run_parallel(
    #     some(2.2, name="Slow"),
    #     run_sequence(
    #         some2(1.2, name="Sequential first"),
    #         some2(0.2, name="Sequential second"),
    #         some2(0.3, name="Sequential third")
    #     ),
    #     some(1.3, name="Middle"),
    #     some(2.2, name="Slow"),
    #     some(0.5, name="Fast"),
    #     some(0.5, name="Fast"),
    # )
    #
    await run_parallel(
        *(some(x, name=f"{i}-th") for i, x in enumerate([1.2, 0.5, 0.8, 0.4, 3.2, 0.7]))
    )

    print(await some2(1.4))


if __name__ == "__main__":
    asyncio.run(main())
