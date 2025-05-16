# YacineTV API Scripts

This project contains scripts for interacting with the YacineTV API.

## Project Structure

- `utils/`: Contains utility modules
  - `yacine_tv.py`: Main API client class for interacting with YacineTV
- `scripts/`: Contains executable scripts
  - `get_categories.py`: Fetch and save all available categories
  - `get_channels_by_category.py`: Fetch and save channels for a specific category
  - `get_channel_data.py`: Fetch and save data for a specific channel

## Usage

### Get All Categories

```
python scripts/get_categories.py [output_file.json]
```

### Get Channels by Category ID

```
python scripts/get_channels_by_category.py [category_id] [output_file.json]
```

Default category ID is 9 if not specified.

### Get Channel Data by ID

```
python scripts/get_channel_data.py [channel_id] [output_file.json]
```

Default channel ID is 1575 if not specified.

## Output

All scripts save their output as JSON files with timestamps in the filename (unless a specific output file is provided).

## GitHub Actions Workflows

This project includes several GitHub Actions workflows for automated data fetching:

### 1. Fetch Categories
- **Workflow file**: `.github/workflows/fetch_categories.yml`
- **Schedule**: Runs daily at midnight UTC
- **Manual trigger**: Available through workflow_dispatch
- **Output**: Saves categories to a JSON file and uploads as an artifact

### 2. Fetch Channel Data
- **Workflow file**: `.github/workflows/fetch_channel_data.yml`
- **Schedule**: Runs daily at 2 AM UTC
- **Manual trigger**: Available with configurable channel_id
- **Default channel**: ID 4
- **Output**: Saves channel data to a JSON file and uploads as an artifact

### 3. Fetch Channels by Category
- **Workflow file**: `.github/workflows/fetch_channels_by_category.yml`
- **Schedule**: Runs daily at 4 AM UTC
- **Manual trigger**: Available with configurable category_id
- **Default category**: ID 86
- **Output**: Saves category channels to a JSON file and uploads as an artifact

### 4. Fetch All Data
- **Workflow file**: `.github/workflows/fetch_all_data.yml`
- **Schedule**: Runs weekly on Sundays at 6 AM UTC
- **Manual trigger**: Available with configurable channel_id and category_id
- **Output**: Saves all data to JSON files and uploads as a combined artifact

## Running Workflows Manually

1. Go to the "Actions" tab in your GitHub repository
2. Select the desired workflow
3. Click "Run workflow"
4. Optionally configure input parameters
5. Click "Run workflow" to start the execution 