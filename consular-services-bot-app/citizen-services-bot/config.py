#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import os
import openai
class DefaultConfig:
    """ Bot Configuration """
    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "xxxxxxxxxxxxxxxxx")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "xxxxxxxxxxxxxxx")
    ai_search_url = "https://xxxxxxxxxxxxxxxxx.search.windows.net"
    ai_search_key = "xxxxxxxxxxxxxxxxxxxxx"
    ai_index_name = "mea-docs-repo-0101"
    ai_semantic_config = "mea-docs-repo-0101-semantic-configuration"
    az_openai_key = "xxxxxxxxxxxxxx"
    az_openai_baseurl = "https://xxxxxxxxxxxxxx5.openai.azure.com/"
    az_openai_type = "azure"
    az_openai_version_latest = "2023-08-01-preview"
    az_openai_version = "2023-07-01-preview"
    # deployment_name = "turbo0613"  # T
    deployment_name = "gpt-4"  # T

    attlassian_api_key = 'xxxxxxxxxxxxxx'
    attlassian_user_name = 'xxxxxxxxxxxx'
    attlassian_url = 'https://xxxxxxxxxx.atlassian.net/'
    grievance_project_key = 'CON'
    grievance_type = 'Task'
    grievance_project_name = 'consular_services'
