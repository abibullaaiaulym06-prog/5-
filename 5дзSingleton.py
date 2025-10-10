import threading
import json

class ConfigurationManager:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        self.settings = {}

    @classmethod
    def get_instance(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = cls()
        return cls._instance

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                self.settings = json.load(f)
        except FileNotFoundError:
            print("Файл табылмады, бос конфигурация жасалды.")

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            json.dump(self.settings, f)

    def get_setting(self, key):
        return self.settings.get(key, "Мұндай параметр жоқ")

    def set_setting(self, key, value):
        self.settings[key] = value


\
def test_singleton():
    c1 = ConfigurationManager.get_instance()
    c2 = ConfigurationManager.get_instance()

    c1.set_setting("theme", "dark")
    print(c2.get_setting("theme"))

    print("Бір экземпляр ма?", c1 is c2)

test_singleton()
