from rich.console import Console

from actions import (
    list_containers,
    restart_containers,
    up_containers,
    down_containers,
    logs,
    up,
    stop,
    remove,
    bash,
    clean_and_update,
    pull,
    clean_and_update_all,
)
from constants import Option, DockerOption, DockerActionOption


def input_option() -> Option:
    print(Option.EXIT.get_menu_option())
    print(Option.INDIVIDUAL_ACTIONS.get_menu_option())
    print(Option.LIST_CONTAINERS.get_menu_option())
    print(Option.RESTART_CONTAINERS.get_menu_option())
    print(Option.UP_CONTAINERS.get_menu_option())
    print(Option.DOWN_CONTAINERS.get_menu_option())
    print(Option.PULL.get_menu_option())
    print(Option.CLEAN_AND_UPDATE_ALL.get_menu_option())
    try:
        option = Option(int(input("Choose an option: ")))
        return option
    except ValueError:
        pass


def docker_input_option() -> DockerOption:
    print(DockerOption.EXIT.get_menu_option())
    print(DockerOption.ATOMIK_CRAWLERS.get_menu_option())
    print(DockerOption.CRAWLER_WORKER.get_menu_option())
    print(DockerOption.GLOBAL_API.get_menu_option())
    print(DockerOption.PIPELINE_WORKER.get_menu_option())
    try:
        option = DockerOption(int(input("Choose an option: ")))
        return option
    except ValueError:
        pass


def docker_action_input_option() -> DockerActionOption:
    print(DockerActionOption.EXIT.get_menu_option())
    print(DockerActionOption.LOGS.get_menu_option())
    print(DockerActionOption.UP.get_menu_option())
    print(DockerActionOption.STOP.get_menu_option())
    print(DockerActionOption.REMOVE.get_menu_option())
    print(DockerActionOption.BASH.get_menu_option())
    print(DockerActionOption.CLEAN_AND_UPDATE.get_menu_option())
    try:
        option = DockerActionOption(int(input("Choose an option: ")))
        return option
    except ValueError:
        pass


def handle_main_menu(c: Console) -> Option:
    c.clear()
    c.print("DockersManager v0.0.2", style="bold cyan")
    option = input_option()
    return option


def handle_individual_actions(c: Console) -> DockerOption:
    c.clear()
    c.print("Select a container", style="bold cyan")
    docker_option = docker_input_option()
    return docker_option


def handle_container_actions(c: Console, docker_option: DockerOption):
    while True:
        c.clear()
        c.print(
            f"Selected container: {docker_option.get_name()}",
            style=docker_option.get_color(),
        )
        action_option = docker_action_input_option()
        if action_option == DockerActionOption.EXIT:
            break
        elif action_option == DockerActionOption.LOGS:
            child = logs(container_name=docker_option.get_service_name())
            child.close()
        elif action_option == DockerActionOption.UP:
            child = up(container_name=docker_option.get_name())
            child.close()
        elif action_option == DockerActionOption.STOP:
            child = stop(container_name=docker_option.get_service_name())
            child.close()
        elif action_option == DockerActionOption.REMOVE:
            child = remove(container_name=docker_option.get_service_name())
            child.close()
        elif action_option == DockerActionOption.BASH:
            child = bash(container_name=docker_option.get_service_name())
            child.close()
        elif action_option == DockerActionOption.CLEAN_AND_UPDATE:
            child = clean_and_update(docker_option.get_directory())
            child.close()
        else:
            pass


def start(c: Console):
    while True:
        option = handle_main_menu(c)
        if option == Option.EXIT:
            c.print("Exiting", style="bold green")
            break
        elif option == Option.INDIVIDUAL_ACTIONS:
            while True:
                docker_option = handle_individual_actions(c)
                if docker_option == DockerOption.EXIT:
                    break
                else:
                    handle_container_actions(c, docker_option)
        elif option == Option.LIST_CONTAINERS:
            child = list_containers()
            child.close()
        elif option == Option.RESTART_CONTAINERS:
            child = restart_containers()
            child.close()
        elif option == Option.UP_CONTAINERS:
            child = up_containers()
            child.close()
        elif option == Option.DOWN_CONTAINERS:
            child = down_containers()
            child.close()
        elif option == Option.PULL:
            child = pull()
            child.close()
        elif option == Option.CLEAN_AND_UPDATE_ALL:
            child = clean_and_update_all()
            child.close()
        else:
            pass


if __name__ == "__main__":
    console = Console()
    start(c=console)
