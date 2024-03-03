# Traverse all folders and subfolder and search for files with .mdx extension and delete all files whose file names does not end in 'en.mdx'
# This is to remove all non-english files from the folder
import os
import glob


def delete_non_english_mdx_files(directory):
    # Traverse all folders and subfolders
    for root, dirs, files in os.walk(directory):
        # Search for files with .mdx extension
        for file in glob.glob(root + "/*.mdx"):
            # Delete all files whose file names does not end in 'en.mdx'
            if not file.endswith("en.mdx"):
                os.remove(file)


def delete_non_english_meta_json_files(directory):
    # Traverse all folders and subfolders
    for root, dirs, files in os.walk(directory):
        # Search for files with .mdx extension
        for file in glob.glob(root + "/_meta.*.json"):
            # Delete all files whose file names does not end in 'en.mdx'
            if not file.endswith("_meta.en.json"):
                os.remove(file)

if __name__ == "__main__":
    delete_non_english_mdx_files(".")
    delete_non_english_meta_json_files(".")