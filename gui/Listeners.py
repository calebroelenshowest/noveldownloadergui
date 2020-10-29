from pubsub import pub
from novelcores.novelclass.Func import ExFunc


class Message:

    @staticmethod
    def error(message: str):
        pub.sendMessage("error", error=message)

    @staticmethod
    def warning(warning: str):
        pub.sendMessage("warning", warning=warning)

    @staticmethod
    def message(message: str):
        pub.sendMessage("message", data=message)


class Download:

    @staticmethod
    def download_progress_percentage(percentage: float):
        pub.sendMessage("download_percentage", progress=percentage)

    @staticmethod
    def download_progress_numbers(now: int, done: int):
        pub.sendMessage("download_number", now=now, max=done)


class NovelPub:

    @staticmethod
    def download_novel_info(novel_info: dict):
        source_set = novel_info["source"]
        source_url = novel_info["url"]

        novel_compiled = {}
        soup = source_set.get_soup(source_url)

        novel_compiled["title"] = source_set.get_title(soup)
        Message.message("Title: " + novel_compiled["title"])

        novel_compiled["author"] = source_set.get_author(soup)
        Message.message(f"Author: {novel_compiled['author']}")

        novel_compiled["chapters"] = source_set.get_url_chapters(soup)
        Message.message(f"Found {len(novel_compiled['chapters'])} chapters")

        novel_compiled["image"] = ExFunc.download_image(source_set.get_url_image(soup))
        if isinstance(novel_compiled["image"], bool):
            Message.error("No image found")
        else:
            Message.message(f"Downloaded image ({novel_compiled['image']})")

        pub.sendMessage("novel_display_update", novel_info=novel_compiled)
