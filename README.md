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

## API Access via GitHub Pages

This project provides API-like access to YacineTV data through GitHub Pages. After setting up, you can access the data via the following URLs:

### Endpoints

1. **Categories**
   - URL: `https://[username].github.io/[repo-name]/api/categories/`
   - Returns all available categories

2. **Channel Data**
   - URL: `https://[username].github.io/[repo-name]/api/channel/[channel_id]/`
   - Returns data for a specific channel
   - Example: `https://[username].github.io/[repo-name]/api/channel/4/`

3. **Category Channels**
   - URL: `https://[username].github.io/[repo-name]/api/category/[category_id]/`
   - Returns all channels in a specific category
   - Example: `https://[username].github.io/[repo-name]/api/category/86/`

### Setup Instructions

1. Enable GitHub Pages in your repository settings:
   - Go to Settings > Pages
   - Set Source to "GitHub Actions"

2. Run the "Setup GitHub Pages" workflow:
   - Go to Actions tab
   - Select "Setup GitHub Pages"
   - Click "Run workflow"

3. To update data, trigger the appropriate workflow:
   - Through the GitHub UI (Actions tab)
   - Via the GitHub API (see below)

### Triggering Updates via API

You can trigger data updates using the GitHub repository_dispatch API:

```bash
# Update categories
curl -X POST \
  https://api.github.com/repos/[username]/[repo-name]/dispatches \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  -d '{"event_type": "fetch-categories"}'

# Update channel data (with channel_id parameter)
curl -X POST \
  https://api.github.com/repos/[username]/[repo-name]/dispatches \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  -d '{"event_type": "fetch-channel", "client_payload": {"channel_id": "4"}}'

# Update category channels (with category_id parameter)
curl -X POST \
  https://api.github.com/repos/[username]/[repo-name]/dispatches \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  -d '{"event_type": "fetch-category-channels", "client_payload": {"category_id": "86"}}'
```

To create a personal access token, go to GitHub Settings > Developer settings > Personal access tokens. 