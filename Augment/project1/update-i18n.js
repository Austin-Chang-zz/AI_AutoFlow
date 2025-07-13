// 為所有頁面添加多語言支持的腳本
const fs = require('fs');
const path = require('path');

// 語言選擇器HTML
const languageSelector = `            <div class="language-selector">
                <div class="language-dropdown">
                    <button class="language-btn" id="languageBtn">
                        <i class="fas fa-globe"></i>
                        <span id="currentLang">中文</span>
                        <i class="fas fa-chevron-down"></i>
                    </button>
                    <div class="language-options" id="languageOptions">
                        <div class="language-option" data-lang="zh" data-flag="🇨🇳">
                            <span class="flag">🇨🇳</span>
                            <span>中文</span>
                        </div>
                        <div class="language-option" data-lang="en" data-flag="🇺🇸">
                            <span class="flag">🇺🇸</span>
                            <span>English</span>
                        </div>
                        <div class="language-option" data-lang="ja" data-flag="🇯🇵">
                            <span class="flag">🇯🇵</span>
                            <span>日本語</span>
                        </div>
                        <div class="language-option" data-lang="ko" data-flag="🇰🇷">
                            <span class="flag">🇰🇷</span>
                            <span>한국어</span>
                        </div>
                        <div class="language-option" data-lang="es" data-flag="🇪🇸">
                            <span class="flag">🇪🇸</span>
                            <span>Español</span>
                        </div>
                    </div>
                </div>
            </div>`;

// 需要更新的文件列表
const files = ['pricing.html', 'comparison.html', 'testimonials.html'];

// 導航欄更新映射
const navUpdates = {
    'pricing.html': 'pricing',
    'comparison.html': 'comparison', 
    'testimonials.html': 'testimonials'
};

// 為每個文件添加多語言支持
files.forEach(filename => {
    const filePath = path.join(__dirname, filename);
    
    if (fs.existsSync(filePath)) {
        let content = fs.readFileSync(filePath, 'utf8');
        
        // 1. 更新導航欄鏈接添加data-i18n屬性
        content = content.replace(
            /<a href="home\.html" class="nav-link"[^>]*>首頁<\/a>/,
            '<a href="home.html" class="nav-link" data-i18n="nav.home">首頁</a>'
        );
        content = content.replace(
            /<a href="features\.html" class="nav-link"[^>]*>功能特色<\/a>/,
            '<a href="features.html" class="nav-link" data-i18n="nav.features">功能特色</a>'
        );
        content = content.replace(
            /<a href="pricing\.html" class="nav-link[^"]*"[^>]*>價格方案<\/a>/,
            '<a href="pricing.html" class="nav-link' + (navUpdates[filename] === 'pricing' ? ' active' : '') + '" data-i18n="nav.pricing">價格方案</a>'
        );
        content = content.replace(
            /<a href="comparison\.html" class="nav-link[^"]*"[^>]*>產品對比<\/a>/,
            '<a href="comparison.html" class="nav-link' + (navUpdates[filename] === 'comparison' ? ' active' : '') + '" data-i18n="nav.comparison">產品對比</a>'
        );
        content = content.replace(
            /<a href="testimonials\.html" class="nav-link[^"]*"[^>]*>用戶評價<\/a>/,
            '<a href="testimonials.html" class="nav-link' + (navUpdates[filename] === 'testimonials' ? ' active' : '') + '" data-i18n="nav.testimonials">用戶評價</a>'
        );
        
        // 2. 在導航菜單後添加語言選擇器
        content = content.replace(
            /(<\/div>\s*<\/div>\s*<\/nav>)/,
            languageSelector + '\n        </div>\n    </nav>'
        );
        
        // 3. 在script標籤前添加i18n.js
        content = content.replace(
            /<script src="script\.js"><\/script>/,
            '<script src="i18n.js"></script>\n    <script src="script.js"></script>'
        );
        
        // 寫回文件
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`Updated ${filename} with i18n support`);
    }
});

console.log('All files updated successfully!');
