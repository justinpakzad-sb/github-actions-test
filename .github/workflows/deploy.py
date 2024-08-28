import os
import tdworkflow


def get_api_keys(instance_type: str) -> str:
    """
    Retrieves the API keys for the specified instance type (dev/prod) for both EU and US regions.
    Args: instance_type (str): The instance type, either 'dev' or 'prod', used to retrieve the appropriate API keys.
    Returns: Tuple[str, str]: A tuple containing the API keys for the EU and US regions, respectively.
    """
    api_key_eu = os.environ[f"TD_API_KEY_EU_{instance_type.upper()}"]
    api_key_us = os.environ[f"TD_API_KEY_US_{instance_type.upper()}"]
    return api_key_eu, api_key_us


def get_project_paths():
    """
    Generates and returns the file paths for the project directories corresponding to the EU and US regions.
    Returns: Tuple[str, str]: A tuple containing the paths to the EU and US project directories.
    """
    project_path_eu = os.path.join(os.getcwd(), "eu")
    project_path_us = os.path.join(os.getcwd(), "us")
    return project_path_eu, project_path_us


def get_endpoints():
    """
    Gets the API endpoints for the Treasure Data console for both the EU and US regions.
    Returns: Tuple[str, str]: A tuple containing the API endpoints for the US and EU regions, respectively.
    """
    us_endpoint = "https://console-next.treasuredata.com"
    eu_endpoint = "https://console-next.eu01.treasuredata.com"
    return us_endpoint, eu_endpoint


def deploy_td_project(project_folder, api_key, endpoint):
    """
    Deploys a Treasure Data project to the specified region using the TD Workflow API client.
    Args:
        project_folder (str): The path to the project folder that needs to be deployed.
        api_key (str): The API key to authenticate the deployment process.
        endpoint (str): The API endpoint for the region where the project is being deployed.
    Returns: None
    """
    client = tdworkflow.client.Client(api_key=api_key, endpoint=endpoint)
    os.chdir(project_folder)
    client.create_project(project_folder, ".")


def main():
    instance_type = os.environ.get("INSTANCE", "DEV")
    api_key_eu, api_key_us = get_api_keys(instance_type)
    project_path_eu, project_path_us = get_project_paths()
    eu_endpoint, us_endpoint = get_endpoints()
    deploy_td_project(
        project_folder=project_path_eu, api_key=api_key_eu, endpoint=eu_endpoint
    )
    deploy_td_project(
        project_folder=project_path_us, api_key=api_key_us, endpoint=us_endpoint
    )


if __name__ == "__main__":
    main()
