"""
MCP 反饋收集器 - 為 MCP 服務器提供交互式用戶反饋收集功能

這個包提供了一個現代化的基於 GUI 的反饋收集系統，用於模型上下文協議 (MCP) 服務器，
允許 AI 助手通過直觀的界面收集用戶反饋。

主要功能：
- 交互式反饋收集對話框
- 支持文字和圖片反饋
- 多圖片選擇和預覽
- 剪貼板圖片粘貼功能
- 超時控制和錯誤處理
"""

# 版本信息
__version__ = "2.0.0"
__author__ = "MCP Feedback Collector Team"
__email__ = "your.email@example.com"

# 從服務器模塊導入主函數
from .server import main

# 公開的API接口
__all__ = ["main"]