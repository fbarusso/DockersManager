from enum import Enum


class Option(Enum):
    EXIT = 1
    INDIVIDUAL_ACTIONS = 2
    LIST_CONTAINERS = 3
    RESTART_CONTAINERS = 4
    UP_CONTAINERS = 5
    DOWN_CONTAINERS = 6
    PULL = 7

    def get_menu_option(self) -> str:
        return f"{self.value} {self.name.replace('_', ' ').title()}"


class DockerOption(Enum):
    EXIT = 1
    ATOMIK_CRAWLERS = 2
    CRAWLER_WORKER = 3
    GLOBAL_API = 4
    PIPELINE_WORKER = 5

    def get_menu_option(self) -> str:
        return f"{self.value} {self.name.replace('_', ' ').title()}"

    def get_name(self) -> str:
        return f"risk3_{self.name.lower()}"

    def get_service_name(self) -> str:
        return f"risk3_sb_{self.name.lower()}"

    def get_directory(self) -> str:
        return f"git/risk3-dev/risk3-{self.name.replace('_', '-').lower()}"

    def get_color(self) -> str:
        if self == DockerOption.ATOMIK_CRAWLERS:
            return "bold cyan"
        elif self == DockerOption.CRAWLER_WORKER:
            return "bold magenta"
        elif self == DockerOption.GLOBAL_API:
            return "bold green"
        elif self == DockerOption.PIPELINE_WORKER:
            return "bold yellow"


class DockerActionOption(Enum):
    EXIT = 1
    LOGS = 2
    UP = 3
    STOP = 4
    REMOVE = 5
    BASH = 6
    CLEAN_AND_UPDATE = 7

    def get_menu_option(self) -> str:
        return f"{self.value} {self.name.replace('_', ' ').title()}"
