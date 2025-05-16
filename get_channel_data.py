import json
import sys
from datetime import datetime
from utils.yacine_tv import YacineTV

def main():
    # Default channel ID (from the original script)
    channel_id = 4
    
    # Check if channel ID was provided as command line argument
    if len(sys.argv) > 1:
        try:
            channel_id = int(sys.argv[1])
        except ValueError:
            print(f"Error: Invalid channel ID '{sys.argv[1]}'. Using default: {channel_id}")
    
    # Set output filename
    output_file = f"ytv_channel_{channel_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    
    # Initialize API client
    yacine_tv = YacineTV()
    
    # Get channel data
    print(f"Fetching data for channel ID {channel_id}...")
    response = yacine_tv.get_channel_data(channel_id)
    
    try:
        # Try to parse the JSON response
        data = json.loads(response)
        
        # Save to file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"Channel data saved to {output_file}")
        
        # Display basic info about the channel if available
        if isinstance(data, dict) and 'name' in data:
            print(f"Channel: {data['name']}")
        
    except json.JSONDecodeError:
        print("Error: Could not parse API response as JSON")
        print("Response:", response)
    except Exception as e:
        print(f"Error: {str(e)}")
        print("Response:", response)

if __name__ == "__main__":
    main() 