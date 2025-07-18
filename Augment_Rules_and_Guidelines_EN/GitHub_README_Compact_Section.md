## 📋 Rules & Guidelines: When and How to Use

Augment Code offers two powerful ways to customize AI behavior. Understanding the difference is key to maximizing productivity.

### 🎯 **Quick Reference: Settings vs Chat Rules**

| Feature | Settings Page Rules | Chat Dialog Rules |
|---------|-------------------|------------------|
| **Duration** | Long-term (months/years) | Short-term (days/weeks) |
| **Scope** | Global (entire project) | Local (current task) |
| **Content** | Standards & principles | Specific requirements |
| **Examples** | Technology stack, code quality | Current feature, priorities |

### 📋 **Settings Page Rules** - Your Project's "Constitution"

**Use for:** Stable, project-wide standards

```markdown
# Example: E-commerce Development Standards v1.0

## Technology Stack
- Frontend: React 18 + TypeScript
- Backend: Node.js + Express
- Database: PostgreSQL + Redis

## Code Quality Standards
1. TypeScript strict mode required
2. Test coverage >80%
3. All APIs must include error handling

## AI Response Format
1. Provide complete code implementations
2. Include detailed comments
3. Explain potential security risks
```

**When to set:**
- ✅ Project initialization
- ✅ Technology stack decisions
- ✅ Team standard establishment
- ✅ Major version upgrades

### 💬 **Chat Dialog Rules** - Your Task's "Action Plan"

**Use for:** Current task-specific requirements

```markdown
# Example: User Authentication Module

## Current Focus
- JWT authentication system
- Registration, login, password reset
- Social media login support

## Special Requirements
1. bcrypt encryption, salt rounds = 12
2. JWT: access token 15min, refresh 7 days
3. Lock account after 5 failed attempts

## Priorities
1. High: Basic login/registration
2. Medium: Password reset
3. Low: Social media integration
```

**When to use:**
- ✅ Starting new features
- ✅ Special task requirements
- ✅ Temporary priority changes
- ✅ Experimental approaches

### 🚀 **Quick Setup Guide**

#### **Step 1: Global Rules (Settings)**
1. Open Augment Code Settings → Rules & Guidelines
2. Add project standards (tech stack, quality, security)
3. Set AI response preferences
4. Save as version 1.0

#### **Step 2: Task Rules (Chat)**
1. Click rules icon in chat dialog
2. Add current task focus and requirements
3. Set priorities and constraints
4. Start coding with context

#### **Step 3: Evolution**
- Update Settings rules monthly/quarterly
- Adjust Chat rules per task/daily
- Version control major changes

### 💡 **Pro Tips**

**✅ Best Practices:**
- Keep Settings rules stable and universal
- Use Chat rules for current task focus
- Start simple, refine gradually
- Version your rule changes

**❌ Common Mistakes:**
- Putting temporary needs in Settings
- Repeating basic standards in Chat
- Making Settings too specific
- Making Chat rules too abstract

### 📊 **Real Example: API Development**

**Settings Page (Stable):**
```markdown
## API Standards
- RESTful design principles
- Unified error response format
- Authentication required for all endpoints
```

**Chat Dialog (Current Task):**
```markdown
## User Management API
- Implement CRUD operations
- Support role-based filtering  
- Soft delete instead of hard delete
- Exclude password in responses
```

---

**Remember:** Settings = "Constitution" (fundamental law), Chat = "Regulations" (specific implementation)

*For detailed examples and templates, see our [complete documentation](link-to-full-guide).*
