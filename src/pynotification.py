import os
import shutil
import platform
from pathlib import Path
from plyer import notification
from typing import Optional


def notify(**kwargs):
    _title: str = kwargs.get('title', "Title")
    _subtitle: str = kwargs.get("subtitle", None)
    _text: str = kwargs.get("text", "Notification Message")
    _image_path: str = kwargs.get("image_path", None)

    if platform.system() == 'Darwin':
        notify_macos(title=_title, text=_text, subtitle=_subtitle, image_path=_image_path)
    elif platform.system() == 'Linux':
        notify_linux(title=_title, text=_text, image_path=_image_path)
    elif platform.system() == 'Windows':
        notify_windows(title=_title, text=_text, image_path=_image_path)
    else:
        pass


def change_icon(new_image_path_: str):
    new_image_path_ = Path(new_image_path_)
    if new_image_path_.suffix == ".icns":
        old_image_path = Path("popup.app/Contents/Resources/applet.icns")
        if os.path.isfile(old_image_path):
            os.remove(old_image_path)
            shutil.copyfile(new_image_path_, old_image_path)


def notify_macos(title: str, text: str, subtitle: Optional[str], image_path: Optional):
    if image_path is not None:
        change_icon(image_path)

    os.system(
        """osascript -e 'tell application "popup.app" to notify("{}", "{}", "{}")'""".format(text, title, subtitle))
    os.system("""osascript -e 'quit app "popup"'""")


def notify_linux(title, text, image_path: Optional):
    os.system('notify-send -i "{}" "{}" "{}"'.format(image_path, title, text))


def notify_windows(title, text, image_path: Optional):
    notification.notify(
        title=title,
        message=text,
        timeout=50,
        app_icon=image_path
    )
