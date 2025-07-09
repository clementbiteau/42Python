import sys
from time import sleep, time

def ft_tqdm(lst: range):
    """Custom tqdm function that shows a progression bar whilst loading data.
    This function is being used for many instances in frontend and iteractive purposes
    1) We define the length of bar as well as a timer to init
    2) for each index enumerated in our range, we print a █ filler
    3) We customize the printing of the bar"""
    total = len(lst)
    bar_length = 50
    start_time = time()

    for i, value in enumerate(lst, 1):
        progress = i / total
        filling = int(progress * bar_length)
        bar = "█" * filling + " " * (bar_length - filling)
        per = int(progress * 100)

        elapsed_time = time() - start_time
        remaining_time = (elapsed_time / progress) - elapsed_time if progress > 0 else 0
        iter_per_sec = i / elapsed_time if elapsed_time > 0 else 0
        elapsed_str = f"{int(elapsed_time // 60):02}:{int(elapsed_time % 60):02}"
        remaining_str = f"{int(remaining_time // 60):02}:{int(remaining_time % 60):02}"
        iter_per_sec_str = f"{iter_per_sec:6.2f}it/s"

        sys.stdout.write(f"\r{per}%|{bar}| [{elapsed_str}<{remaining_str}, {iter_per_sec_str}] Loading...")
        sys.stdout.flush()

        yield value

        sleep(0.008)

    sys.stdout.write(f"\r100% |{'█' * bar_length}| {total}/{total} [{elapsed_str}<00:00, {iter_per_sec_str}] Loading Complete\n")
    sys.stdout.flush()
