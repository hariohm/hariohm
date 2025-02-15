import re

# Read URLs from input file
with open("urls.txt", "r") as file:
    urls = file.readlines()

cleaned_urls = []

for url in urls:
    url = url.strip()
    url = re.sub(r'^https://', '', url)  # Remove https://
    url = re.sub(r'([a-zA-Z0-9.-]+\.(com|net|edu|org|io|gov|in|co)).*', r'\1', url)  # Keep only domain
    if re.match(r'^[a-zA-Z0-9.-]+\.(com|net|edu|org|io|gov|in|co)$', url):  # Ensure it's a valid domain
        cleaned_urls.append(url)

# Save the cleaned URLs to a new file
with open("cleaned_urls.txt", "w") as output_file:
    output_file.write("\n".join(cleaned_urls))
