# 📋 Augment Code Rules & Guidelines - Complete User Guide

## 🎯 **Understanding Rules & Guidelines Features**

Augment Code provides two powerful ways to customize AI behavior: **Settings Page Rules** (global, long-term) and **Chat Dialog Rules** (local, temporary). Understanding when and how to use each is crucial for maximizing your productivity.

## 🔍 **Key Differences: Settings vs Chat Rules**

### **📋 Settings Page Rules (Global & Long-term)**
**Use for:** Project standards that remain stable for months/years

| ✅ **Should Include** | ❌ **Should NOT Include** |
|----------------------|---------------------------|
| Technology stack standards | Current task requirements |
| Code quality baselines | Temporary priority adjustments |
| Security requirements | Feature-specific details |
| Team collaboration standards | Context-specific limitations |
| AI response format preferences | Experimental approaches |

**Example Settings Page Rule:**
```markdown
# E-commerce Project Development Standards v1.0

## Technology Stack
- Frontend: React 18 + TypeScript + Tailwind CSS
- Backend: Node.js + Express + TypeScript
- Database: PostgreSQL + Redis
- Deployment: Docker + AWS

## Code Quality Requirements
1. All code must use TypeScript strict mode
2. Functions must have explicit type definitions
3. Test coverage must be >80%
4. All APIs must include error handling

## Security Standards
1. All user inputs must be validated
2. Sensitive data must be encrypted
3. APIs must include authentication
4. Follow OWASP security guidelines

## AI Response Standards
1. Provide complete code implementations
2. Include detailed comments
3. Provide usage examples and test cases
4. Explain potential security risks
```

### **💬 Chat Dialog Rules (Local & Temporary)**
**Use for:** Current task-specific requirements that change frequently

| ✅ **Should Include** | ❌ **Should NOT Include** |
|----------------------|---------------------------|
| Current task focus | Technology stack choices |
| Special requirements | Basic code quality standards |
| Temporary priorities | Long-term security policies |
| Context-specific constraints | Universal response formats |
| Experimental approaches | Team-wide standards |

**Example Chat Dialog Rule:**
```markdown
# Current Task: User Authentication Module

## Task Focus
- Implementing JWT authentication system
- Registration, login, password reset features
- Support for social media login (Google, Facebook)
- Multi-factor authentication (2FA)

## Special Requirements
1. Password encryption using bcrypt, salt rounds = 12
2. JWT tokens: access token 15min, refresh token 7 days
3. Lock account for 30min after 5 failed login attempts
4. Log all authentication-related operations

## Current Priorities
1. High: Basic registration/login functionality
2. Medium: Password reset, account verification
3. Low: Social media login, 2FA
```

## 🚀 **Step-by-Step Usage Guide**

### **Step 1: Set Up Global Rules (Settings Page)**

**When to do this:**
- At project start
- When technology stack is decided
- When team standards are established

**How to set up:**
1. Open Augment Code Settings
2. Navigate to "Rules & Guidelines" section
3. Click "Add New Rule"
4. Enter rule title: `[Project Name] Development Standards v1.0`
5. Add content covering:
   - Technology stack standards
   - Code quality requirements
   - Security requirements
   - AI response format preferences
6. Save the rule

### **Step 2: Use Task-Specific Rules (Chat Dialog)**

**When to use:**
- Starting new feature development
- Need special requirements
- Temporary standard adjustments

**How to use:**
1. Find the rules icon at the bottom of chat dialog
2. Click "Add Rule" or "Edit Rule"
3. Enter current task-specific rules:
   - Current task focus
   - Special requirements
   - Priority settings
4. Start conversation - rules will be automatically applied

### **Step 3: Upgrade and Update Rules**

**When to upgrade:**
- Project requirements change
- New best practices discovered
- Technology stack upgrades
- Team standards adjustments

**How to upgrade:**
1. Evaluate current rule effectiveness
2. Identify areas for improvement
3. Update Settings Page base rules
4. Test updated rules in new conversations
5. Further adjust based on results

## 📊 **Real-World Usage Examples**

### **Example 1: API Development Project**

**Settings Page Rules:**
```markdown
# RESTful API Development Standards

## API Design Principles
1. Use standard HTTP methods (GET, POST, PUT, DELETE)
2. Follow RESTful URL conventions
3. Unified error response format
4. Support pagination and sorting
5. Include API versioning

## Response Format Standards
- Success: { success: true, data: {...}, message: "..." }
- Error: { success: false, error: {...}, message: "..." }
- Pagination: { data: [...], pagination: { page, limit, total } }
```

**Chat Dialog Rules:**
```markdown
# User Management API Development

## Current Task
Implement user CRUD APIs:
- GET /api/users - Get user list
- GET /api/users/:id - Get single user
- POST /api/users - Create user
- PUT /api/users/:id - Update user
- DELETE /api/users/:id - Delete user

## Special Requirements
1. Exclude password field in responses
2. Support filtering users by role
3. Implement soft delete instead of hard delete
4. Include user activity status tracking
```

### **Example 2: Frontend Component Development**

**Settings Page Rules:**
```markdown
# React Component Development Standards

## Component Design Principles
1. Use functional components and Hooks
2. Follow single responsibility principle
3. Support TypeScript strict mode
4. Implement responsive design
5. Include accessibility features (a11y)

## File Structure Standards
- Component: ComponentName.tsx
- Styles: ComponentName.module.css
- Tests: ComponentName.test.tsx
- Types: ComponentName.types.ts
```

**Chat Dialog Rules:**
```markdown
# Product Card Component Development

## Component Requirements
1. Display product image, name, price, rating
2. Include "Add to Cart" and "Buy Now" buttons
3. Support product variant selection (size, color)
4. Implement image lazy loading and error handling
5. Support keyboard navigation and screen readers

## Performance Requirements
1. Use React.memo to optimize re-renders
2. Images in WebP format with multiple sizes
3. Implement virtual scrolling (if used in lists)
```

## 🔄 **Rule Evolution Strategy**

### **Version Control Approach**
```markdown
# Rule Version Management

## v1.0 - Project Initialization
- Basic technology stack standards
- Basic code quality requirements
- Initial security specifications

## v1.1 - Feature Development Phase
- Add state management standards
- Update performance requirements
- Expand testing requirements

## v1.2 - Optimization Phase
- Add monitoring and logging requirements
- Update deployment standards
- Strengthen security specifications

## v2.0 - Major Upgrade
- Technology stack upgrade
- Architecture adjustments
- New development processes
```

### **Upgrade Decision Process**
```markdown
1. Evaluation Phase
   - Analyze current rule effectiveness
   - Collect team feedback
   - Identify improvement opportunities

2. Planning Phase
   - Define upgrade goals
   - Design new rules
   - Assess impact scope

3. Implementation Phase
   - Update Settings Page rules
   - Test in new projects
   - Gradually roll out to existing projects

4. Validation Phase
   - Monitor rule effectiveness
   - Collect usage feedback
   - Make necessary adjustments
```

## 💡 **Best Practices & Tips**

### **✅ Do's**
- Start simple and gradually refine
- Keep Settings Page rules stable and universal
- Use Chat Dialog rules for current task focus
- Version control your rule changes
- Regularly evaluate rule effectiveness

### **❌ Don'ts**
- Don't put temporary requirements in Settings Page
- Don't repeat basic standards in Chat Dialog
- Don't make Settings Page rules too specific
- Don't make Chat Dialog rules too abstract
- Don't duplicate content between both places

### **🎯 Remember**
**Settings Page Rules = "Constitution" (fundamental law)**
**Chat Dialog Rules = "Regulations" (specific implementation details)**

## 🚀 **Getting Started**

1. **New to Augment Code?** Start with our [Getting Started Guide](link-to-getting-started)
2. **Ready to set rules?** Use our [Rule Templates](link-to-templates)
3. **Need examples?** Check our [Sample Conversations](link-to-examples)
4. **Want to contribute?** See our [Contributing Guidelines](link-to-contributing)

---

**Transform your AI coding experience with properly configured rules and guidelines!** 🎯

*This guide is based on real user experiences and best practices. For more detailed examples and templates, check our [complete documentation](link-to-docs).*
