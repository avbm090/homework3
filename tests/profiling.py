import cProfile
import pstats
import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import main

def profiling():
    profiler = cProfile.Profile()
    profiler.enable()
    main.main()
    profiler.disable()

    stats = pstats.Stats(profiler).sort_stats("cumtime")
    stats.print_stats(5)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    txt_path = f"tests/profiling_output_{timestamp}.txt"

    with open(txt_path, "w") as f:
        stats = pstats.Stats(profiler, stream=f).sort_stats("cumtime")
        stats.print_stats()

if __name__ == "__main__":
    profiling()
