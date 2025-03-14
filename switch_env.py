import os
from pathlib import Path

# Define the workspace directory (relative to script location)
WORKSPACE_DIR = Path(__file__).parent  # Goes up to /home/thuan/workspace/grapple

# Available environment options
ENV_OPTIONS = {
    "1": ".env.dev",
    "2": ".env.uat",
    "3": ".env.dev2"
}

# Specific paths to apply the environment switch (relative to WORKSPACE_DIR)
TARGET_PATHS = [
    "grapple-plus-api",               # Adjust if name differs
    "grapple-plus-app",
    "grapple-website/apps/grapple-web"
]

def replace_env_content(source_env_path, target_env_path):
    """Clear target .env and replace with contents of source .env."""
    if not source_env_path.exists():
        print(f"Source file {source_env_path} does not exist. Skipping.")
        return
    
    # Read source .env content
    with open(source_env_path, 'r') as source_file:
        source_content = source_file.read()
    
    # Write (replace) to target .env
    with open(target_env_path, 'w') as target_file:
        target_file.write(source_content)
    #print(f"{target_env_path} → {source_env_path}\n")

def switch_environment():
    """Prompt user to select an environment and update specified paths."""
    print("Select an environment to switch to:")
    for key, value in ENV_OPTIONS.items():
        print(f"{key}: {value}")
    
    choice = input("Enter your choice (1-3): ").strip()
    
    if choice not in ENV_OPTIONS:
        print("Invalid choice. Exiting.")
        return
    
    selected_env = ENV_OPTIONS[choice]
    
    print(f"Switching to {selected_env} for .env files...\n")
    for relative_path in TARGET_PATHS:
        repo_path = WORKSPACE_DIR / relative_path
        if not repo_path.exists():
            print(f"Path {repo_path} does not exist. Skipping.")
            continue
        
        source_env_path = repo_path / selected_env  # Source file in the repo
        target_env_path = repo_path / ".env"        # Target .env in the repo
        
        replace_env_content(source_env_path, target_env_path)
        print(f"Process {relative_path} completed ✅")
    
    print("\n Environment switch complete!")

if __name__ == "__main__":
    switch_environment()
