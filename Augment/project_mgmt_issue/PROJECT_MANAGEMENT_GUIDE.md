# Augment Code 項目管理系統使用指南

## 🎯 **系統概述**

這個項目管理系統專為Augment Code開發環境設計，支持三種主要的開發類型：
- **網站開發** (website) - HTML/CSS/JavaScript項目
- **n8n工作流程** (n8n) - 自動化工作流程JSON文件
- **小說寫作** (novel) - 文學創作項目

## 🚀 **快速開始**

### **方法1：使用圖形界面 (推薦)**
```bash
# 運行圖形界面
project_setup.bat
```

### **方法2：使用命令行**
```bash
# 查看幫助
python project_manager.py

# 創建新項目
python project_manager.py init my_website website
python project_manager.py init my_workflow n8n
python project_manager.py init my_novel novel
```

## 📁 **項目結構**

系統會自動創建以下目錄結構：
```
Projects/
├── my_website/
│   ├── project.json          # 項目配置文件
│   └── versions/
│       ├── v1.0.0/           # 版本1.0.0
│       ├── v1.0.1/           # 版本1.0.1
│       └── v1.0.2/           # 版本1.0.2
├── my_workflow/
└── my_novel/

project_config.json           # 全局配置
.current_project             # 當前項目標記
```

## 🛠️ **主要功能**

### **1. 創建新項目**
```bash
python project_manager.py init <項目名稱> <項目類型>
```

**項目類型說明：**
- `website` - 創建網站開發項目，工作目錄：`Augment/`
- `n8n` - 創建n8n工作流程項目，工作目錄：`Alex_Hsieh/`
- `novel` - 創建小說寫作項目，工作目錄：`Prompt/William/`

**示例：**
```bash
python project_manager.py init augment_website website
python project_manager.py init crm_workflow n8n
python project_manager.py init fantasy_novel novel
```

### **2. 列出所有項目**
```bash
python project_manager.py list
```

**輸出示例：**
```
📋 項目列表:
------------------------------------------------------------
🟢 當前 augment_website
   類型: website
   版本: v1.0.2
   路徑: Projects\augment_website

⚪ crm_workflow
   類型: n8n
   版本: v1.0.1
   路徑: Projects\crm_workflow
```

### **3. 切換項目**
```bash
# 切換到最新版本
python project_manager.py switch <項目名稱>

# 切換到指定版本
python project_manager.py switch <項目名稱> <版本號>
```

**示例：**
```bash
python project_manager.py switch augment_website
python project_manager.py switch crm_workflow v1.0.1
```

### **4. 保存當前工作**
```bash
python project_manager.py save <項目名稱> [描述]
```

**示例：**
```bash
python project_manager.py save augment_website "添加多語言支持"
python project_manager.py save crm_workflow "修復客戶數據同步問題"
```

### **5. 查看項目狀態**
```bash
python project_manager.py status
```

**輸出示例：**
```
🟢 當前項目: augment_website
📁 項目類型: website
🏷️  當前版本: v1.0.2
📂 項目路徑: Projects\augment_website
⏰ 創建時間: 2025-01-13T16:30:00
📝 描述: 網站開發項目
```

### **6. 查看版本歷史**
```bash
python project_manager.py versions <項目名稱>
```

**輸出示例：**
```
📋 項目 'augment_website' 版本歷史:
--------------------------------------------------
🟢 當前 v1.0.2
   時間: 2025-01-13T16:45:00
   描述: 添加多語言支持
   文件: 15 個

⚪ v1.0.1
   時間: 2025-01-13T16:30:00
   描述: 修復CSS樣式問題
   文件: 12 個

⚪ v1.0.0
   時間: 2025-01-13T16:00:00
   描述: 初始版本
   文件: 8 個
```

## 🔄 **工作流程示例**

### **網站開發項目**
```bash
# 1. 創建網站項目
python project_manager.py init my_website website

# 2. 切換到項目 (文件會恢復到 Augment/ 目錄)
python project_manager.py switch my_website

# 3. 在 Augment/ 目錄中開發網站
# 編輯 index.html, styles.css, script.js 等

# 4. 保存當前進度
python project_manager.py save my_website "完成首頁設計"

# 5. 繼續開發...
# 6. 再次保存
python project_manager.py save my_website "添加響應式設計"
```

### **n8n工作流程項目**
```bash
# 1. 創建工作流程項目
python project_manager.py init crm_automation n8n

# 2. 切換到項目 (文件會恢復到 Alex_Hsieh/ 目錄)
python project_manager.py switch crm_automation

# 3. 在 Alex_Hsieh/ 目錄中開發工作流程
# 編輯 .json 文件

# 4. 保存版本
python project_manager.py save crm_automation "完成客戶數據同步流程"
```

### **小說寫作項目**
```bash
# 1. 創建小說項目
python project_manager.py init fantasy_story novel

# 2. 切換到項目 (文件會恢復到 Prompt/William/ 目錄)
python project_manager.py switch fantasy_story

# 3. 在 Prompt/William/ 目錄中寫作
# 編輯 outline.md, characters.md, chapters/ 等

# 4. 保存章節進度
python project_manager.py save fantasy_story "完成第1-3章"
```

## 🎨 **項目模板**

### **Website 項目模板**
創建時自動生成：
- `index.html` - 主頁面
- `styles.css` - 樣式文件
- `script.js` - JavaScript文件
- `README.md` - 項目說明

### **n8n 項目模板**
創建時自動生成：
- `workflow.json` - 工作流程配置
- `config.json` - 配置文件
- `README.md` - 項目說明

### **Novel 項目模板**
創建時自動生成：
- `outline.md` - 故事大綱
- `characters.md` - 角色設定
- `chapters/` - 章節目錄
- `README.md` - 項目說明

## ⚙️ **高級功能**

### **自動文件檢測**
系統會根據項目類型自動檢測和保存相關文件：
- **Website**: `.html`, `.css`, `.js`, `.md`, `.json`
- **n8n**: `.json`, `.md`
- **Novel**: `.md`, `.txt`, `.docx`

### **版本自動編號**
版本號採用語義化版本控制：
- 初始版本：`v1.0.0`
- 後續版本：`v1.0.1`, `v1.0.2`, `v1.0.3`...

### **工作目錄映射**
- **Website** → `Augment/` 目錄
- **n8n** → `Alex_Hsieh/` 目錄  
- **Novel** → `Prompt/William/` 目錄

## 🔧 **故障排除**

### **常見問題**

**Q: 切換項目後文件沒有恢復？**
A: 檢查項目類型對應的工作目錄是否存在，確保有足夠的文件權限。

**Q: 保存時提示項目不存在？**
A: 使用 `python project_manager.py list` 查看項目列表，確認項目名稱正確。

**Q: 版本歷史丟失？**
A: 檢查 `Projects/` 目錄下的項目文件夾是否完整，查看 `project.json` 配置文件。

### **重置系統**
如果需要重置整個項目管理系統：
```bash
# 刪除配置文件
del project_config.json
del .current_project

# 刪除項目目錄 (謹慎操作!)
rmdir /s Projects
```

## 📝 **最佳實踐**

1. **定期保存**: 完成重要功能後及時保存版本
2. **描述清晰**: 為每個版本提供清晰的描述信息
3. **項目分類**: 按功能和類型合理創建項目
4. **版本管理**: 重大更改前先保存當前版本
5. **備份重要**: 定期備份 `Projects/` 目錄

## 🚀 **進階使用**

### **批量操作**
可以編寫腳本實現批量項目操作：
```bash
# 批量保存所有項目
for project in website_project n8n_project novel_project; do
    python project_manager.py save $project "定期備份"
done
```

### **集成Git**
可以將整個 `Projects/` 目錄納入Git版本控制：
```bash
git add Projects/
git commit -m "更新項目版本"
```

---

**🎉 現在您可以高效地管理多個開發項目，在不同版本間自由切換，再也不用擔心丟失工作進度了！**
