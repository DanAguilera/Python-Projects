import subprocess

result = subprocess.run(
    ["ping", "-n", "2", "google.com"],
    capture_output=True,
    text=True
)
print(result)