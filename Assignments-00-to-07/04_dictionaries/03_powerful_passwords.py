import hashlib

def hash_password(password):
    """Returns the SHA-256 hash of the password"""
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    """
    Checks if the provided password matches the stored hash for the email
    
    Args:
        email: User's email address
        password_to_check: Password to verify
        stored_logins: Dictionary of {email: password_hash}
        
    Returns:
        bool: True if password matches, False otherwise
    """
    # Check if email exists in stored_logins
    if email not in stored_logins:
        return False
    
    # Hash the provided password and compare with stored hash
    hashed_password = hash_password(password_to_check)
    return stored_logins[email] == hashed_password

# Example usage
if __name__ == "__main__":
    # Sample database of stored login hashes
    stored_logins = {
        "user1@example.com": hash_password("hello123"),
        "user2@example.com": hash_password("secure!456")
    }
    
    # Test cases
    print(login("user1@example.com", "hello123", stored_logins))  # True
    print(login("user1@example.com", "wrongpass", stored_logins))  # False
    print(login("unknown@example.com", "hello123", stored_logins))  # False