#!/usr/bin/env python3
"""
Augment Code 項目管理系統
支持網站開發、n8n工作流程、小說寫作的版本控制和項目切換

使用方法:
python project_manager.py init <project_name> <project_type>
python project_manager.py list
python project_manager.py switch <project_name> [version]
python project_manager.py save <project_name> [description]
python project_manager.py status
python project_manager.py versions <project_name>
"""

import os
import sys
import json
import shutil
import datetime
from pathlib import Path
from typing import Dict, List, Optional

class ProjectManager:
    def __init__(self):
        self.base_dir = Path(".")
        self.projects_dir = self.base_dir / "Projects"
        self.config_file = self.base_dir / "project_config.json"
        self.current_project_file = self.base_dir / ".current_project"
        
        # 確保項目目錄存在
        self.projects_dir.mkdir(exist_ok=True)
        
        # 項目類型配置
        self.project_types = {
            "website": {
                "description": "網站開發項目",
                "template_files": ["index.html", "styles.css", "script.js", "README.md"],
                "work_dir": "Augment",
                "extensions": [".html", ".css", ".js", ".md", ".json"]
            },
            "n8n": {
                "description": "n8n工作流程項目", 
                "template_files": ["workflow.json", "README.md", "config.json"],
                "work_dir": "Alex_Hsieh",
                "extensions": [".json", ".md"]
            },
            "novel": {
                "description": "小說寫作項目",
                "template_files": ["outline.md", "characters.md", "chapters/", "README.md"],
                "work_dir": "Prompt/William",
                "extensions": [".md", ".txt", ".docx"]
            }
        }
        
        self.load_config()
    
    def load_config(self):
        """載入項目配置"""
        if self.config_file.exists():
            with open(self.config_file, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        else:
            self.config = {"projects": {}, "current_project": None}
            self.save_config()
    
    def save_config(self):
        """保存項目配置"""
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)
    
    def get_current_project(self) -> Optional[str]:
        """獲取當前項目"""
        if self.current_project_file.exists():
            with open(self.current_project_file, 'r') as f:
                return f.read().strip()
        return None
    
    def set_current_project(self, project_name: str):
        """設置當前項目"""
        with open(self.current_project_file, 'w') as f:
            f.write(project_name)
        self.config["current_project"] = project_name
        self.save_config()
    
    def init_project(self, project_name: str, project_type: str):
        """初始化新項目"""
        if project_type not in self.project_types:
            print(f"❌ 不支持的項目類型: {project_type}")
            print(f"支持的類型: {', '.join(self.project_types.keys())}")
            return False
        
        project_dir = self.projects_dir / project_name
        if project_dir.exists():
            print(f"❌ 項目 '{project_name}' 已存在")
            return False
        
        # 創建項目目錄結構
        project_dir.mkdir(parents=True)
        versions_dir = project_dir / "versions"
        versions_dir.mkdir()
        
        # 創建初始版本
        v1_dir = versions_dir / "v1.0.0"
        v1_dir.mkdir()
        
        # 創建項目配置
        project_config = {
            "name": project_name,
            "type": project_type,
            "description": self.project_types[project_type]["description"],
            "created_at": datetime.datetime.now().isoformat(),
            "current_version": "v1.0.0",
            "versions": {
                "v1.0.0": {
                    "created_at": datetime.datetime.now().isoformat(),
                    "description": "初始版本",
                    "files": []
                }
            }
        }
        
        # 保存項目配置
        with open(project_dir / "project.json", 'w', encoding='utf-8') as f:
            json.dump(project_config, f, indent=2, ensure_ascii=False)
        
        # 創建模板文件
        self.create_template_files(v1_dir, project_type)
        
        # 更新全局配置
        self.config["projects"][project_name] = {
            "type": project_type,
            "path": str(project_dir),
            "current_version": "v1.0.0"
        }
        self.save_config()
        
        print(f"✅ 項目 '{project_name}' ({project_type}) 創建成功")
        print(f"📁 項目路徑: {project_dir}")
        return True
    
    def create_template_files(self, version_dir: Path, project_type: str):
        """創建模板文件"""
        templates = self.project_types[project_type]["template_files"]
        
        for template in templates:
            if template.endswith("/"):
                # 創建目錄
                (version_dir / template).mkdir(parents=True)
            else:
                # 創建文件
                file_path = version_dir / template
                file_path.parent.mkdir(parents=True, exist_ok=True)
                
                if template == "README.md":
                    content = f"# {version_dir.parent.parent.name}\n\n項目類型: {project_type}\n創建時間: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n## 版本歷史\n\n### v1.0.0\n- 初始版本\n"
                elif template.endswith(".json"):
                    content = "{}\n"
                elif template.endswith(".html"):
                    content = "<!DOCTYPE html>\n<html>\n<head>\n    <title>New Project</title>\n</head>\n<body>\n    <h1>Hello World</h1>\n</body>\n</html>\n"
                elif template.endswith(".css"):
                    content = "/* 樣式文件 */\nbody {\n    font-family: Arial, sans-serif;\n}\n"
                elif template.endswith(".js"):
                    content = "// JavaScript 文件\nconsole.log('Hello World');\n"
                else:
                    content = f"# {template}\n\n這是一個 {project_type} 項目文件。\n"
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
    
    def list_projects(self):
        """列出所有項目"""
        if not self.config["projects"]:
            print("📝 沒有找到任何項目")
            return
        
        current = self.get_current_project()
        print("📋 項目列表:")
        print("-" * 60)
        
        for name, info in self.config["projects"].items():
            status = "🟢 當前" if name == current else "⚪"
            print(f"{status} {name}")
            print(f"   類型: {info['type']}")
            print(f"   版本: {info['current_version']}")
            print(f"   路徑: {info['path']}")
            print()
    
    def switch_project(self, project_name: str, version: Optional[str] = None):
        """切換項目"""
        if project_name not in self.config["projects"]:
            print(f"❌ 項目 '{project_name}' 不存在")
            return False
        
        project_dir = Path(self.config["projects"][project_name]["path"])
        project_config_file = project_dir / "project.json"
        
        if not project_config_file.exists():
            print(f"❌ 項目配置文件不存在: {project_config_file}")
            return False
        
        with open(project_config_file, 'r', encoding='utf-8') as f:
            project_config = json.load(f)
        
        # 確定要切換的版本
        target_version = version or project_config["current_version"]
        if target_version not in project_config["versions"]:
            print(f"❌ 版本 '{target_version}' 不存在")
            print(f"可用版本: {', '.join(project_config['versions'].keys())}")
            return False
        
        # 備份當前工作區（如果有當前項目）
        current_project = self.get_current_project()
        if current_project and current_project != project_name:
            self.save_current_work(current_project)
        
        # 恢復項目文件到工作區
        self.restore_project_files(project_name, target_version)
        
        # 更新當前項目
        self.set_current_project(project_name)
        
        print(f"✅ 已切換到項目 '{project_name}' 版本 '{target_version}'")
        return True
    
    def save_current_work(self, project_name: str, description: str = ""):
        """保存當前工作到項目版本"""
        if project_name not in self.config["projects"]:
            print(f"❌ 項目 '{project_name}' 不存在")
            return False
        
        project_dir = Path(self.config["projects"][project_name]["path"])
        project_config_file = project_dir / "project.json"
        
        with open(project_config_file, 'r', encoding='utf-8') as f:
            project_config = json.load(f)
        
        # 生成新版本號
        versions = list(project_config["versions"].keys())
        latest_version = max(versions, key=lambda x: [int(i) for i in x[1:].split('.')])
        major, minor, patch = [int(i) for i in latest_version[1:].split('.')]
        new_version = f"v{major}.{minor}.{patch + 1}"
        
        # 創建新版本目錄
        new_version_dir = project_dir / "versions" / new_version
        new_version_dir.mkdir(parents=True)
        
        # 複製當前工作文件
        project_type = project_config["type"]
        work_dir = Path(self.project_types[project_type]["work_dir"])
        
        if work_dir.exists():
            self.copy_work_files(work_dir, new_version_dir, project_type)
        
        # 更新項目配置
        project_config["versions"][new_version] = {
            "created_at": datetime.datetime.now().isoformat(),
            "description": description or f"自動保存版本",
            "files": self.get_file_list(new_version_dir)
        }
        project_config["current_version"] = new_version
        
        with open(project_config_file, 'w', encoding='utf-8') as f:
            json.dump(project_config, f, indent=2, ensure_ascii=False)
        
        # 更新全局配置
        self.config["projects"][project_name]["current_version"] = new_version
        self.save_config()
        
        print(f"✅ 已保存項目 '{project_name}' 為版本 '{new_version}'")
        return True
    
    def copy_work_files(self, source_dir: Path, target_dir: Path, project_type: str):
        """複製工作文件"""
        extensions = self.project_types[project_type]["extensions"]
        
        for file_path in source_dir.rglob("*"):
            if file_path.is_file() and any(str(file_path).endswith(ext) for ext in extensions):
                relative_path = file_path.relative_to(source_dir)
                target_file = target_dir / relative_path
                target_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(file_path, target_file)
    
    def restore_project_files(self, project_name: str, version: str):
        """恢復項目文件到工作區"""
        project_dir = Path(self.config["projects"][project_name]["path"])
        version_dir = project_dir / "versions" / version
        
        with open(project_dir / "project.json", 'r', encoding='utf-8') as f:
            project_config = json.load(f)
        
        project_type = project_config["type"]
        work_dir = Path(self.project_types[project_type]["work_dir"])
        
        # 清理工作目錄（可選）
        # if work_dir.exists():
        #     shutil.rmtree(work_dir)
        
        work_dir.mkdir(parents=True, exist_ok=True)
        
        # 複製版本文件到工作區
        if version_dir.exists():
            for file_path in version_dir.rglob("*"):
                if file_path.is_file():
                    relative_path = file_path.relative_to(version_dir)
                    target_file = work_dir / relative_path
                    target_file.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(file_path, target_file)
    
    def get_file_list(self, directory: Path) -> List[str]:
        """獲取目錄中的文件列表"""
        files = []
        for file_path in directory.rglob("*"):
            if file_path.is_file():
                files.append(str(file_path.relative_to(directory)))
        return files
    
    def show_status(self):
        """顯示當前狀態"""
        current = self.get_current_project()
        if not current:
            print("📝 當前沒有活動項目")
            return
        
        if current not in self.config["projects"]:
            print(f"❌ 當前項目 '{current}' 配置不存在")
            return
        
        project_info = self.config["projects"][current]
        project_dir = Path(project_info["path"])
        
        with open(project_dir / "project.json", 'r', encoding='utf-8') as f:
            project_config = json.load(f)
        
        print(f"🟢 當前項目: {current}")
        print(f"📁 項目類型: {project_info['type']}")
        print(f"🏷️  當前版本: {project_info['current_version']}")
        print(f"📂 項目路徑: {project_info['path']}")
        print(f"⏰ 創建時間: {project_config['created_at']}")
        print(f"📝 描述: {project_config['description']}")
    
    def show_versions(self, project_name: str):
        """顯示項目版本歷史"""
        if project_name not in self.config["projects"]:
            print(f"❌ 項目 '{project_name}' 不存在")
            return
        
        project_dir = Path(self.config["projects"][project_name]["path"])
        with open(project_dir / "project.json", 'r', encoding='utf-8') as f:
            project_config = json.load(f)
        
        print(f"📋 項目 '{project_name}' 版本歷史:")
        print("-" * 50)
        
        current_version = project_config["current_version"]
        for version, info in project_config["versions"].items():
            status = "🟢 當前" if version == current_version else "⚪"
            print(f"{status} {version}")
            print(f"   時間: {info['created_at']}")
            print(f"   描述: {info['description']}")
            print(f"   文件: {len(info.get('files', []))} 個")
            print()

def main():
    if len(sys.argv) < 2:
        print("使用方法:")
        print("  python project_manager.py init <project_name> <project_type>")
        print("  python project_manager.py list")
        print("  python project_manager.py switch <project_name> [version]")
        print("  python project_manager.py save <project_name> [description]")
        print("  python project_manager.py status")
        print("  python project_manager.py versions <project_name>")
        return
    
    pm = ProjectManager()
    command = sys.argv[1]
    
    if command == "init":
        if len(sys.argv) != 4:
            print("使用方法: python project_manager.py init <project_name> <project_type>")
            print("項目類型: website, n8n, novel")
            return
        pm.init_project(sys.argv[2], sys.argv[3])
    
    elif command == "list":
        pm.list_projects()
    
    elif command == "switch":
        if len(sys.argv) < 3:
            print("使用方法: python project_manager.py switch <project_name> [version]")
            return
        version = sys.argv[3] if len(sys.argv) > 3 else None
        pm.switch_project(sys.argv[2], version)
    
    elif command == "save":
        if len(sys.argv) < 3:
            print("使用方法: python project_manager.py save <project_name> [description]")
            return
        description = sys.argv[3] if len(sys.argv) > 3 else ""
        pm.save_current_work(sys.argv[2], description)
    
    elif command == "status":
        pm.show_status()
    
    elif command == "versions":
        if len(sys.argv) != 3:
            print("使用方法: python project_manager.py versions <project_name>")
            return
        pm.show_versions(sys.argv[2])
    
    else:
        print(f"❌ 未知命令: {command}")

if __name__ == "__main__":
    main()
