# Translation Guide (Chinese - Simplified)

This guide outlines the standards and best practices for translating the project into Simplified Chinese (`zh_CN`), based on the conventions established in the legacy configuration files (`*_old.json`).

## 1. Syntax & Formatting

### Variables
*   **Format:** Variables are denoted by curly braces, e.g., `{item}`, `{modelName}`.
*   **Rule:** **Do not translate the variable name inside the braces.**
*   **Spacing:** Unlike English, **do not add spaces** between Chinese characters and the variable unless necessary for separation from another English word.
    *   *English:* `"New {item}"`
    *   *Chinese:* `"新{item}"` (No space)
    *   *English:* `"Edit {item}"`
    *   *Chinese:* `"编辑{item}"`

### Plurals & Variants
*   **Format:** The pipe character `|` is used to separate singular and plural forms (or variants).
*   **Rule:** Chinese generally does not distinguish between singular and plural nouns. Usually, the same term is repeated on both sides of the pipe to maintain the format required by the application.
    *   *English:* `"Model | Models"`
    *   *Chinese:* `"模型 | 模型"`
    *   *English:* `"Folder | Folders"`
    *   *Chinese:* `"文件夹 | 文件夹"`

### Punctuation
*   **Ellipsis:** Use `...` as seen in the source.
    *   *English:* `"Loading {item}..."`
    *   *Chinese:* `"加载{item}..."`
*   **Colons:** Use full-width colons `：` in UI labels if applicable, though the JSON values often omit them or use standard colons depending on context. Follow the source string's lead but adapt for Chinese typography where appropriate.

## 2. Terminology Glossary

Consistency is key. Use the following standard translations for core application terms:

| English Term | Chinese Translation | Notes |
| :--- | :--- | :--- |
| **AI** | AI | Keep as "AI" (e.g., 本地AI服务) |
| **Appearance** | 外观 | |
| **Application** | 应用 | |
| **Cancel** | 取消 | |
| **Chat** | 聊天 / 对话 | "Chat" as a verb/action is often "聊天", as a noun/object "对话" (Conversation) |
| **Confirm** | 确认 | |
| **Context Shield** | 内容保护盾 | |
| **Conversation** | 对话 | |
| **Delete** | 删除 | |
| **Edit** | 编辑 | |
| **Folder** | 文件夹 | |
| **General** | 总览 | In settings context |
| **Knowledge Stack** | 知识库 | |
| **License** | 许可证 | |
| **Local AI** | 本地AI | |
| **Model** | 模型 | |
| **New** | 新 | e.g., 新{item} |
| **Prompt** | 提示词 | |
| **Provider** | 提供方 / 服务商 | "Provider" -> 提供方, "Service Provider" -> 服务商 |
| **Remote** | 远端 | e.g., 远端模型 |
| **Remove** | 移除 | |
| **Reset** | 重置 | |
| **Save** | 保存 | |
| **Search** | 搜索 | |
| **Settings** | 设置 | |
| **Split Chat** | 拆分对话 | |
| **System** | 系统 | e.g., 跟随系统 (Follow System) |
| **Theme** | 主题 | |
| **Token** | Token | Keep as "Token" usually, or "初始token" (Initial token) |
| **Workspace** | 工作空间 | |

## 3. Style & Tone

*   **Professional & Concise:** The translation should be formal yet user-friendly. Avoid overly colloquial language.
*   **Action-Oriented:** For buttons and menu items, use precise verbs (e.g., "Switch to" -> "切换为", "Import" -> "导入").
*   **Expansion:** Some English terms need expansion to be natural in Chinese.
    *   *English:* "Light" (Theme) -> *Chinese:* "亮色主题" (Light Color Theme)
    *   *English:* "Dark" (Theme) -> *Chinese:* "暗色主题" (Dark Color Theme)

### Grammar & Voice
*   **Active Voice:** Prefer active voice for status messages.
    *   *Bad:* `"Model provider {name} added"` -> `"模型提供方 {name} 已添加"`
    *   *Good:* `"Model provider {name} added"` -> `"已添加模型提供方 {name}"`
    *   *Bad:* `"{item} deleted"` -> `"{item} 已删除"`
    *   *Good:* `"{item} deleted"` -> `"已删除 {item}"`

## 4. Common Patterns

*   **"Toggle {item}"** -> `"开关{item}"`
*   **"Select {item}"** -> `"选择{item}"`
*   **"Fetch {item}"** -> `"获取{item}"`
*   **"Manage {item}"** -> `"管理{item}"`

## 5. Specific Rules & Corrections

### Spacing with Variables
*   **General Rule:** Do **NOT** add spaces between Chinese characters and variables, especially if the variable content is likely to be Chinese or a generic item.
    *   *Correct:* `"{item}设置完成"`
    *   *Incorrect:* `"{item} 设置完成"`
    *   *Correct:* `"已导入{count}个模型"`
    *   *Incorrect:* `"已导入 {count} 个模型"`
*   **Exception:** You may keep a space if the variable is expected to be an English Proper Noun (like a Provider Name).
    *   *Example:* `"已添加模型提供方 {providerName}"`

### Acronyms
*   **CORS:** Translate/Explain as `"CORS (跨来源资源共享)"` where appropriate in descriptions/settings. For simple labels, "CORS" might suffice if space is limited, but prefer the explanation.
*   **Local AI:** Translate as `"本地AI服务"`.

### Terminology Updates
*   **Provider:** "模型提供商" or "提供方" (Provider).
*   **Local AI:** "本地AI服务".
