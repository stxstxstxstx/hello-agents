# 测试天气 API
import requests
response = requests.get("https://wttr.in/Beijing?format=j1")
print("天气API状态:", response.status_code)

# 加载环境变量
from dotenv import load_dotenv
import os
load_dotenv()

# 测试 Tavily API
from tavily import TavilyClient
tavily_api_key = os.getenv("TAVILY_API_KEY")
if not tavily_api_key:
    print("错误: 未找到 TAVILY_API_KEY 环境变量")
else:
    tavily = TavilyClient(api_key=tavily_api_key)
    try:
        result = tavily.search("test", search_depth="basic")
        print("Tavily API 连接成功")
    except Exception as e:
        print("Tavily API 错误:", e)

# 测试 LLM API - AIHubmix
# from openai import OpenAI
# client = OpenAI(
#     api_key=os.getenv("OPENAI_API_KEY"),
#     base_url=os.getenv("OPENAI_BASE_URL", "https://aihubmix.com/v1")
# )
# try:
#     response = client.chat.completions.create(
#         model=os.getenv("MODEL_NAME", "coding-glm-4.7-free"),
#         messages=[{"role": "user", "content": "Hello"}],
#         max_tokens=10
#     )
#     print("LLM API 连接成功:", response.choices[0].message.content)
# except Exception as e:
#     print("LLM API 错误:", e)

# 测试 LLM API - ModelScope（如果您使用的是 ModelScope，请取消注释并替换配置）
from openai import OpenAI
api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL", "https://api-inference.modelscope.cn/v1/")
model_name = os.getenv("MODEL_NAME", "inclusionAI/Ring-2.6-1T")

if not api_key:
    print("错误: 未找到 OPENAI_API_KEY 环境变量")
else:
    client = OpenAI(
        api_key=api_key,
        base_url=base_url
    )
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=10
        )
        print("LLM API 连接成功:", response.choices[0].message.content)
    except Exception as e:
        print("LLM API 错误:", e)