import os, shutil, subprocess, configparser, tempfile
from pathlib import Path

def clone_horsemods_folder():
    """Clone the buck folder from HorseMod repository to the horse folder locally."""
    
    # Define paths
    repo_url = "https://github.com/PZ-HorseTeam/HorseMod.git"
    source_folder = "Contents/mods/HorseMod/42/media/AnimSets/buck"
    dest_folder = "Contents/mods/HorseMod-AttachmentEditor/42/media/AnimSets/horse"
    temp_clone_dir = os.path.join(tempfile.gettempdir(), "horsemods_temp_clone")
    
    # Create destination directory structure
    dest_path = Path(dest_folder)
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Clean up any existing temporary clone
    if os.path.exists(temp_clone_dir):
        shutil.rmtree(temp_clone_dir)
    
    print(f"Cloning repository from {repo_url}...")
    try:
        # Clone the repository
        subprocess.run(
            ["git", "clone", "--depth", "1", repo_url, temp_clone_dir],
            check=True,
            capture_output=True
        )
        
        # Source path in the cloned repository
        source_path = os.path.join(temp_clone_dir, source_folder)
        
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"Source folder not found: {source_path}")
        
        # Copy the folder (preserving existing files)
        shutil.copytree(source_path, dest_folder, dirs_exist_ok=True)
        print(f"Successfully cloned {source_folder} to {dest_folder}")
        
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e}")
        raise
    except Exception as e:
        print(f"Error during setup: {e}")
        raise
    finally:
        # Clean up temporary clone
        if os.path.exists(temp_clone_dir):
            shutil.rmtree(temp_clone_dir)
            print("Cleaned up temporary files")

if __name__ == "__main__":
    # load config
    config = configparser.ConfigParser()
    config_file = "config.ini"
    config.read(config_file)
    game_media_folder = str(Path(config["PATHS"]["game_media_folder"]).expanduser())
    actiongroups_path = os.path.join(game_media_folder, "actiongroups")
    
    
    print("\033[34m 1. Cloning HorseMod AnimSets folder...\033[0m")
    clone_horsemods_folder()

    print("\033[34m 2. Copy buck vanilla ActionGroup to horse ActionGroup...\033[0m")
    # Copy the entire buck_actiongroup folder to horse_actiongroup folder
    src_folder = os.path.join(actiongroups_path, "buck")
    dst_folder = os.path.join(actiongroups_path, "horse")
    shutil.copytree(src_folder, dst_folder, dirs_exist_ok=True)

    print("\033[31m Done\033[0m")
    