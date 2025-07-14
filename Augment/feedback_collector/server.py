"""
交互式反饋收集器 MCP 服務器

這是一個基於 Model Context Protocol (MCP) 的服務器，提供交互式用戶反饋收集功能。
AI 助手可以通過此服務器向用戶展示工作完成情況，並收集用戶的文字和圖片反饋。

主要特性：
1. 美觀的 GUI 界面，使用 tkinter 構建
2. 支持多種反饋方式：純文字、純圖片、文字+圖片
3. 多圖片選擇和預覽功能
4. 剪貼板圖片粘貼支持
5. 可配置的超時控制
6. 完整的錯誤處理機制

技術棧：
- MCP (Model Context Protocol) - 用於 AI 工具集成
- tkinter - Python 標準 GUI 庫
- PIL/Pillow - 圖片處理庫
- threading - 多線程支持
- queue - 線程間通信
"""

# 標準庫導入
import io
import base64
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from PIL import Image, ImageTk
import threading
import queue
from pathlib import Path
from datetime import datetime
import os

# MCP 相關導入
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.utilities.types import Image as MCPImage

# 創建 MCP 服務器實例
# FastMCP 是一個簡化的 MCP 服務器框架，用於快速構建 MCP 工具
mcp = FastMCP(
    "交互式反饋收集器",  # 服務器名稱
    dependencies=["pillow", "tkinter"]  # 依賴的 Python 包
)

# 配置超時時間（秒）
# 用戶可以通過環境變量 MCP_DIALOG_TIMEOUT 自定義超時時間
DEFAULT_DIALOG_TIMEOUT = 300  # 默認 5 分鐘
DIALOG_TIMEOUT = int(os.getenv("MCP_DIALOG_TIMEOUT", DEFAULT_DIALOG_TIMEOUT))

class FeedbackDialog:
    """
    反饋收集對話框類

    這個類負責創建和管理用戶反饋收集的 GUI 界面。
    使用 tkinter 構建現代化的用戶界面，支持文字和圖片反饋。

    主要功能：
    - 顯示 AI 工作完成報告
    - 收集用戶文字反饋
    - 支持多圖片選擇和預覽
    - 剪貼板圖片粘貼
    - 超時控制
    """

    def __init__(self, work_summary: str = "", timeout_seconds: int = DIALOG_TIMEOUT):
        """
        初始化反饋對話框

        Args:
            work_summary: AI 完成的工作內容摘要
            timeout_seconds: 對話框超時時間（秒）
        """
        self.result_queue = queue.Queue()  # 用於線程間通信的隊列
        self.root = None  # tkinter 根窗口
        self.work_summary = work_summary  # 工作摘要文本
        self.timeout_seconds = timeout_seconds  # 超時時間
        self.selected_images = []  # 存儲選中的圖片信息（支持多張）
        self.image_preview_frame = None  # 圖片預覽框架
        self.text_widget = None  # 文字輸入組件
        
    def show_dialog(self):
        """
        在新線程中顯示反饋收集對話框

        這個方法使用多線程技術來避免阻塞主程序：
        1. 創建新線程運行 tkinter GUI
        2. 主線程等待用戶反饋結果
        3. 通過 queue 進行線程間通信
        4. 支持超時處理

        Returns:
            dict or None: 用戶反饋結果，超時時返回 None
        """
        def run_dialog():
            """在新線程中運行對話框的內部函數"""
            # 創建 tkinter 根窗口
            self.root = tk.Tk()
            self.root.title("🎯 工作完成匯報與反饋收集")
            self.root.geometry("700x800")  # 設置窗口大小
            self.root.resizable(True, True)  # 允許調整大小
            self.root.configure(bg="#f5f5f5")  # 設置背景色

            # 設置窗口圖標和樣式
            try:
                self.root.iconbitmap(default="")  # 嘗試設置圖標
            except:
                pass  # 忽略圖標設置錯誤

            # 居中顯示窗口
            self.root.eval('tk::PlaceWindow . center')

            # 創建界面組件
            self.create_widgets()

            # 運行 tkinter 主循環
            self.root.mainloop()

        # 在新線程中運行對話框，避免阻塞主程序
        dialog_thread = threading.Thread(target=run_dialog)
        dialog_thread.daemon = True  # 設為守護線程
        dialog_thread.start()

        # 主線程等待結果
        try:
            # 從隊列中獲取結果，設置超時時間
            result = self.result_queue.get(timeout=self.timeout_seconds)
            return result
        except queue.Empty:
            # 超時情況：用戶未在規定時間內提供反饋
            return None
            
    def create_widgets(self):
        """创建美化的界面组件"""
        # 主框架
        main_frame = tk.Frame(self.root, bg="#f5f5f5")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # 标题
        title_label = tk.Label(
            main_frame,
            text="🎯 工作完成汇报与反馈收集",
            font=("Microsoft YaHei", 16, "bold"),
            bg="#f5f5f5",
            fg="#2c3e50"
        )
        title_label.pack(pady=(0, 20))
        
        # 1. 工作汇报区域
        report_frame = tk.LabelFrame(
            main_frame, 
            text="📋 AI工作完成汇报", 
            font=("Microsoft YaHei", 12, "bold"),
            bg="#ffffff",
            fg="#34495e",
            relief=tk.RAISED,
            bd=2
        )
        report_frame.pack(fill=tk.X, pady=(0, 15))
        
        report_text = tk.Text(
            report_frame, 
            height=5, 
            wrap=tk.WORD, 
            bg="#ecf0f1", 
            fg="#2c3e50",
            font=("Microsoft YaHei", 10),
            relief=tk.FLAT,
            bd=5,
            state=tk.DISABLED
        )
        report_text.pack(fill=tk.X, padx=15, pady=15)
        
        # 显示工作汇报内容
        report_text.config(state=tk.NORMAL)
        report_text.insert(tk.END, self.work_summary or "本次对话中完成的工作内容...")
        report_text.config(state=tk.DISABLED)
        
        # 2. 用户反馈文本区域
        feedback_frame = tk.LabelFrame(
            main_frame, 
            text="💬 您的文字反馈（可选）", 
            font=("Microsoft YaHei", 12, "bold"),
            bg="#ffffff",
            fg="#34495e",
            relief=tk.RAISED,
            bd=2
        )
        feedback_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        # 文本输入框
        self.text_widget = scrolledtext.ScrolledText(
            feedback_frame, 
            height=6, 
            wrap=tk.WORD,
            font=("Microsoft YaHei", 10),
            bg="#ffffff",
            fg="#2c3e50",
            relief=tk.FLAT,
            bd=5,
            insertbackground="#3498db"
        )
        self.text_widget.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        self.text_widget.insert(tk.END, "请在此输入您的反馈、建议或问题...")
        self.text_widget.bind("<FocusIn>", self.clear_placeholder)
        
        # 3. 图片选择区域
        image_frame = tk.LabelFrame(
            main_frame, 
            text="🖼️ 图片反馈（可选，支持多张）", 
            font=("Microsoft YaHei", 12, "bold"),
            bg="#ffffff",
            fg="#34495e",
            relief=tk.RAISED,
            bd=2
        )
        image_frame.pack(fill=tk.X, pady=(0, 15))
        
        # 图片操作按钮
        btn_frame = tk.Frame(image_frame, bg="#ffffff")
        btn_frame.pack(fill=tk.X, padx=15, pady=10)
        
        # 美化的按钮样式
        btn_style = {
            "font": ("Microsoft YaHei", 10, "bold"),
            "relief": tk.FLAT,
            "bd": 0,
            "cursor": "hand2",
            "height": 2
        }
        
        tk.Button(
            btn_frame,
            text="📁 选择图片文件",
            command=self.select_image_file,
            bg="#3498db",
            fg="white",
            width=15,
            **btn_style
        ).pack(side=tk.LEFT, padx=(0, 8))
        
        tk.Button(
            btn_frame,
            text="📋 从剪贴板粘贴",
            command=self.paste_from_clipboard,
            bg="#2ecc71",
            fg="white",
            width=15,
            **btn_style
        ).pack(side=tk.LEFT, padx=4)
        
        tk.Button(
            btn_frame,
            text="❌ 清除所有图片",
            command=self.clear_all_images,
            bg="#e74c3c",
            fg="white",
            width=15,
            **btn_style
        ).pack(side=tk.LEFT, padx=8)
        
        # 图片预览区域（支持滚动）
        preview_container = tk.Frame(image_frame, bg="#ffffff")
        preview_container.pack(fill=tk.X, padx=15, pady=(0, 15))
        
        # 创建滚动画布
        canvas = tk.Canvas(preview_container, height=120, bg="#f8f9fa", relief=tk.SUNKEN, bd=1)
        scrollbar = tk.Scrollbar(preview_container, orient="horizontal", command=canvas.xview)
        self.image_preview_frame = tk.Frame(canvas, bg="#f8f9fa")
        
        self.image_preview_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.image_preview_frame, anchor="nw")
        canvas.configure(xscrollcommand=scrollbar.set)
        
        canvas.pack(side="top", fill="x")
        scrollbar.pack(side="bottom", fill="x")
        
        # 初始提示
        self.update_image_preview()
        
        # 4. 操作按钮
        button_frame = tk.Frame(main_frame, bg="#f5f5f5")
        button_frame.pack(fill=tk.X, pady=(15, 0))
        
        # 主要操作按钮
        submit_btn = tk.Button(
            button_frame,
            text="✅ 提交反馈",
            command=self.submit_feedback,
            font=("Microsoft YaHei", 12, "bold"),
            bg="#27ae60",
            fg="white",
            width=18,
            height=2,
            relief=tk.FLAT,
            bd=0,
            cursor="hand2"
        )
        submit_btn.pack(side=tk.LEFT, padx=(0, 15))
        
        cancel_btn = tk.Button(
            button_frame,
            text="❌ 取消",
            command=self.cancel,
            font=("Microsoft YaHei", 12),
            bg="#95a5a6",
            fg="white",
            width=18,
            height=2,
            relief=tk.FLAT,
            bd=0,
            cursor="hand2"
        )
        cancel_btn.pack(side=tk.LEFT)
        
        # 说明文字
        info_label = tk.Label(
            main_frame,
            text="💡 提示：您可以只提供文字反馈、只提供图片，或者两者都提供（支持多张图片）",
            font=("Microsoft YaHei", 9),
            fg="#7f8c8d",
            bg="#f5f5f5"
        )
        info_label.pack(pady=(15, 0))
        
    def clear_placeholder(self, event):
        """清除占位符文本"""
        if self.text_widget.get(1.0, tk.END).strip() == "请在此输入您的反馈、建议或问题...":
            self.text_widget.delete(1.0, tk.END)
            
    def select_image_file(self):
        """选择图片文件（支持多选）"""
        file_types = [
            ("图片文件", "*.png *.jpg *.jpeg *.gif *.bmp *.webp"),
            ("PNG文件", "*.png"),
            ("JPEG文件", "*.jpg *.jpeg"),
            ("所有文件", "*.*")
        ]
        
        file_paths = filedialog.askopenfilenames(
            title="选择图片文件（可多选）",
            filetypes=file_types
        )
        
        for file_path in file_paths:
            try:
                # 读取并验证图片
                with open(file_path, 'rb') as f:
                    image_data = f.read()
                
                img = Image.open(io.BytesIO(image_data))
                self.selected_images.append({
                    'data': image_data,
                    'source': f'文件: {Path(file_path).name}',
                    'size': img.size,
                    'image': img
                })
                
            except Exception as e:
                messagebox.showerror("错误", f"无法读取图片文件 {Path(file_path).name}: {str(e)}")
                
        self.update_image_preview()
                
    def paste_from_clipboard(self):
        """从剪贴板粘贴图片"""
        try:
            from PIL import ImageGrab
            img = ImageGrab.grabclipboard()
            
            if img:
                buffer = io.BytesIO()
                img.save(buffer, format='PNG')
                image_data = buffer.getvalue()
                
                self.selected_images.append({
                    'data': image_data,
                    'source': '剪贴板',
                    'size': img.size,
                    'image': img
                })
                
                self.update_image_preview()
            else:
                messagebox.showwarning("警告", "剪贴板中没有图片数据")
                
        except Exception as e:
            messagebox.showerror("错误", f"无法从剪贴板获取图片: {str(e)}")
            
    def clear_all_images(self):
        """清除所有选择的图片"""
        self.selected_images = []
        self.update_image_preview()
        
    def update_image_preview(self):
        """更新图片预览显示"""
        # 清除现有预览
        for widget in self.image_preview_frame.winfo_children():
            widget.destroy()
            
        if not self.selected_images:
            # 显示未选择图片的提示
            no_image_label = tk.Label(
                self.image_preview_frame,
                text="未选择图片",
                bg="#f8f9fa",
                fg="#95a5a6",
                font=("Microsoft YaHei", 10)
            )
            no_image_label.pack(pady=20)
        else:
            # 显示所有图片预览
            for i, img_info in enumerate(self.selected_images):
                try:
                    # 创建单个图片预览容器
                    img_container = tk.Frame(self.image_preview_frame, bg="#ffffff", relief=tk.RAISED, bd=1)
                    img_container.pack(side=tk.LEFT, padx=5, pady=5)
                    
                    # 创建缩略图
                    img_copy = img_info['image'].copy()
                    img_copy.thumbnail((100, 80), Image.Resampling.LANCZOS)
                    
                    # 转换为tkinter可用的格式
                    photo = ImageTk.PhotoImage(img_copy)
                    
                    # 图片标签
                    img_label = tk.Label(img_container, image=photo, bg="#ffffff")
                    img_label.image = photo  # 保持引用
                    img_label.pack(padx=5, pady=5)
                    
                    # 图片信息
                    info_text = f"{img_info['source']}\n{img_info['size'][0]}x{img_info['size'][1]}"
                    info_label = tk.Label(
                        img_container,
                        text=info_text,
                        font=("Microsoft YaHei", 8),
                        bg="#ffffff",
                        fg="#7f8c8d"
                    )
                    info_label.pack(pady=(0, 5))
                    
                    # 删除按钮
                    del_btn = tk.Button(
                        img_container,
                        text="×",
                        command=lambda idx=i: self.remove_image(idx),
                        font=("Arial", 10, "bold"),
                        bg="#e74c3c",
                        fg="white",
                        width=3,
                        relief=tk.FLAT,
                        cursor="hand2"
                    )
                    del_btn.pack(pady=(0, 5))
                    
                except Exception as e:
                    print(f"预览更新失败: {e}")
                    
    def remove_image(self, index):
        """删除指定索引的图片"""
        if 0 <= index < len(self.selected_images):
            self.selected_images.pop(index)
            self.update_image_preview()
            
    def submit_feedback(self):
        """提交反馈"""
        # 获取文本内容
        text_content = self.text_widget.get(1.0, tk.END).strip()
        if text_content == "请在此输入您的反馈、建议或问题...":
            text_content = ""
            
        # 检查是否有内容
        has_text = bool(text_content)
        has_images = bool(self.selected_images)
        
        if not has_text and not has_images:
            messagebox.showwarning("警告", "请至少提供文字反馈或图片反馈")
            return
            
        # 准备结果数据
        result = {
            'success': True,
            'text_feedback': text_content if has_text else None,
            'images': [img['data'] for img in self.selected_images] if has_images else None,
            'image_sources': [img['source'] for img in self.selected_images] if has_images else None,
            'has_text': has_text,
            'has_images': has_images,
            'image_count': len(self.selected_images),
            'timestamp': datetime.now().isoformat()
        }
        
        self.result_queue.put(result)
        self.root.destroy()
        
    def cancel(self):
        """取消操作"""
        self.result_queue.put({
            'success': False,
            'message': '用户取消了反馈提交'
        })
        self.root.destroy()


@mcp.tool()
def collect_feedback(work_summary: str = "", timeout_seconds: int = DIALOG_TIMEOUT) -> list:
    """
    收集用户反馈的交互式工具。AI可以汇报完成的工作，用户可以提供文字和/或图片反馈。
    
    Args:
        work_summary: AI完成的工作内容汇报
        timeout_seconds: 对话框超时时间（秒），默认300秒（5分钟）
        
    Returns:
        包含用户反馈内容的列表，可能包含文本和图片
    """
    dialog = FeedbackDialog(work_summary, timeout_seconds)
    result = dialog.show_dialog()
    
    if result is None:
        raise Exception(f"操作超时（{timeout_seconds}秒），请重试")
        
    if not result['success']:
        raise Exception(result.get('message', '用户取消了反馈提交'))
    
    # 构建返回内容列表
    feedback_items = []
    
    # 添加文字反馈
    if result['has_text']:
        from mcp.types import TextContent
        feedback_items.append(TextContent(
            type="text", 
            text=f"用户文字反馈：{result['text_feedback']}\n提交时间：{result['timestamp']}"
        ))
        
    # 添加图片反馈
    if result['has_images']:
        for image_data, source in zip(result['images'], result['image_sources']):
            feedback_items.append(MCPImage(data=image_data, format='png'))
        
    return feedback_items


@mcp.tool()
def pick_image() -> MCPImage:
    """
    弹出图片选择对话框，让用户选择图片文件或从剪贴板粘贴图片。
    用户可以选择本地图片文件，或者先截图到剪贴板然后粘贴。
    """
    # 使用简化的对话框只选择图片
    dialog = FeedbackDialog()
    dialog.work_summary = "请选择一张图片"
    
    # 创建简化版本的图片选择对话框
    def simple_image_dialog():
        root = tk.Tk()
        root.title("选择图片")
        root.geometry("400x300")
        root.resizable(False, False)
        root.eval('tk::PlaceWindow . center')
        
        selected_image = {'data': None}
        
        def select_file():
            file_path = filedialog.askopenfilename(
                title="选择图片文件",
                filetypes=[("图片文件", "*.png *.jpg *.jpeg *.gif *.bmp *.webp")]
            )
            if file_path:
                try:
                    with open(file_path, 'rb') as f:
                        selected_image['data'] = f.read()
                    root.destroy()
                except Exception as e:
                    messagebox.showerror("错误", f"无法读取图片: {e}")
                    
        def paste_clipboard():
            try:
                from PIL import ImageGrab
                img = ImageGrab.grabclipboard()
                if img:
                    buffer = io.BytesIO()
                    img.save(buffer, format='PNG')
                    selected_image['data'] = buffer.getvalue()
                    root.destroy()
                else:
                    messagebox.showwarning("警告", "剪贴板中没有图片")
            except Exception as e:
                messagebox.showerror("错误", f"剪贴板操作失败: {e}")
                
        def cancel():
            root.destroy()
            
        # 界面
        tk.Label(root, text="请选择图片来源", font=("Arial", 14, "bold")).pack(pady=20)
        
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="📁 选择图片文件", font=("Arial", 12), 
                 width=20, height=2, command=select_file).pack(pady=10)
        tk.Button(btn_frame, text="📋 从剪贴板粘贴", font=("Arial", 12), 
                 width=20, height=2, command=paste_clipboard).pack(pady=10)
        tk.Button(btn_frame, text="❌ 取消", font=("Arial", 12), 
                 width=20, height=1, command=cancel).pack(pady=10)
        
        root.mainloop()
        return selected_image['data']
    
    image_data = simple_image_dialog()
    
    if image_data is None:
        raise Exception("未选择图片或操作被取消")
        
    return MCPImage(data=image_data, format='png')


@mcp.tool()
def get_image_info(image_path: str) -> str:
    """
    获取指定路径图片的信息（尺寸、格式等）
    
    Args:
        image_path: 图片文件路径
    """
    try:
        path = Path(image_path)
        if not path.exists():
            return f"文件不存在: {image_path}"
            
        with Image.open(path) as img:
            info = {
                "文件名": path.name,
                "格式": img.format,
                "尺寸": f"{img.width} x {img.height}",
                "模式": img.mode,
                "文件大小": f"{path.stat().st_size / 1024:.1f} KB"
            }
            
        return "\n".join([f"{k}: {v}" for k, v in info.items()])
        
    except Exception as e:
        return f"获取图片信息失败: {str(e)}"


if __name__ == "__main__":
    mcp.run()


def main():
    """Main entry point for the mcp-feedback-collector command."""
    mcp.run() 