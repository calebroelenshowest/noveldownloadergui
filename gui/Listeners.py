from pubsub import pub


class Message:

    @staticmethod
    def error(message: str):
        pub.sendMessage("error", error=message)

    @staticmethod
    def warning(warning: str):
        pub.sendMessage("warning", warning=warning)


class Download:

    @staticmethod
    def download_progress_percentage(percentage: float):
        pub.sendMessage("download_percentage", progress=percentage)

    @staticmethod
    def download_progress_numbers(now: int, done: int):
        pub.sendMessage("download_number", now=now, max=done)

