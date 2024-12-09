
# AWS Instance Metadata Retrieval Tool

This tool retrieves metadata of an AWS EC2 instance in JSON format. It provides options to:
- Retrieve all metadata available for the instance.
- Retrieve a specific metadata key.

## Features
- Queries AWS EC2 instance metadata from `http://169.254.169.254/latest/meta-data/`.
- Outputs data in JSON format.
- Includes error handling for failed requests.
- Allows fetching a specific key for bonus points.

## Prerequisites
- Python 3.x installed.
- `requests` library installed.

You can install the `requests` library using:
```bash
pip install requests
```

## How to Use
1. Clone this repository or download the script.
2. Run the script on an AWS EC2 instance. Metadata is only accessible from within the instance.

### Running the Script
1. Open a terminal.
2. Navigate to the directory containing the script.
3. Execute the script:
```bash
python metadata_tool.py
```
4. Follow the interactive prompts:
   - Enter `1` to retrieve all metadata.
   - Enter `2` to retrieve a specific metadata key.

### Example Output
#### Retrieve All Metadata
```json
{
    "ami-id": "ami-0abcdef1234567890",
    "instance-id": "i-0abcdef1234567890",
    "hostname": "ip-172-31-22-33.ec2.internal"
}
```
#### Retrieve Specific Key
```json
{
    "ami-id": "ami-0abcdef1234567890"
}
```

## Notes
- This script should be run **inside an AWS EC2 instance** to access the metadata service.
- The metadata service URL (`http://169.254.169.254`) is accessible only from EC2 instances.

---

Developed by Nagaraj
