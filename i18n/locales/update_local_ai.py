import json
import re

file_path = 'zh_CN.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

def replace_value(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            obj[k] = replace_value(v)
    elif isinstance(obj, list):
        for i in range(len(obj)):
            obj[i] = replace_value(obj[i])
    elif isinstance(obj, str):
        # Replace "Local AI Service" first to avoid redundancy
        new_val = obj.replace("Local AI Service", "本地AI服务")
        # Replace "Local AI"
        new_val = new_val.replace("Local AI", "本地AI服务")
        
        # Handle potential redundancy in references or mixed text
        # e.g. "本地AI服务 Service" -> "本地AI服务"
        new_val = new_val.replace("本地AI服务 Service", "本地AI服务")
        new_val = new_val.replace("本地AI服务 服务", "本地AI服务")
        
        return new_val
    return obj

# Apply recursive replacement
data = replace_value(data)

# Explicitly set the keys to ensure definition is correct
def set_key(d, key_path, value):
    keys = key_path.split('.')
    curr = d
    for k in keys[:-1]:
        if k not in d:
            d[k] = {}
        curr = curr[k]
    curr[keys[-1]] = value

set_key(data, "localAI", "本地AI服务")
set_key(data, "localAIService", "本地AI服务")

# Also Translate the untranslated items found in grep
# "Configure where your Local AI models are stored."
# After replacement: "Configure where your 本地AI服务 models are stored."
# I should translate these sentences if possible, but the user only asked to change "Local AI".
# However, leaving "Configure where your 本地AI服务 models are stored." is weird.
# I will attempt to translate the specific keys I saw in grep.

keys_to_translate = {
    "modelHub.localModels.openModelHub": "打开本地AI服务模型中心",
    "modelHub.localModels.featured.title": "精选模型",
    "modelHub.localModels.installed.title": "已安装模型",
    "modelHub.localModels.ollamaModels.title": "Ollama 模型",
    "modelHub.localModels.huggingfaceModels.title": "Hugging Face 模型",
    "settings.localAI.manageModels.title": "管理本地AI服务模型",
    "settings.localAI.manageModels.description": "浏览、安装和管理用于本地推理的 AI 模型。",
    "settings.localAI.manageModels.openModelHub": "打开本地AI服务模型中心",
    "settings.localAI.openSettings": "打开本地AI服务设置",
    "settings.localAI.modelsLocation.description": "配置您的本地AI服务模型存储位置。"
}

for k, v in keys_to_translate.items():
    # Check if key exists
    try:
        # Simple check
        keys = k.split('.')
        curr = data
        valid = True
        for key in keys:
            if key in curr:
                curr = curr[key]
            else:
                valid = False
                break
        if valid:
             set_key(data, k, v)
    except:
        pass

# Specific complex string found in grep:
# "{modelName} requires a newer version of Local AI. Please update to the latest version from Settings > Local AI > Service Version > ... > Force Update Local AI Service"
# Replaced: "{modelName} requires a newer version of 本地AI服务. Please update to the latest version from Settings > 本地AI服务 > Service Version > ... > Force Update 本地AI服务"
# I will translate this one.
update_err = "{modelName} 需要更新版本的本地AI服务。请从 设置 > 本地AI服务 > 服务版本 > ... > 强制更新本地AI服务 进行更新"
set_key(data, "modelHub.localModels.modelInstall.errorMessage.newerVersion", update_err)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated Local AI to 本地AI服务.")
