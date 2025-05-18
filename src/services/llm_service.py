import subprocess
from src.core.config import settings  # Make sure your settings are imported

def query_phi3(prompt: str) -> str:
    """
    Queries the phi3 model using the Ollama CLI.
    Make sure `ollama` is installed and accessible in PATH.
    """
    try:
        print(f"Prompting phi3 via Ollama: {prompt}")  # Debug

        result = subprocess.run(
            ["ollama", "run", settings.LLM_MODEL],  # Uses the model from config (e.g., "phi3")
            input=prompt.encode('utf-8'),
            capture_output=True,
            check=True
        )

        output = result.stdout.decode('utf-8').strip()
        print(f"OLLAMA Output: {output}")  # Debug
        return output

    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.decode('utf-8') if e.stderr else "Unknown error"
        print(f"OLLAMA Process Error: {error_msg}")
        return f"Error running {settings.LLM_MODEL} model: {error_msg}"

    except FileNotFoundError:
        error_msg = "Error: 'ollama' command not found. Please ensure it is installed and added to PATH."
        print(error_msg)
        return error_msg

    except Exception as e:
        error_msg = f"Unexpected error: {str(e)}"
        print(error_msg)
        return error_msg
