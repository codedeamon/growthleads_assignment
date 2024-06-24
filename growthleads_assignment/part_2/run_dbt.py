import os
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        raise Exception(f"Command failed with return code {result.returncode}: {command}")

def main():
    # Navigate to dbt project directory
    os.chdir('dbt_tr')

    # Run dbt seed
    run_command('dbt seed')

    # Run dbt models
    run_command('dbt run')

if __name__ == "__main__":
    main()
