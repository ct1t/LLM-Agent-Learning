# -*- coding: utf-8 -*-
"""第1周 · 虚拟环境冒烟测试：用足本周知识点（类型注解/异常/生成器）。

运行：.venv\\Scripts\\python.exe hello.py
期望输出：
  total = 15
  生成器取前 3 个偶数: [0, 2, 4]
  捕获到异常: division by zero
  环境就绪：Python 3.10.x（venv 隔离生效）
"""

import sys
from typing import List, Optional


def add_all(nums: List[int]) -> int:
    """类型注解示例：累加列表。"""
    total: int = 0
    for n in nums:
        total += n
    return total


def even_gen(limit: int):
    """生成器示例：产出不超过 limit 的偶数。"""
    for i in range(limit):
        if i % 2 == 0:
            yield i


def safe_divide(a: float, b: float) -> Optional[float]:
    """异常处理示例：除零时返回 None 而非抛错。"""
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f"捕获到异常: {e}")
        return None


if __name__ == "__main__":
    print(f"total = {add_all([1, 2, 3, 4, 5])}")
    first3: List[int] = []
    for idx, val in enumerate(even_gen(10)):
        if idx >= 3:
            break
        first3.append(val)
    print(f"生成器取前 3 个偶数: {first3}")
    safe_divide(1, 0)
    print(f"环境就绪：{sys.version.split()[0]}（venv 隔离生效）")
