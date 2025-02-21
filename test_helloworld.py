import subprocess

def test_helloworld():
    result = subprocess.run(["python3", "helloworld.py"], capture_output=True, text=True)
    assert result.returncode == 0, f"Error: {result.stderr}"
