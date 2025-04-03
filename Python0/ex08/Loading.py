import sys
from time import sleep, time
from typing import Generator

def ft_tqdm(lst: range) -> Generator[int, None, None]:
    """Custom tqdm function that shows a progression bar whilst loading data.
    This function is being using for many instances in frontend and iteractive purposes"""
    total = len(lst)
    bar_length = 50
    start_time = time()
    
    for i, value in enumerate(lst, 1):
        progress = i / total
        filling = int(progress * bar_length)
        bar = "█" * filling + " " * (bar_length - filling)
        per = int(progress * 100)
        
        # Custom elapsed time [] to match the builtin tqdm
        elapsed_time = time() - start_time
        remaining_time = (elapsed_time / progress) - elapsed_time if progress > 0 else 0
        iter_per_sec = i / elapsed_time if elapsed_time > 0 else 0
        elapsed_str = f"{int(elapsed_time // 60):02}:{int(elapsed_time % 60):02}"
        remaining_str = f"{int(remaining_time // 60):02}:{int(remaining_time % 60):02}"
        iter_per_sec_str = f"{iter_per_sec:6.2f}it/s" 

        sys.stdout.write(f"\r{per}%|{bar}| Loading...")
        sys.stdout.flush()
        
        yield value
        
        sleep(0.005)

    # After the loop finishes, print the final progress bar
    sys.stdout.write(f"\r100% |{('█' * bar_length)}| {len(lst)}/{len(lst)} [{elapsed_str}<00:00, {iter_per_sec_str}] Loading Complete\n")
    sys.stdout.flush()
