# noinspection PyShadowingBuiltins,PyUnusedLocal
  
def compute(value1: int, value2: int) -> int:
        if value1 not in [0,100] or value2 not in [0,100]:
            raise Exception("params not in accepted range")

        return int(value1 + value2)
