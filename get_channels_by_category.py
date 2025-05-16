import json
import sys
from datetime import datetime
from utils.yacine_tv import YacineTV

def main():
    # Default category ID (9 from the original script)
    category_id = 86
    
    # Check if category ID was provided as command line argument
    if len(sys.argv) > 1:
        try:
            category_id = int(sys.argv[1])
        except ValueError:
            print(f"Error: Invalid category ID '{sys.argv[1]}'. Using default: {category_id}")
    
    # Set output filename
    output_file = f"ytv_channels_cat{category_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    
    # Initialize API client
    yacine_tv = YacineTV()
    
    # Get channels for the category
    print(f"Fetching channels for category ID {category_id}...")
    response = yacine_tv.get_channels_by_category(category_id)
    
    try:
        # Try to parse the JSON response
        data = json.loads(response)
        
        # Save to file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"Channel data saved to {output_file}")
        
        # Display summary info if data is available
        if isinstance(data, list):
            print(f"Found {len(data)} channels")
        elif isinstance(data, dict) and 'channels' in data:
            print(f"Found {len(data['channels'])} channels")
        
    except json.JSONDecodeError:
        print("Error: Could not parse API response as JSON")
        print("Response:", response)
    except Exception as e:
        print(f"Error: {str(e)}")
        print("Response:", response)

if __name__ == "__main__":
    main() 