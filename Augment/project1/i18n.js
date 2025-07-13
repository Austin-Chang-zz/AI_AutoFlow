// 多語言翻譯配置
const translations = {
    zh: {
        // 導航欄
        nav: {
            home: "首頁",
            features: "功能特色",
            pricing: "價格方案",
            comparison: "產品對比",
            testimonials: "用戶評價"
        },
        // 主標題區域
        hero: {
            title1: "更好的上下文，更好的智能體",
            title2: "更好的代碼",
            subtitle: "業界領先的上下文引擎支持的最強大AI軟件開發平台"
        },
        // 按鈕
        buttons: {
            install: "立即安裝",
            learn_more: "了解更多",
            free_trial: "14天免費試用",
            contact_sales: "聯繫銷售",
            get_started: "免費開始",
            view_pricing: "查看價格"
        },
        // 統計數據
        stats: {
            developers: "開發者信賴",
            champion: "冠軍",
            trial: "免費試用",
            rating: "用戶評分",
            recommendation: "推薦率",
            efficiency: "效率提升",
            active_developers: "活躍開發者"
        },
        // 區域標題
        sections: {
            explore: "探索 Augment Code",
            explore_subtitle: "了解為什麼全球50,000+開發者選擇我們",
            features_title: "為軟件工程師而生",
            features_subtitle: "從自主編程智能體到精確的代碼庫感知自動完成，AI助力您快速完成任何項目",
            pricing_title: "簡單定價",
            pricing_subtitle: "為重要功能付費，享受其他一切",
            comparison_title: "Augment Code vs 競爭對手",
            comparison_subtitle: "了解為什麼Augment Code是最佳選擇",
            testimonials_title: "用戶怎麼說",
            testimonials_subtitle: "來自全球開發者的真實反饋"
        },
        // 功能特色
        features: {
            context_engine: "上下文引擎",
            context_desc: "業界領先的上下文引擎和自主智能體",
            autonomous_agent: "自主智能體",
            agent_desc: "本地或遠程智能體端到端完成任務，可以規劃、構建並為您開啟PR",
            smart_apply: "智能應用",
            apply_desc: "一鍵智能應用聊天建議到您的代碼",
            terminal_integration: "終端集成",
            terminal_desc: "智能體可以在您的終端中運行命令——需要批准或自動運行",
            mcp_support: "MCP支持",
            mcp_desc: "引入額外上下文並與100+外部工具協作",
            security: "安全隱私",
            security_desc: "您的代碼默認安全且私密"
        },
        // 價格方案
        pricing: {
            community: "Community",
            developer: "Developer",
            pro: "Pro",
            max: "Max",
            enterprise: "Enterprise",
            free: "免費",
            month: "/月",
            custom: "定制",
            popular: "最受歡迎",
            community_desc: "開始使用基本功能的完美選擇",
            developer_desc: "適合想要快速發布到生產環境的個人或小團隊",
            pro_desc: "適合需要增強容量和支持的成長團隊",
            max_desc: "為高需求團隊或企業設計的密集使用方案",
            enterprise_desc: "適合有高容量、安全或支持需求的企業團隊"
        },
        // 頁腳
        footer: {
            description: "業界領先的AI軟件開發平台，讓每一次按鍵都更有價值。",
            navigation: "頁面導航",
            resources: "資源",
            company: "公司",
            docs: "文檔",
            blog: "博客",
            changelog: "更新日誌",
            status: "狀態頁面",
            careers: "職業機會",
            contact_sales: "聯繫銷售",
            contact_support: "聯繫支持",
            copyright: "保留所有權利。"
        }
    },
    en: {
        // Navigation
        nav: {
            home: "Home",
            features: "Features",
            pricing: "Pricing",
            comparison: "Comparison",
            testimonials: "Testimonials"
        },
        // Hero section
        hero: {
            title1: "Better context, better agents",
            title2: "Better code",
            subtitle: "The most powerful AI software development platform powered by the industry's leading context engine"
        },
        // Buttons
        buttons: {
            install: "Install Now",
            learn_more: "Learn More",
            free_trial: "14-Day Free Trial",
            contact_sales: "Contact Sales",
            get_started: "Get Started Free",
            view_pricing: "View Pricing"
        },
        // Statistics
        stats: {
            developers: "Developers Trust",
            champion: "Champion",
            trial: "Free Trial",
            rating: "User Rating",
            recommendation: "Recommendation Rate",
            efficiency: "Efficiency Boost",
            active_developers: "Active Developers"
        },
        // Section titles
        sections: {
            explore: "Explore Augment Code",
            explore_subtitle: "Discover why 50,000+ developers worldwide choose us",
            features_title: "Built for Software Engineers",
            features_subtitle: "From autonomous coding agents to precise codebase-aware autocomplete, AI helps you ship any project fast",
            pricing_title: "Simple Pricing",
            pricing_subtitle: "Pay for what matters, enjoy everything else",
            comparison_title: "Augment Code vs Competitors",
            comparison_subtitle: "Learn why Augment Code is the best choice",
            testimonials_title: "What Users Say",
            testimonials_subtitle: "Real feedback from developers worldwide"
        },
        // Features
        features: {
            context_engine: "Context Engine",
            context_desc: "Industry-leading context engine and autonomous agents",
            autonomous_agent: "Autonomous Agents",
            agent_desc: "Local or remote agents complete tasks end-to-end, can plan, build, and open PRs for you",
            smart_apply: "Smart Apply",
            apply_desc: "One-click smart apply chat suggestions to your code",
            terminal_integration: "Terminal Integration",
            terminal_desc: "Agents can run commands in your terminal—with approval or automatically",
            mcp_support: "MCP Support",
            mcp_desc: "Bring in additional context and collaborate with 100+ external tools",
            security: "Security & Privacy",
            security_desc: "Your code is secure and private by default"
        },
        // Pricing
        pricing: {
            community: "Community",
            developer: "Developer",
            pro: "Pro",
            max: "Max",
            enterprise: "Enterprise",
            free: "Free",
            month: "/month",
            custom: "Custom",
            popular: "Most Popular",
            community_desc: "Perfect for getting started with basic features",
            developer_desc: "For individuals or small teams who want to ship to production fast",
            pro_desc: "For growing teams that need enhanced capacity and support",
            max_desc: "Designed for high-demand teams or enterprises with intensive usage",
            enterprise_desc: "For enterprise teams with high-volume, security, or support needs"
        },
        // Footer
        footer: {
            description: "The industry's leading AI software development platform that makes every keystroke count.",
            navigation: "Navigation",
            resources: "Resources",
            company: "Company",
            docs: "Documentation",
            blog: "Blog",
            changelog: "Changelog",
            status: "Status Page",
            careers: "Careers",
            contact_sales: "Contact Sales",
            contact_support: "Contact Support",
            copyright: "All rights reserved."
        }
    },
    ja: {
        // ナビゲーション
        nav: {
            home: "ホーム",
            features: "機能",
            pricing: "料金",
            comparison: "比較",
            testimonials: "お客様の声"
        },
        // ヒーローセクション
        hero: {
            title1: "より良いコンテキスト、より良いエージェント",
            title2: "より良いコード",
            subtitle: "業界最先端のコンテキストエンジンを搭載した最強のAIソフトウェア開発プラットフォーム"
        },
        // ボタン
        buttons: {
            install: "今すぐインストール",
            learn_more: "詳細を見る",
            free_trial: "14日間無料トライアル",
            contact_sales: "営業に問い合わせ",
            get_started: "無料で始める",
            view_pricing: "料金を見る"
        },
        // 統計
        stats: {
            developers: "開発者が信頼",
            champion: "チャンピオン",
            trial: "無料トライアル",
            rating: "ユーザー評価",
            recommendation: "推奨率",
            efficiency: "効率向上",
            active_developers: "アクティブ開発者"
        },
        // セクションタイトル
        sections: {
            explore: "Augment Codeを探索",
            explore_subtitle: "世界中の50,000+の開発者が選ぶ理由を発見",
            features_title: "ソフトウェアエンジニアのために構築",
            features_subtitle: "自律的なコーディングエージェントから精密なコードベース対応オートコンプリートまで、AIがあらゆるプロジェクトの高速配信を支援",
            pricing_title: "シンプルな料金体系",
            pricing_subtitle: "重要な機能にお支払いいただき、その他すべてをお楽しみください",
            comparison_title: "Augment Code vs 競合他社",
            comparison_subtitle: "Augment Codeが最良の選択である理由を学ぶ",
            testimonials_title: "ユーザーの声",
            testimonials_subtitle: "世界中の開発者からの実際のフィードバック"
        },
        // 機能
        features: {
            context_engine: "コンテキストエンジン",
            context_desc: "業界最先端のコンテキストエンジンと自律エージェント",
            autonomous_agent: "自律エージェント",
            agent_desc: "ローカルまたはリモートエージェントがタスクをエンドツーエンドで完了、計画、構築、PRの作成が可能",
            smart_apply: "スマート適用",
            apply_desc: "チャット提案をコードにワンクリックでスマート適用",
            terminal_integration: "ターミナル統合",
            terminal_desc: "エージェントがターミナルでコマンドを実行—承認付きまたは自動で",
            mcp_support: "MCPサポート",
            mcp_desc: "追加のコンテキストを取り込み、100+の外部ツールと連携",
            security: "セキュリティとプライバシー",
            security_desc: "コードはデフォルトで安全かつプライベート"
        },
        // 料金
        pricing: {
            community: "コミュニティ",
            developer: "デベロッパー",
            pro: "プロ",
            max: "マックス",
            enterprise: "エンタープライズ",
            free: "無料",
            month: "/月",
            custom: "カスタム",
            popular: "最も人気",
            community_desc: "基本機能で始めるのに最適",
            developer_desc: "本番環境への高速配信を望む個人または小チーム向け",
            pro_desc: "強化された容量とサポートが必要な成長チーム向け",
            max_desc: "集約的な使用を行う高需要チームまたは企業向けに設計",
            enterprise_desc: "大容量、セキュリティ、またはサポートニーズを持つ企業チーム向け"
        },
        // フッター
        footer: {
            description: "すべてのキーストロークを価値あるものにする業界最先端のAIソフトウェア開発プラットフォーム。",
            navigation: "ナビゲーション",
            resources: "リソース",
            company: "会社",
            docs: "ドキュメント",
            blog: "ブログ",
            changelog: "変更履歴",
            status: "ステータスページ",
            careers: "採用情報",
            contact_sales: "営業に問い合わせ",
            contact_support: "サポートに問い合わせ",
            copyright: "全著作権所有。"
        }
    },
    ko: {
        // 내비게이션
        nav: {
            home: "홈",
            features: "기능",
            pricing: "가격",
            comparison: "비교",
            testimonials: "사용자 후기"
        },
        // 히어로 섹션
        hero: {
            title1: "더 나은 컨텍스트, 더 나은 에이전트",
            title2: "더 나은 코드",
            subtitle: "업계 최고의 컨텍스트 엔진으로 구동되는 가장 강력한 AI 소프트웨어 개발 플랫폼"
        },
        // 버튼
        buttons: {
            install: "지금 설치",
            learn_more: "자세히 알아보기",
            free_trial: "14일 무료 체험",
            contact_sales: "영업팀 문의",
            get_started: "무료로 시작",
            view_pricing: "가격 보기"
        },
        // 통계
        stats: {
            developers: "개발자 신뢰",
            champion: "챔피언",
            trial: "무료 체험",
            rating: "사용자 평점",
            recommendation: "추천율",
            efficiency: "효율성 향상",
            active_developers: "활성 개발자"
        },
        // 섹션 제목
        sections: {
            explore: "Augment Code 탐색",
            explore_subtitle: "전 세계 50,000+ 개발자가 선택하는 이유를 알아보세요",
            features_title: "소프트웨어 엔지니어를 위해 구축",
            features_subtitle: "자율적인 코딩 에이전트부터 정밀한 코드베이스 인식 자동완성까지, AI가 모든 프로젝트의 빠른 배포를 도와줍니다",
            pricing_title: "간단한 가격",
            pricing_subtitle: "중요한 기능에 대해서만 지불하고 나머지는 모두 즐기세요",
            comparison_title: "Augment Code vs 경쟁사",
            comparison_subtitle: "Augment Code가 최고의 선택인 이유를 알아보세요",
            testimonials_title: "사용자 후기",
            testimonials_subtitle: "전 세계 개발자들의 실제 피드백"
        },
        // 기능
        features: {
            context_engine: "컨텍스트 엔진",
            context_desc: "업계 최고의 컨텍스트 엔진과 자율 에이전트",
            autonomous_agent: "자율 에이전트",
            agent_desc: "로컬 또는 원격 에이전트가 작업을 엔드투엔드로 완료하고, 계획하고, 구축하고, PR을 열어줍니다",
            smart_apply: "스마트 적용",
            apply_desc: "채팅 제안을 코드에 원클릭으로 스마트 적용",
            terminal_integration: "터미널 통합",
            terminal_desc: "에이전트가 터미널에서 명령을 실행할 수 있습니다—승인 후 또는 자동으로",
            mcp_support: "MCP 지원",
            mcp_desc: "추가 컨텍스트를 가져오고 100+ 외부 도구와 협업",
            security: "보안 및 개인정보",
            security_desc: "코드는 기본적으로 안전하고 비공개입니다"
        },
        // 가격
        pricing: {
            community: "커뮤니티",
            developer: "개발자",
            pro: "프로",
            max: "맥스",
            enterprise: "엔터프라이즈",
            free: "무료",
            month: "/월",
            custom: "맞춤형",
            popular: "가장 인기",
            community_desc: "기본 기능으로 시작하기에 완벽",
            developer_desc: "빠른 프로덕션 배포를 원하는 개인 또는 소규모 팀용",
            pro_desc: "향상된 용량과 지원이 필요한 성장하는 팀용",
            max_desc: "집약적인 사용을 하는 고수요 팀 또는 기업용으로 설계",
            enterprise_desc: "대용량, 보안 또는 지원 요구사항이 있는 기업 팀용"
        },
        // 푸터
        footer: {
            description: "모든 키 입력을 가치 있게 만드는 업계 최고의 AI 소프트웨어 개발 플랫폼.",
            navigation: "내비게이션",
            resources: "리소스",
            company: "회사",
            docs: "문서",
            blog: "블로그",
            changelog: "변경 로그",
            status: "상태 페이지",
            careers: "채용",
            contact_sales: "영업팀 문의",
            contact_support: "지원팀 문의",
            copyright: "모든 권리 보유."
        }
    },
    es: {
        // Navegación
        nav: {
            home: "Inicio",
            features: "Características",
            pricing: "Precios",
            comparison: "Comparación",
            testimonials: "Testimonios"
        },
        // Sección hero
        hero: {
            title1: "Mejor contexto, mejores agentes",
            title2: "Mejor código",
            subtitle: "La plataforma de desarrollo de software con IA más poderosa impulsada por el motor de contexto líder de la industria"
        },
        // Botones
        buttons: {
            install: "Instalar Ahora",
            learn_more: "Saber Más",
            free_trial: "Prueba Gratuita de 14 Días",
            contact_sales: "Contactar Ventas",
            get_started: "Comenzar Gratis",
            view_pricing: "Ver Precios"
        },
        // Estadísticas
        stats: {
            developers: "Desarrolladores Confían",
            champion: "Campeón",
            trial: "Prueba Gratuita",
            rating: "Calificación de Usuario",
            recommendation: "Tasa de Recomendación",
            efficiency: "Aumento de Eficiencia",
            active_developers: "Desarrolladores Activos"
        },
        // Títulos de sección
        sections: {
            explore: "Explorar Augment Code",
            explore_subtitle: "Descubre por qué más de 50,000 desarrolladores en todo el mundo nos eligen",
            features_title: "Construido para Ingenieros de Software",
            features_subtitle: "Desde agentes de codificación autónomos hasta autocompletado preciso consciente del código base, la IA te ayuda a enviar cualquier proyecto rápidamente",
            pricing_title: "Precios Simples",
            pricing_subtitle: "Paga por lo que importa, disfruta todo lo demás",
            comparison_title: "Augment Code vs Competidores",
            comparison_subtitle: "Aprende por qué Augment Code es la mejor opción",
            testimonials_title: "Lo Que Dicen Los Usuarios",
            testimonials_subtitle: "Comentarios reales de desarrolladores de todo el mundo"
        },
        // Características
        features: {
            context_engine: "Motor de Contexto",
            context_desc: "Motor de contexto líder de la industria y agentes autónomos",
            autonomous_agent: "Agentes Autónomos",
            agent_desc: "Agentes locales o remotos completan tareas de extremo a extremo, pueden planificar, construir y abrir PRs para ti",
            smart_apply: "Aplicación Inteligente",
            apply_desc: "Aplicación inteligente de un clic de sugerencias de chat a tu código",
            terminal_integration: "Integración de Terminal",
            terminal_desc: "Los agentes pueden ejecutar comandos en tu terminal—con aprobación o automáticamente",
            mcp_support: "Soporte MCP",
            mcp_desc: "Trae contexto adicional y colabora con más de 100 herramientas externas",
            security: "Seguridad y Privacidad",
            security_desc: "Tu código es seguro y privado por defecto"
        },
        // Precios
        pricing: {
            community: "Comunidad",
            developer: "Desarrollador",
            pro: "Pro",
            max: "Máximo",
            enterprise: "Empresa",
            free: "Gratis",
            month: "/mes",
            custom: "Personalizado",
            popular: "Más Popular",
            community_desc: "Perfecto para comenzar con características básicas",
            developer_desc: "Para individuos o equipos pequeños que quieren enviar a producción rápido",
            pro_desc: "Para equipos en crecimiento que necesitan capacidad mejorada y soporte",
            max_desc: "Diseñado para equipos de alta demanda o empresas con uso intensivo",
            enterprise_desc: "Para equipos empresariales con necesidades de alto volumen, seguridad o soporte"
        },
        // Pie de página
        footer: {
            description: "La plataforma de desarrollo de software con IA líder de la industria que hace que cada pulsación de tecla cuente.",
            navigation: "Navegación",
            resources: "Recursos",
            company: "Empresa",
            docs: "Documentación",
            blog: "Blog",
            changelog: "Registro de Cambios",
            status: "Página de Estado",
            careers: "Carreras",
            contact_sales: "Contactar Ventas",
            contact_support: "Contactar Soporte",
            copyright: "Todos los derechos reservados."
        }
    }
};

// 語言管理類
class LanguageManager {
    constructor() {
        this.currentLanguage = localStorage.getItem('language') || 'zh';
        this.init();
    }

    init() {
        this.setupLanguageSelector();
        this.translatePage();
        this.updateLanguageDisplay();
    }

    setupLanguageSelector() {
        const languageBtn = document.getElementById('languageBtn');
        const languageOptions = document.getElementById('languageOptions');

        if (languageBtn && languageOptions) {
            // 切換下拉菜單
            languageBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                languageOptions.classList.toggle('show');
            });

            // 點擊外部關閉下拉菜單
            document.addEventListener('click', () => {
                languageOptions.classList.remove('show');
            });

            // 語言選項點擊事件
            languageOptions.addEventListener('click', (e) => {
                const option = e.target.closest('.language-option');
                if (option) {
                    const lang = option.dataset.lang;
                    this.changeLanguage(lang);
                    languageOptions.classList.remove('show');
                }
            });
        }
    }

    changeLanguage(lang) {
        this.currentLanguage = lang;
        localStorage.setItem('language', lang);
        this.translatePage();
        this.updateLanguageDisplay();
    }

    translatePage() {
        const elements = document.querySelectorAll('[data-i18n]');
        elements.forEach(element => {
            const key = element.getAttribute('data-i18n');
            const translation = this.getTranslation(key);
            if (translation) {
                element.textContent = translation;
            }
        });
    }

    getTranslation(key) {
        const keys = key.split('.');
        let translation = translations[this.currentLanguage];

        for (const k of keys) {
            if (translation && translation[k]) {
                translation = translation[k];
            } else {
                return null;
            }
        }

        return translation;
    }

    updateLanguageDisplay() {
        const currentLangElement = document.getElementById('currentLang');
        const languageNames = {
            zh: '中文',
            en: 'English',
            ja: '日本語',
            ko: '한국어',
            es: 'Español'
        };

        if (currentLangElement) {
            currentLangElement.textContent = languageNames[this.currentLanguage];
        }

        // 更新選中狀態
        const options = document.querySelectorAll('.language-option');
        options.forEach(option => {
            option.classList.remove('selected');
            if (option.dataset.lang === this.currentLanguage) {
                option.classList.add('selected');
            }
        });
    }

    getCurrentLanguage() {
        return this.currentLanguage;
    }
}

// 初始化語言管理器
let languageManager;
document.addEventListener('DOMContentLoaded', () => {
    languageManager = new LanguageManager();
});

// 導出供其他頁面使用
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { translations, LanguageManager };
}
