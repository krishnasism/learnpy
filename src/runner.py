import logging
import subprocess


class Runner:
    """Runner runs a python scripts and parses the output."""

    def __init__(self, script_path: str):
        self.script_path = script_path
        self.stdout: bytes
        self.stderr: bytes

    def run(self):
        """Run the script and return the output."""
        result = subprocess.run(["python", self.script_path], capture_output=True)
        self.stdout = result.stdout
        self.stderr = result.stderr

    def got_err(self) -> bool:
        """Check if there is an error."""
        decoded = self.stderr.decode("utf-8")
        logging.debug(decoded)
        return len(decoded) > 0

    def get_stdout(self) -> str:
        """Return the stdout."""
        return self.stdout.decode("utf-8")
