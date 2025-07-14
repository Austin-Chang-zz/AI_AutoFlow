// 平滑滾動
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// 導航欄滾動效果
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 100) {
        navbar.style.background = 'rgba(10, 10, 10, 0.98)';
    } else {
        navbar.style.background = 'rgba(10, 10, 10, 0.95)';
    }
});

// 代碼打字效果
const codeLines = [
    '// AI智能體正在為您編寫代碼...',
    'function generateOptimizedCode() {',
    '  return "完美的生產級代碼";',
    '}'
];

let currentLine = 0;
let currentChar = 0;

function typeCode() {
    const codeElements = document.querySelectorAll('.code-text');
    
    if (currentLine < codeLines.length && codeElements[currentLine]) {
        const line = codeLines[currentLine];
        const element = codeElements[currentLine];
        
        if (currentChar < line.length) {
            element.innerHTML = line.substring(0, currentChar + 1);
            currentChar++;
            setTimeout(typeCode, 50);
        } else {
            currentLine++;
            currentChar = 0;
            setTimeout(typeCode, 500);
        }
    } else {
        // 重置動畫
        setTimeout(() => {
            currentLine = 0;
            currentChar = 0;
            document.querySelectorAll('.code-text').forEach(el => el.innerHTML = '');
            typeCode();
        }, 3000);
    }
}

// 頁面載入後開始打字效果
window.addEventListener('load', () => {
    setTimeout(typeCode, 1000);
});

// 卡片懸停效果
document.querySelectorAll('.feature-card, .pricing-card').forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-10px)';
    });
    
    card.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0)';
    });
});

// 滾動動畫
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// 為所有需要動畫的元素添加觀察者
document.addEventListener('DOMContentLoaded', () => {
    const animatedElements = document.querySelectorAll('.feature-card, .pricing-card, .section-header');
    
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
});

// 粒子背景效果
function createParticles() {
    const hero = document.querySelector('.hero');
    const particleCount = 50;
    
    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.cssText = `
            position: absolute;
            width: 2px;
            height: 2px;
            background: rgba(99, 102, 241, 0.3);
            border-radius: 50%;
            pointer-events: none;
            left: ${Math.random() * 100}%;
            top: ${Math.random() * 100}%;
            animation: float ${3 + Math.random() * 4}s ease-in-out infinite;
            animation-delay: ${Math.random() * 2}s;
        `;
        hero.appendChild(particle);
    }
}

// 添加CSS動畫
const style = document.createElement('style');
style.textContent = `
    @keyframes float {
        0%, 100% {
            transform: translateY(0px) rotate(0deg);
            opacity: 0.3;
        }
        50% {
            transform: translateY(-20px) rotate(180deg);
            opacity: 0.8;
        }
    }
    
    .particle {
        animation: float 6s ease-in-out infinite;
    }
`;
document.head.appendChild(style);

// 初始化粒子效果
window.addEventListener('load', createParticles);

// 按鈕點擊效果
document.querySelectorAll('.btn').forEach(btn => {
    btn.addEventListener('click', function(e) {
        // 創建漣漪效果
        const ripple = document.createElement('span');
        const rect = this.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = e.clientX - rect.left - size / 2;
        const y = e.clientY - rect.top - size / 2;
        
        ripple.style.cssText = `
            position: absolute;
            width: ${size}px;
            height: ${size}px;
            left: ${x}px;
            top: ${y}px;
            background: rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            transform: scale(0);
            animation: ripple 0.6s linear;
            pointer-events: none;
        `;
        
        this.style.position = 'relative';
        this.style.overflow = 'hidden';
        this.appendChild(ripple);
        
        setTimeout(() => {
            ripple.remove();
        }, 600);
    });
});

// 添加漣漪動畫
const rippleStyle = document.createElement('style');
rippleStyle.textContent = `
    @keyframes ripple {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
`;
document.head.appendChild(rippleStyle);

// 統計數字動畫
function animateNumbers() {
    const stats = document.querySelectorAll('.stat-number');
    
    stats.forEach(stat => {
        const text = stat.textContent;
        if (text.includes('50K+')) {
            animateNumber(stat, 0, 50000, 2000, (num) => Math.floor(num / 1000) + 'K+');
        }
    });
}

function animateNumber(element, start, end, duration, formatter) {
    const startTime = performance.now();
    
    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const current = start + (end - start) * easeOutQuart(progress);
        
        element.textContent = formatter ? formatter(current) : Math.floor(current);
        
        if (progress < 1) {
            requestAnimationFrame(update);
        }
    }
    
    requestAnimationFrame(update);
}

function easeOutQuart(t) {
    return 1 - Math.pow(1 - t, 4);
}

// 當統計區域進入視窗時開始動畫
const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            animateNumbers();
            statsObserver.unobserve(entry.target);
        }
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const heroStats = document.querySelector('.hero-stats');
    if (heroStats) {
        statsObserver.observe(heroStats);
    }
});
