import requests
import base64
import time
import json

class YacineTV:
    """
    YacineTV API client for making requests and decrypting responses.
    """
    api_url = "https://deft.yacinelive.com/"
    key = "c!xZj+N9&G@Ev@vw"

    def decrypt(self, enc, key):
        """
        Decrypt the encoded response from the API.
        
        Args:
            enc (str): Encoded response
            key (str): Decryption key
            
        Returns:
            str: Decrypted data
        """
        enc = base64.b64decode(enc.encode("ascii")).decode("ascii")
        return ''.join(chr(ord(enc[i]) ^ ord(key[i % len(key)])) for i in range(len(enc)))

    def req(self, path):
        """
        Make a request to the YacineTV API and decrypt the response.
        
        Args:
            path (str): API endpoint path
            
        Returns:
            str: Decrypted response data
        """
        try:
            r = requests.get(self.api_url + path)
            r.raise_for_status()
            
            timestamp = r.headers.get("t", str(int(time.time())))
            decrypted_data = self.decrypt(r.text, key=self.key + timestamp)
            return decrypted_data
        except requests.RequestException as e:
            return f"Request error: {str(e)}"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def get_categories(self):
        """Get all categories from the API"""
        return self.req("api/categories")
    
    def get_channels_by_category(self, category_id):
        """Get channels for a specific category"""
        return self.req(f"api/categories/{category_id}/channels")
    
    def get_channel_data(self, channel_id):
        """Get data for a specific channel"""
        return self.req(f"api/channel/{channel_id}") 