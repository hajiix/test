from datetime import datetime

# Path to your README.md file
readme_path = "README.md"

# Get current date in your preferred format
current_date = datetime.now().strftime("%Y-%m-%d")

# Read the README file
with open(readme_path, "r") as file:
    content = file.readlines()

# Modify the line with the date (Assume the date is on a specific line or look for a specific placeholder)
for i, line in enumerate(content):
    if line.startswith("Last updated:"):
        content[i] = f"Last updated: {current_date}\n"
        break
else:
    # If no line starts with "Last updated:", add it at the end
    content.append(f"\nLast updated: {current_date}\n")

# Write back the updated content to README.md
with open(readme_path, "w") as file:
    file.writelines(content)
