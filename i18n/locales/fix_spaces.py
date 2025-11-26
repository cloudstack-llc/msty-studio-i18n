import json
import re

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

# Manually fix identified issues based on the report and user instructions.
# Rule: Remove space between Chinese and Variable/Ref unless the variable is English-like.

# {item} -> Chinese context -> Remove spaces
set_key(data, "selectItem", "@:select{item}")
set_key(data, "clone.successMessage.detail", "{item}已克隆")
set_key(data, "clone.errorMessage.detail", "克隆{item}失败")
set_key(data, "setupItem.label", "设置{item}")
set_key(data, "setupItem.success", "{item}设置完成")
set_key(data, "setupItem.failure", "无法设置{item}")
set_key(data, "duplicateName", "重复或无效的{item}名称。请输入唯一的名称。")
set_key(data, "settings.dataMigrate.successMessage", "成功迁移{item}") # Was "Successfully migrated {item}"
set_key(data, "settings.dataMigrate.errorMessage", "迁移{item}失败")
set_key(data, "settings.dataMigrate.migrationComplete", "{item}迁移完成")
set_key(data, "settings.dataMigrate.migrationFail", "{item}迁移失败")
set_key(data, "settings.dataMigrate.migratingItem", "正在迁移{item}...")
set_key(data, "copiedToClipboard.itemCopied", "{item}已复制到剪切板")
set_key(data, "pinItem.title", "已固定{item}")
set_key(data, "pinItem.action", "固定{item}")
set_key(data, "pinItem.successMessage.detail", "{item}已固定")
set_key(data, "pinItem.errorMessage.detail", "无法固定{item}")
set_key(data, "unpinItem.action", "取消固定{item}")
set_key(data, "unpinItem.successMessage.detail", "{item}已取消固定")
set_key(data, "unpinItem.errorMessage.detail", "无法取消固定{item}")
set_key(data, "setDefaultItem.title", "默认{item}")
set_key(data, "setDefaultItem.action", "将{item}设为默认")
set_key(data, "setDefaultItem.successMessage.detail", "{item}已设为默认")
set_key(data, "setDefaultItem.errorMessage.detail", "无法将{item}设为默认")
set_key(data, "unsetDefaultItem.action", "默认{item}。点击取消。")
set_key(data, "unsetDefaultItem.successMessage.detail", "{item}已取消默认")
set_key(data, "hideItem.action", "隐藏{item}")
set_key(data, "hideItem.successMessage.detail", "{item}已隐藏")
set_key(data, "hideItem.errorMessage.detail", "无法隐藏{item}")
set_key(data, "hideItem.unhideParent", "取消隐藏父级{item}")
set_key(data, "showItem.action", "显示{item}")
set_key(data, "cloneItem.action", "克隆{item}")
set_key(data, "cloneItem.successMessage.detail", "{item}已克隆")
set_key(data, "cloneItem.errorMessage.detail", "无法克隆{item}")
set_key(data, "cloneItemTo.action", "克隆到{item}")
set_key(data, "cloneItemTo.successMessage.detail", "已成功克隆到新{item}")
set_key(data, "cloneItemTo.errorMessage.detail", "无法克隆到新{item}")
set_key(data, "importJson.clipboardTitle", "从 JSON 剪切板导入{item}")
set_key(data, "importJson.fileTitle", "从 JSON 文件导入{item}")
set_key(data, "importJson.successMessage.detail", "{count} 个{item}已导入成功") # Keep space for count
set_key(data, "importJson.successMessage.detailDestination", "@:importJson.successMessage.detail {item} 到 {destination}")
set_key(data, "importJson.successMessageWithToolsets.detail", "{count} 个{item}已导入成功并自动创建了相应的工具集")
set_key(data, "importJson.dragAndDropMessage", "拖放 JSON 文件以导入{item}。")
set_key(data, "updateItem.action", "更新{item}")
set_key(data, "updateItem.editAction", "编辑{item}")
set_key(data, "updateItem.successMessage.detail", "{item}已更新")
set_key(data, "updateItem.errorMessage.detail", "无法更新{item}")
set_key(data, "makeActive.title", "设为活动{itemType}")
set_key(data, "makeActive.isActive", "活动{itemType}")
set_key(data, "makeActive.successMessage.detail", "{itemName}现在是活动{itemType}")
set_key(data, "makeActive.errorMessage.detail", "无法将{itemName}设为活动{itemType}")
set_key(data, "moveItem.action", "移动{item}")
set_key(data, "moveItem.moveLocation", "移动 {count} 个{sourceType}到{item}")
set_key(data, "moveItem.confirmation.message", "您确定要移动选中的{item}吗？")
set_key(data, "moveItem.successMessage.detail", "{item}已移动 | {item}已移动")
set_key(data, "moveItem.errorMessage.detail", "无法移动{item}")
set_key(data, "moveItem.errrorMessage.detail", "无法移动{item}")
set_key(data, "deleteItem.action", "删除{item}")
set_key(data, "deleteItem.successMessage.detail", "{item}已删除")
set_key(data, "deleteItem.errorMessage.detail", "无法删除{item}")
set_key(data, "importDefault.title", "导入默认{item}")
set_key(data, "importDefault.successMessage.detail", "已导入默认{item}")
set_key(data, "importDefault.errorMessage.detail", "导入默认{item}失败")
set_key(data, "reIndexItem.action", "重新索引{item}")
set_key(data, "reIndexItem.successMessage.detail", "{item}重新索引成功")
set_key(data, "reIndexItem.errorMessage.detail", "重新索引{item}失败")
set_key(data, "reIndexItem.confirmationMessage", "您确定要重新索引{item}吗？")
set_key(data, "selectModel", "@:select模型 | @:select模型") # Already done but check
set_key(data, "selectModel", "选择模型 | 选择模型") # Fix @:select ref spacing? No, replace with word if simpler or keep strict. "@:select模型" -> "选择模型" if @:select="选择". "选择模型" is safer. Let's use literal.

# {data} / @:data -> "数据" -> Remove spaces
set_key(data, "manageData.exportData", "导出数据")
set_key(data, "manageData.importDataSuccessMessage.detail", "已导入数据") # Was "已导入 @:data" -> "已导入数据"
set_key(data, "manageData.importDataErrorMessage.detail", "导入数据失败")
set_key(data, "manageData.backupData", "备份数据")
set_key(data, "manageData.clearData", "清除数据")
set_key(data, "manageData.restoreData", "恢复数据")
set_key(data, "manageData.clearDataConfirmation.header", "清除数据")
set_key(data, "manageData.restoreDataConfirmation.header", "恢复数据")
set_key(data, "workspaces.deleteConfirmation.downloadWorkspaceData", "下载工作空间数据")
set_key(data, "rtd.title", "实时数据") # Real Time Data

# {model} -> "模型" -> Remove spaces
set_key(data, "modelHub.languageModelsProviders.providerForm.selectModels", "选择模型")
set_key(data, "modelParams.savePresetForm.title", "保存参数为预设") # @:modelParams.params -> 参数
set_key(data, "modelParams.savePresetForm.successMessage.detail", "参数预设已保存。")
set_key(data, "modelParams.deletePresetConfirm.successMessage.detail", "参数预设已删除。")
set_key(data, "settings.localAI.serviceConfigurations.unsavedChanges.message", "您在@:localAIService配置中有未保存的更改。保存后，@:localAIService将使用新配置重启。")
set_key(data, "settings.localAI.serviceConfigurations.unsavedChanges.errorMessage.detail", "保存@:localAIService配置失败。请检查日志以获取更多详细信息。")
set_key(data, "settings.localAI.modelConfigurations.unsavedChanges.message", "您在@:settings.localAI.modelConfigurations.title中有未保存的更改。请确保在开始新聊天会话前保存它们。")
set_key(data, "settings.localAI.modelConfigurations.unsavedChanges.errorMessage.detail", "保存@:settings.localAI.modelConfigurations.title失败。请检查日志以获取更多详细信息。")

# {conversation} -> "对话" -> Remove spaces
set_key(data, "conversationActions.exportConversation.title", "导出@:conversation.title为 JSON")
set_key(data, "conversation.deleteConversation", "删除@:conversation.title")
set_key(data, "conversation.addNewConversation", "添加新@:conversation.title")
set_key(data, "conversation.newConversation", "新@:conversation.title")
set_key(data, "conversation.deleteConfirmation.header", "删除@:conversation.title")
set_key(data, "conversation.deleteConfirmation.successMessage.detail", "@:conversation.title已删除")
set_key(data, "conversation.deleteConfirmation.errorMessage.detail", "删除@:conversation.title失败")
set_key(data, "conversation.convertToChat.successMessage.detail", "@:conversation.title已转换为聊天")
set_key(data, "conversation.convertToForgeCanvas.successMessage.detail", "@:conversation.title已转换为@:forge.forgeCanvas")

# {preset} -> "预设"
set_key(data, "conversationActions.splitPresetForm.editTitle", "编辑拆分@:preset {presetName}") # Keep space for English Name
set_key(data, "conversationActions.splitPresetForm.presetOptionsPlaceholder", "选择@:preset选项")
set_key(data, "conversationActions.deleteSplitPresetConfirmation.message", "您确定要删除 {splitPresetName} 吗？")
set_key(data, "modelParams.deletePresetConfirm.message", "您确定要删除 {presetName} 吗？")

# {provider}
set_key(data, "modelHub.languageModelsProviders.deleteConfirmation.message", "您确定要删除 {providerName} 吗？")
set_key(data, "modelHub.languageModelsProviders.toggleVisibility.successMessage.detail", "{provider}现在{visibility}")

# {service} -> "服务" or English name?
# "继续 {service} 设置" -> "继续{service}设置" (User: "unless things are like providernames... there shouldn't be spaces")
# Service names can be "Local AI", "MLX". "继续 Local AI 设置". Space looks better for English words.
# But if service is translated... "继续服务设置".
# Let's assume Service Name is English/Proper Noun. Keep space.

# {action} -> "操作" (translated usually)
set_key(data, "chatSplitActions.exportOrCopyChat.successMessage", "已成功将聊天{action}为 {format}") # "成功导出聊天为 JSON" -> "已成功将聊天导出为 JSON"

# {format} -> JSON/Markdown (English) -> Keep space.

# {group} -> "组"
set_key(data, "sidebar.expandGroup", "展开{group}")
set_key(data, "sidebar.collapseGroup", "折叠{group}")

# {folder}
set_key(data, "persona.folderForm.updateErrorMessage.detail", "更新@:folder失败")
set_key(data, "persona.folderForm.createErrorMessage.detail", "创建@:folder失败")
set_key(data, "persona.folderForm.deleteConfirmation.header", "删除@:folder")
set_key(data, "persona.folderForm.deleteConfirmation.errorMessage.detail", "删除@:folder失败")
set_key(data, "promptsLibrary.folderForm.updateErrorMessage.detail", "更新@:folder失败")
set_key(data, "promptsLibrary.folderForm.createErrorMessage.detail", "创建@:folder失败")
set_key(data, "promptsLibrary.folderForm.deleteConfirmation.header", "删除@:folder")
set_key(data, "promptsLibrary.folderForm.deleteConfirmation.errorMessage.detail", "删除@:folder失败")

# Misc
set_key(data, "conversation.promptPlaceHolder.normal.focused", "按 {trigger} 键使用快捷指令 或 开始输入...") # Trigger is usually '/'
set_key(data, "conversationActions.enableCompactMode", "启用紧凑模式")
set_key(data, "conversationActions.disableCompactMode", "禁用紧凑模式")
set_key(data, "login.successMessage", "登录链接已发送至 {email}") # Fix variable name spacing too

# Fix "import @:data" types
set_key(data, "manageData.importDataSuccessMessage.detail", "数据已导入")

# {item} in general
set_key(data, "selectItem", "选择{item}")

# {count}
# "已删除 {count} 个对话" -> "已删除{count}个对话" (Compact chinese)
set_key(data, "project.deleteAllConversations.successMessage.detail", "已删除{count}个对话 | 已删除{count}个对话")
set_key(data, "onboard.modelsAvailableCount", "{count}个模型可用 | {count}个模型可用")
set_key(data, "onboard.modelsAddedCount", "已添加{count}个模型 | 已添加{count}个模型")

# Setup Item
set_key(data, "setupItem.success", "{item}设置完成")

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Space refinements applied.")
