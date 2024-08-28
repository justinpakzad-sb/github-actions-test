import os
import tdworkflow


def deploy_td_project(instance_type, project_folder,api_key):
    endpoint = os.environ[f"SYSTEM_TD_WORKFLOW_ENDPOINT_{region.upper()}"]
    api_key = os.environ[f"TD_API_KEY_{region.upper()}"]
    client = tdworkflow.client.Client(api_key=api_key, endpoint=endpoint)
    os.chdir(project_folder)
    client.create_project(region, ".")


if __name__ == "__main__":
    instance_type = os.environ.get("INSTANCE", "DEV")
    api_key_eu = os.environ[f"TD_API_KEY_EU_{instance_type.upper()}"]
    api_key_us = os.environ[f"TD_API_KEY_US_{instance_type.upper()}"]
    project_path_eu = os.path.join(os.getcwd(), "eu")
    project_path_us = os.path.join(os.getcwd(), "us")
    deploy_td_project(project_path_eu,endpoint_eu,api_key_eu)
    deploy_td_project(project_path_us,endpoint_us,api_key_us)
    # deploy_td_project(region, project_path)
