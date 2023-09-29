import os
import openai
from senha import API_KEY

openai.organization = "org-8DPM9ymLIZQplOD6M1LpXiXa"
openai.api_key = f"{API_KEY}"
openai.Model.list()