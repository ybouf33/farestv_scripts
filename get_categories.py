import json
import sys
from datetime import datetime
from utils.yacine_tv import YacineTV

def main():
    # Set output filename
    output_file = f"ytv_categories_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    if len(sys.argv) > 1:
        output_file = sys.argv[1]
    
    # Initialize API client
    yacine_tv = YacineTV()
    
    # Get categories
    print("Fetching categories...")
    categories_response = yacine_tv.get_categories()
    
    try:
        # Try to parse the JSON response
        categories_data = json.loads(categories_response)
        
        # Save to file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(categories_data, f, indent=2, ensure_ascii=False)
        
        print(f"Categories saved to {output_file}")
        print(f"Found {len(categories_data)} categories")
        
    except json.JSONDecodeError:
        print("Error: Could not parse API response as JSON")
        print("Response:", categories_response)
    except Exception as e:
        print(f"Error: {str(e)}")
        print("Response:", categories_response)

if __name__ == "__main__":
    main() 