import requests
import json

def get_metadata(base_url="http://169.254.169.254/latest/meta-data/", key=None):
    """
    Retrieve instance metadata from AWS.

    :param base_url: Base URL for AWS metadata
    :param key: Specific key to retrieve
    :return: Metadata in JSON format
    """
    try:
        if key:
            # Retrieve a specific key
            response = requests.get(base_url + key, timeout=5)
            if response.status_code == 200:
                return json.dumps({key: response.text}, indent=4)
            else:
                return json.dumps({"error": f"Failed to retrieve key '{key}'. Status code: {response.status_code}"}, indent=4)
        else:
            # Retrieve all metadata
            response = requests.get(base_url, timeout=5)
            if response.status_code == 200:
                metadata_keys = response.text.splitlines()
                metadata = {}
                for k in metadata_keys:
                    sub_response = requests.get(base_url + k, timeout=5)
                    metadata[k] = sub_response.text if sub_response.status_code == 200 else "N/A"
                return json.dumps(metadata, indent=4)
            else:
                return json.dumps({"error": f"Failed to retrieve metadata. Status code: {response.status_code}"}, indent=4)
    except requests.exceptions.RequestException as e:
        return json.dumps({"error": str(e)}, indent=4)

if __name__ == "__main__":
    print("AWS Metadata Retrieval Tool")
    print("1. Retrieve all metadata")
    print("2. Retrieve a specific metadata key")
    choice = input("Enter your choice (1/2): ").strip()

    if choice == "1":
        print("\nFetching all metadata...")
        print(get_metadata())
    elif choice == "2":
        key = input("Enter the metadata key to retrieve: ").strip()
        print(f"\nFetching metadata for key: {key}")
        print(get_metadata(key=key))
    else:
        print("Invalid choice. Exiting.")
