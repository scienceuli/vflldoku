import os
import re

ATTACHMENTS_FOLDER = "attachments"

def on_page_markdown(markdown, page, config, files):
    def replacer(match):
        img_alt, size, img_path = match.groups()

        # Ensure the path is correctly prefixed with "attachments/"
        if not img_path.startswith(ATTACHMENTS_FOLDER + "/"):
            img_path = os.path.join(ATTACHMENTS_FOLDER, img_path)

        return f'<img src="/{img_path}" width="{size}px">'

    # Convert Obsidian-style image syntax with size parameter to HTML
    return re.sub(r"!\[(.*?)\|(\d+)]\((.*?)\)", replacer, markdown)