import json
import os

file_path = 'zh_CN.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

def set_key(d, key_path, value):
    keys = key_path.split('.')
    for k in keys[:-1]:
        if k not in d:
            d[k] = {}
        d = d[k]
    d[keys[-1]] = value

def get_key(d, key_path):
    keys = key_path.split('.')
    curr = d
    for k in keys:
        if k in curr:
            curr = curr[k]
        else:
            return None
    return curr

# 1. Passive -> Active Voice
set_key(data, "modelHub.languageModelsProviders.providerForm.successMessage.addDetail", "已添加模型提供商 {providerName}")
set_key(data, "modelHub.languageModelsProviders.providerForm.successMessage.updateDetail", "已更新模型提供商 {providerName}")
set_key(data, "modelHub.languageModelsProviders.deleteConfirmation.successMessage.detail", "已删除提供方")

set_key(data, "manageData.exportSuccessMessage.detail", "已导出@:data")
set_key(data, "manageData.clearSuccessMessage.detail", "已清除@:data")
set_key(data, "manageData.importDataSuccessMessage.detail", "已导入 @:data")

set_key(data, "project.deleteConfirmation.successMessage.detail", "已删除项目")
set_key(data, "project.deleteAllConversations.successMessage.detail", "已删除 {count} 个对话 | 已删除 {count} 个对话")

set_key(data, "conversation.deleteConfirmation.successMessage.detail", "已删除@:conversation.title")
set_key(data, "conversation.convertToChat.successMessage.detail", "已将@:conversation.title转换为聊天")
set_key(data, "conversation.convertToForgeCanvas.successMessage.detail", "已将@:conversation.title转换为@:forge.forgeCanvas")
set_key(data, "conversation.cloneAncestorsSuccess.detail", "已将消息克隆到新拆分")
set_key(data, "conversation.cloneAncestorsToNewConversationSuccess.detail", "已将消息克隆到新对话")

set_key(data, "conversationActions.splitPresetForm.successMessage.saveDetail", "已添加拆分@:preset")
set_key(data, "conversationActions.splitPresetForm.successMessage.editDetail", "已更新拆分@:preset")
set_key(data, "conversationActions.deleteSplitPresetConfirmation.successMessage.detail", "已删除拆分@:preset")

set_key(data, "modelParams.savePresetForm.successMessage.detail", "已保存@:modelParams.params预设。")
set_key(data, "modelParams.deletePresetConfirm.successMessage.detail", "已删除@:modelParams.params预设。")

set_key(data, "chatSplitActions.copySplitToNewConversationSuccess.detail", "已将拆分复制到新对话")
set_key(data, "chatSplitActions.moveSplitToNewConversationSuccess.detail", "已将拆分移动到新对话")
set_key(data, "chatSplitActions.showAllHiddenMessages.successMessage.detail", "所有隐藏消息现已可见")

# 2. Acronyms & Terms
set_key(data, "modelHub.languageModelsProviders.providerForm.lmsCorsNote", "您必须在 LM Studio 中启用 CORS (跨来源资源共享) 才能与 Msty 配合使用")

# Fix potentially missing translations in settings.webSecurity
set_key(data, "settings.webSecurity.title", "禁用网络安全")
set_key(data, "settings.webSecurity.description", "这可能有助于您解决一些与 CORS (跨来源资源共享) 相关的问题。但是，不建议这样做，这可能会使您的应用程序面临安全风险。仅在您知道自己在做什么的情况下禁用它。您必须重启应用才能使此设置生效。")
set_key(data, "settings.webSecurity.applyAndRestart", "应用并重启")

# 3. Spacing
set_key(data, "modelHub.languageModelsProviders.toggleVisibility.successMessage.detail", "{provider} 现在{visibility}")

# 4. Additional cleanups (Reviewing other keys)
# "conversationActions.exportConversation.successMessage": "成功导出对话为 JSON" -> "已成功导出对话为 JSON" (Optional, but "成功导出" is also fine. "已成功导出" is slightly more formal active result).
set_key(data, "conversationActions.exportConversation.successMessage", "已成功导出对话为 JSON")

# "chatSplitActions.exportOrCopyChat.successMessage": "成功 {action} 聊天为 {format}" -> "已成功 {action} 聊天为 {format}"
set_key(data, "chatSplitActions.exportOrCopyChat.successMessage", "已成功 {action} 聊天为 {format}")

# "setupItem.success": "{item} 设置完成" -> "已完成 {item} 设置" or keep "{item} 设置完成" (Item setup completed).
# "{item} setup completed" -> "{item} 设置完成" is good.

# "onboard.modelsAddedCount": "{count} 个模型已添加" -> "已添加 {count} 个模型"
set_key(data, "onboard.modelsAddedCount", "已添加 {count} 个模型 | 已添加 {count} 个模型")

# "manageData.backupData": "备份@:data" -> "备份 @:data" (Add space for aesthetics? or remove? Rule says no space. "@:data" resolves to "数据". "备份数据" is fine. "备份@:data" -> "备份数据". No space needed.)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Refined zh_CN.json successfully.")
