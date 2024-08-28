import os
import tdworkflow


def get_api_keys(instance_type: str) -> str:
    """Returns corresponding API keys depending on instance type (dev/prod)"""
    api_key_eu = os.environ[f"TD_API_KEY_EU_{instance_type.upper()}"]
    api_key_us = os.environ[f"TD_API_KEY_US_{instance_type.upper()}"]
    return api_key_eu, api_key_us


def get_project_paths():
    """Returns project paths for eu/us regions"""
    project_path_eu = os.path.join(os.getcwd(), "eu")
    project_path_us = os.path.join(os.getcwd(), "us")
    return project_path_eu, project_path_us


def get_endpoints():
    """Returns endpoints for eu/us regions"""
    us_endpoint = "https://console-next.treasuredata.com"
    eu_endpoint = "https://console-next.eu01.treasuredata.com"
    return us_endpoint, eu_endpoint


def deploy_td_project(project_folder, api_key, endpoint):
    """Deploys projects to TD via workflow API client"""
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
