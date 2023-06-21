import time

from insert_query import query

import pandas as pd
import watchdog.events
import watchdog.observers


class Handler(watchdog.events.PatternMatchingEventHandler):
    """Notifies when 'archivo.csv' is modified. 
    """

    def __init__(self):
        """Set the patterns for PatternMatchingEventHandler
        """
        watchdog.events.PatternMatchingEventHandler.__init__(
            self,
            patterns=['archivo.csv'],
            ignore_directories=True,
            case_sensitive=False
        )
        df = pd.read_csv('data/archivo.csv')
        self.number_of_lines = df.shape[0]

    def on_modified(self, event):
        """Is executed when file 'archivo.csv' is modified.

        Args:
            event: A watchdog event that is triggered when a change
            occurs on the aforementioned file. It is based of 
            watchdog.events.FileSystemEvent.
        """
        print("Watchdog received modified event - % s." % event.src_path)
        # Event is modified, you can process it now
        df = pd.read_csv(event.src_path)

        if df.shape[0] > self.number_of_lines:
            # New line added to CSV file
            last_line = df.iloc[-1].to_dict()
            self.number_of_lines = df.shape[0]
            print()
            print("======== The query is ==========")
            print(query.format(**last_line))
            

if __name__ == "__main__":
    src_path = r"data/"
    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=src_path)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
