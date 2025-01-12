from kittens.tui.handler import result_handler

@result_handler
def main(tab, tabs, current_tab):
    # Format for active tab
    if tab == current_tab:
        return f"\x1b[31m{tab.num_windows}\x1b[0m:{tab.title}"  # Red `num_windows`
    # Format for inactive tabs
    return f"\x1b[37m{tab.num_windows}\x1b[0m:{tab.title}"  # White `num_windows`

