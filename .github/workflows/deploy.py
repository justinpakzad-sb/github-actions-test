import os
import tdworkflow


def deploy_td_project(region, project_folder):
    endpoint = os.environ[f"SYSTEM_TD_WORKFLOW_ENDPOINT_{region.upper()}"]
    api_key = os.environ[f"TD_API_KEY_{region.upper()}"]
    client = tdworkflow.client.Client(api_key=api_key, endpoint=endpoint)
    os.chdir(project_folder)
    client.create_project(region, ".")


if __name__ == "__main__":
    region = os.environ.get("REGION", "EU")
    project_path = os.path.join(os.getcwd(), region.lower())
    deploy_td_project(region, project_path)
