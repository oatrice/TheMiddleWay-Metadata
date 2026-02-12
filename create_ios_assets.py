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

def create_imageset(source_path, asset_name):
    imageset_dir = os.path.join(TARGET_DIR, f"{asset_name}.imageset")
    os.makedirs(imageset_dir, exist_ok=True)

    # Copy file (using 3x for simplicity as High Res, or 2x, or Universal)
    # We'll treat it as universal 1x, 2x, 3x generic or just a single scale
    target_file = "image.png"
    shutil.copy(source_path, os.path.join(imageset_dir, target_file))

    # Create Contents.json
    contents = {
        "images": [
            {
                "filename": target_file,
                "idiom": "universal",
                "scale": "1x" # Assuming the generated images are large enough to be 1x base or specific scale. 
                              # For simplicity in this script we just map it to 1x. 
                              # Ideally we should resize or just specify it as 3x if it's high res.
            },
             {
                "idiom": "universal",
                "scale": "2x"
            },
             {
                "idiom": "universal",
                "scale": "3x"
            }
        ],
        "info": {
            "author": "xcode",
            "version": 1
        }
    }
    
    # Update to just use one slot for simplicity and let iOS scale if needed, or fill all slots with same image (wasteful but works for mock)
    # Let's just put it in 1x slot.
    
    with open(os.path.join(imageset_dir, "Contents.json"), "w") as f:
        json.dump(contents, f, indent=2)

    print(f"Created {asset_name}.imageset")

def main():
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
