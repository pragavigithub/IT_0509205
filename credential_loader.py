import json
import os
import logging

def load_credentials_from_json(file_path=None):
    """
    Load credentials from JSON file and optionally write to .env file.
    
    Args:
        file_path (str): Path to JSON credential file. 
                        If None, searches multiple locations.
    
    Returns:
        dict: Dictionary containing credentials
    """
    if file_path is None:
        # Search multiple locations for credential files
        search_paths = [
            "./credential.json",                    # Local directory
            "./credentials.json",                   # Local directory alternate name
            "./sap_login/credential.json",         # Local sap_login directory
            "C:/tmp/sap_login/credential.json",    # Windows path
            "/tmp/sap_login/credential.json",      # Linux path
            "C:/credential.json",                   # C:/ root
            "C:/credentials.json",                  # C:/ root alternate
            os.path.expanduser("~/credential.json"), # User home directory
            os.path.expanduser("~/credentials.json") # User home directory alternate
        ]
        
        file_path = None
        for path in search_paths:
            if os.path.exists(path):
                file_path = path
                logging.info(f"🔍 Found credential file at: {path}")
                break
        
        if file_path is None:
            logging.warning(f"⚠️ Credential file not found in any of these locations:")
            for path in search_paths:
                logging.warning(f"   - {path}")
            return {}
    
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                credentials = json.load(f)
            logging.info(f"✅ Credentials loaded from {file_path}")
            
            # Write credentials to .env file for environment variable access
            write_credentials_to_env(credentials)
            
            return credentials
        else:
            logging.warning(f"⚠️ Credential file not found at {file_path}")
            return {}
    except json.JSONDecodeError as e:
        logging.error(f"❌ Error parsing JSON credential file: {e}")
        return {}
    except Exception as e:
        logging.error(f"❌ Error loading credential file: {e}")
        return {}

def write_credentials_to_env(credentials):
    """
    Write credentials to .env file for environment variable access.
    
    Args:
        credentials (dict): Dictionary of credentials to write
    """
    try:
        env_file_path = '.env'
        
        # Read existing .env content if file exists
        existing_env = {}
        if os.path.exists(env_file_path):
            with open(env_file_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        existing_env[key] = value
        
        # Update with new credentials
        for key, value in credentials.items():
            if key and value:  # Only add non-empty keys and values
                # Special handling for DATABASE_URL in Replit environment
                if key == 'DATABASE_URL' and os.environ.get('REPL_ID'):
                    # In Replit, preserve the original PostgreSQL DATABASE_URL
                    original_db_url = os.environ.get('DATABASE_URL')
                    if original_db_url and 'postgresql' in original_db_url:
                        logging.info("🔄 Preserving PostgreSQL DATABASE_URL for Replit environment")
                        existing_env[key] = original_db_url
                        continue
                
                existing_env[key] = str(value)
        
        # Write updated .env file
        with open(env_file_path, 'w') as f:
            f.write("# Auto-generated from JSON credential file\n")
            f.write(f"# Generated on: {os.popen('date').read().strip()}\n\n")
            
            for key, value in existing_env.items():
                f.write(f"{key}={value}\n")
        
        logging.info(f"✅ Credentials written to {env_file_path}")
        
        # Update current environment variables
        for key, value in credentials.items():
            if key and value:
                os.environ[key] = str(value)
        
        logging.info(f"✅ Environment variables updated with JSON credentials")
        
    except Exception as e:
        logging.error(f"❌ Error writing credentials to .env file: {e}")

def get_credential(credentials, key, default=None):
    """
    Get a specific credential with fallback to environment variable.
    
    Args:
        credentials (dict): Loaded credentials dictionary
        key (str): Credential key to retrieve
        default: Default value if key not found
    
    Returns:
        str: Credential value
    """
    # Try to get from JSON credentials first
    if key in credentials:
        return credentials[key]
    
    # Fallback to environment variable
    env_value = os.environ.get(key, default)
    if env_value:
        logging.info(f"Using environment variable for {key}")
        return env_value
    
    logging.warning(f"⚠️ Credential '{key}' not found in JSON file or environment")
    return default