import pexpect


def connect_to_ssh():
    """
    Establishes an SSH connection to the 'dev' server using pexpect.
    Returns:
        pexpect.spawn: The pexpect child object representing the SSH session.
    """
    child = pexpect.spawn(command="ssh dev")
    child.logfile_read = open(file="ssh.log", mode="wb")
    child.expect(pattern=r"passphrase")
    child.sendline(s="201202")
    child.expect(pattern=r"\$")
    return child


def list_containers():
    """
    Lists all Docker containers on the 'dev' server.
    """
    child = connect_to_ssh()
    child.sendline(s="docker ps -a")
    child.interact()
    return child


def restart_containers():
    """
    Restarts all Docker containers on the 'dev' server.

    This function navigates to the 'git/risk3-dev' directory, brings down any running Docker containers,
    and then brings them up in detached mode.
    """
    child = connect_to_ssh()
    child.sendline(s="cd git/risk3-dev")
    child.expect(pattern=r"\$")
    child.sendline(s="docker compose -p sb down")
    child.expect(pattern=r"\$")
    child.sendline(s="docker compose -p sb up -d")
    child.interact()
    return child


def up_containers():
    """
    Starts all Docker containers on the 'dev' server.

    This function navigates to the 'git/risk3-dev' directory, brings up all Docker containers in detached mode.
    """
    child = connect_to_ssh()
    child.sendline(s="cd git/risk3-dev")
    child.expect(pattern=r"\$")
    child.sendline(s="docker compose -p sb up -d")
    child.interact()
    return child


def down_containers():
    """
    Stops all Docker containers on the 'dev' server.

    This function navigates to the 'git/risk3-dev' directory, brings down all running Docker containers.
    """
    child = connect_to_ssh()
    child.sendline(s="cd git/risk3-dev")
    child.expect(pattern=r"\$")
    child.sendline(s="docker compose -p sb down")
    child.interact()
    return child


def pull():
    """
    Pulls the latest Docker images for all services on the 'dev' server.

    This function navigates to the 'git/risk3-dev' directory and pulls the latest Docker images for all services.
    """
    child = connect_to_ssh()
    child.sendline(s="cd git/risk3-dev")
    child.expect(pattern=r"\$")
    child.sendline(s="docker compose pull")
    child.interact()
    return child


def logs(container_name: str):
    """
    Fetches and streams the logs of a specified Docker container on the 'dev' server.
    Args:
        container_name (str): The name of the Docker container whose logs are to be fetched.
    """
    child = connect_to_ssh()
    child.sendline(s=f"docker logs -f {container_name}")
    child.interact()
    return child


def up(container_name: str):
    """
    Starts a specified Docker container on the 'dev' server.
    Args:
        container_name (str): The name of the Docker container to be started.
    """
    child = connect_to_ssh()
    child.sendline(s="cd git/risk3-dev")
    child.expect(pattern=r"\$")
    child.sendline(s=f"docker compose -p sb up -d {container_name}")
    child.interact()
    return child


def stop(container_name: str):
    """
    Stops a specified Docker container on the 'dev' server.
    Args:
        container_name (str): The name of the Docker container to be stopped.
    """
    child = connect_to_ssh()
    child.sendline(s=f"docker stop {container_name}")
    child.interact()
    return child


def remove(container_name: str):
    """
    Removes a specified Docker container on the 'dev' server.
    Args:
        container_name (str): The name of the Docker container to be removed.
    """
    child = connect_to_ssh()
    child.sendline(s=f"docker rm {container_name}")
    child.interact()
    return child


def bash(container_name: str):
    """
    Opens a bash shell inside a specified Docker container on the 'dev' server.
    Args:
        container_name (str): The name of the Docker container to open a bash shell in.
    """
    child = connect_to_ssh()
    child.sendline(s=f"docker exec -it {container_name} bash")
    child.interact()
    return child


def clean_and_update(directory_name: str):
    """
    Cleans a specified directory on the 'dev' server.
    Args:
        directory_name (str): The name of the directory to be cleaned.
    """
    child = connect_to_ssh()
    child.sendline(s=f"cd {directory_name}")
    child.expect(pattern=r"\$")
    child.sendline(s="git clean -df")
    child.expect(pattern=r"\$")
    child.sendline(s="git restore .")
    child.expect(pattern=r"\$")
    child.sendline(s="git checkout develop")
    child.expect(pattern=r"(Already|Switched)")
    child.sendline(s="git pull")
    child.expect(pattern=r"passphrase")
    child.sendline(s="felipe123")
    child.interact()
    return child
