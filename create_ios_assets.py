import os
import shutil
import json

# Configuration
SOURCE_DIR = "/Users/oatrice/.gemini/antigravity/brain/c183d02e-5e38-4deb-8507-6431ec20a2f5"
TARGET_DIR = "Platforms/iOS/TheMiddleWay/Resources/Assets.xcassets"

# Map source filename to asset name
ASSETS = {
    "onboarding_welcome_logo_1770896268486.png": "onboarding_welcome",
    "onboarding_authentic_wisdom_1770896292368.png": "onboarding_wisdom",
    "onboarding_discover_path_1770896310277.png": "onboarding_path",
    "onboarding_daily_practice_1770896329650.png": "onboarding_practice"
}

def create_imageset(source_path: str, asset_name: str) -> None:
    imageset_dir = os.path.join(TARGET_DIR, f"{asset_name}.imageset")
    os.makedirs(imageset_dir, exist_ok=True)

    # Copy file (using 3x for simplicity as High Res, or 2x, or Universal)
    target_file = "image.png"
    shutil.copy(source_path, os.path.join(imageset_dir, target_file))

    # Create Contents.json
    contents = {
        "images": [
            {
                "filename": target_file,
                "idiom": "universal",
                "scale": "1x"
            },
            {
                "filename": target_file,
                "idiom": "universal",
                "scale": "2x"
            },
            {
                "filename": target_file,
                "idiom": "universal",
                "scale": "3x"
            }
        ],
        "info": {
            "author": "xcode",
            "version": 1
        }
    }
    
    with open(os.path.join(imageset_dir, "Contents.json"), "w") as f:
        json.dump(contents, f, indent=2)

    print(f"Created {asset_name}.imageset")

def main() -> None:
    if not os.path.exists(TARGET_DIR):
        print(f"Target directory {TARGET_DIR} does not exist.")
        return

    for src_file, asset_name in ASSETS.items():
        src_path = os.path.join(SOURCE_DIR, src_file)
        if os.path.exists(src_path):
            create_imageset(src_path, asset_name)
        else:
            print(f"Source file not found: {src_path}")

if __name__ == "__main__":
    main()
