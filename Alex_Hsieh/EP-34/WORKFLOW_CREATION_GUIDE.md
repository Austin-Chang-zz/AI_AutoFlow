# n8n Workflow Creation Guide - EP-34 Examples

## 📋 Overview

This guide demonstrates how to create two practical n8n workflows using the MCP server, based on the EP-34 examples:

1. **AI Parents Daily Reminder** - Automated caring messages via email
2. **Simple MCP Test Workflow** - Basic webhook testing and data processing

## 🤖 Workflow 1: AI Parents Daily Reminder

### Description
An automated workflow that generates caring, nagging messages from AI "parents" and sends them via email daily at 8 AM.

### Workflow Architecture
```
Schedule Trigger → Prepare Context → AI Generation → Format Email → Send Gmail
```

### Step-by-Step Creation

#### Step 1: Schedule Trigger Node
```javascript
// Use MCP to get node essentials
get_node_essentials('n8n-nodes-base.scheduleTrigger')

// Configuration
{
  "parameters": {
    "rule": {
      "interval": [
        {
          "field": "hours",
          "hoursInterval": 24
        }
      ]
    },
    "timezone": "Asia/Taipei"
  },
  "name": "每日早上8點觸發",
  "type": "n8n-nodes-base.scheduleTrigger"
}
```

#### Step 2: Set Node - Prepare Daily Context
```javascript
// Get node configuration
get_node_for_task('set_variables')

// Configuration
{
  "parameters": {
    "assignments": {
      "assignments": [
        {
          "id": "1",
          "name": "today",
          "type": "string",
          "value": "={{ $now.format('yyyy年MM月dd日') }}"
        },
        {
          "id": "2",
          "name": "dayOfWeek",
          "type": "string",
          "value": "={{ $now.format('EEEE', 'zh-TW') }}"
        },
        {
          "id": "3",
          "name": "timeOfDay",
          "type": "string",
          "value": "早上"
        },
        {
          "id": "4",
          "name": "userPrompt",
          "type": "string",
          "value": "請給我一段溫馨的碎碎念，提醒我注意生活上的小細節，讓我感受到爸媽的關愛。今天的日期和星期資訊會在前面的節點提供。"
        }
      ]
    }
  },
  "name": "準備每日情境",
  "type": "n8n-nodes-base.set"
}
```

#### Step 3: OpenAI Node - Generate AI Content
```javascript
// Search for OpenAI node
search_nodes({query: 'openai chat'})

// Configuration
{
  "parameters": {
    "resource": "chat",
    "prompt": {
      "messages": [
        {
          "role": "system",
          "content": "你是一位愛碎碎念但關心孩子的台灣爸媽，會用幽默又溫馨的方式提醒生活細節。你的碎碎念要有以下特色：1.用台灣爸媽的語調，親切又有點囉嗦 2.關心健康、飲食、工作、睡眠等生活面向 3.偶爾加入一些長輩的智慧或人生道理 4.語氣要溫暖但有點念念叨叨 5.適時加入台灣特有的用詞和表達方式 6.內容要實用又有愛 7.長度約100-200字。"
        },
        {
          "content": "={{ $json.userPrompt }}"
        }
      ]
    }
  },
  "name": "AI爸媽產生碎碎念",
  "type": "n8n-nodes-base.openAi",
  "credentials": {
    "openAiApi": "your-openai-credentials"
  }
}
```

#### Step 4: Set Node - Prepare Email Content
```javascript
{
  "parameters": {
    "assignments": {
      "assignments": [
        {
          "id": "1",
          "name": "emailSubject",
          "type": "string",
          "value": "=🏠 {{ $('準備每日情境').first().json.today }} 爸媽的每日碎碎念"
        },
        {
          "id": "2",
          "name": "emailText",
          "type": "string",
          "value": "=\n{{ $json.message.content }}\n💝 全國電子，就甘心 💝\n\n這是來自 AI 爸媽的自動關懷 🤖❤️"
        }
      ]
    }
  },
  "name": "準備郵件內容",
  "type": "n8n-nodes-base.set"
}
```

#### Step 5: Gmail Node - Send Email
```javascript
// Get Gmail node essentials
get_node_essentials('n8n-nodes-base.gmail')

// Configuration
{
  "parameters": {
    "sendTo": "your-email@gmail.com",
    "subject": "={{ $json.emailSubject }}",
    "message": "={{ $json.emailText }}"
  },
  "name": "Send Daily Reminder",
  "type": "n8n-nodes-base.gmail",
  "credentials": {
    "gmailOAuth2": "your-gmail-credentials"
  }
}
```

### Validation and Testing
```javascript
// Validate the complete workflow
validate_workflow(workflowJson)

// Test individual nodes
validate_node_operation({
  nodeType: 'n8n-nodes-base.openAi',
  config: openAiConfig,
  profile: 'runtime'
})
```

## 🔧 Workflow 2: Simple MCP Test Workflow

### Description
A basic webhook-triggered workflow for testing MCP functionality and data processing.

### Workflow Architecture
```
Webhook Trigger → Set Response Data → Return Response
```

### Step-by-Step Creation

#### Step 1: Webhook Trigger Node
```javascript
// Get webhook node essentials
get_node_essentials('n8n-nodes-base.webhook')

// Configuration
{
  "parameters": {
    "path": "test-webhook",
    "responseMode": "lastNode",
    "responseData": "allEntries",
    "options": {}
  },
  "name": "Webhook Trigger",
  "type": "n8n-nodes-base.webhook"
}
```

#### Step 2: Set Node - Process Response Data
```javascript
{
  "parameters": {
    "assignments": {
      "assignments": [
        {
          "id": "1",
          "name": "message",
          "value": "Hello from n8n MCP test!",
          "type": "string"
        },
        {
          "id": "2",
          "name": "timestamp",
          "value": "={{ $now.toISO() }}",
          "type": "string"
        },
        {
          "id": "3",
          "name": "receivedData",
          "value": "={{ $json }}",
          "type": "object"
        },
        {
          "id": "4",
          "name": "status",
          "value": "success",
          "type": "string"
        }
      ]
    }
  },
  "name": "Set Response Data",
  "type": "n8n-nodes-base.set"
}
```

### Testing the Webhook
```bash
# Test the webhook with curl
curl -X POST http://your-n8n-instance.com/webhook/test-webhook \
  -H "Content-Type: application/json" \
  -d '{"test": "data", "user": "MCP Test"}'
```

## 🔍 Workflow Validation Process

### Pre-Deployment Validation
```javascript
// 1. Validate individual nodes
validate_node_minimal({
  nodeType: 'n8n-nodes-base.scheduleTrigger',
  config: scheduleConfig
})

// 2. Validate node operations
validate_node_operation({
  nodeType: 'n8n-nodes-base.openAi',
  config: openAiConfig,
  profile: 'runtime'
})

// 3. Validate complete workflow
validate_workflow(completeWorkflow)

// 4. Check workflow connections
validate_workflow_connections(completeWorkflow)

// 5. Validate expressions
validate_workflow_expressions(completeWorkflow)
```

### Post-Deployment Validation
```javascript
// Create workflow in n8n
const result = n8n_create_workflow(validatedWorkflow)

// Validate deployed workflow
n8n_validate_workflow({id: result.id})

// Monitor executions
n8n_list_executions({workflowId: result.id, status: 'error'})
```

## 📊 Workflow Management

### Creating Workflows
```javascript
// Create the AI Parents workflow
n8n_create_workflow({
  name: "🏠 AI爸媽每日碎碎念工作流",
  nodes: [...],
  connections: {...},
  active: true
})
```

### Updating Workflows
```javascript
// Use efficient diff updates
n8n_update_partial_workflow({
  workflowId: 'workflow-id',
  operations: [
    {
      type: 'updateNode',
      nodeId: 'schedule-trigger',
      changes: {
        parameters: {
          rule: {
            interval: [{field: 'hours', hoursInterval: 12}]
          }
        }
      }
    }
  ]
})
```

### Monitoring Workflows
```javascript
// Check workflow health
n8n_health_check()

// List all workflows
n8n_list_workflows({active: true})

// Get execution details
n8n_get_execution('execution-id')
```

## 🎯 Best Practices

### 1. Always Validate Before Deployment
- Use `validate_node_minimal()` for quick checks
- Use `validate_workflow()` for complete validation
- Fix all validation errors before creating workflows

### 2. Use Efficient Updates
- Use `n8n_update_partial_workflow()` for changes
- Avoid full workflow replacement when possible
- Monitor execution status after updates

### 3. Error Handling
- Add error handling nodes where appropriate
- Use retry mechanisms for external API calls
- Monitor workflow executions regularly

### 4. Security Considerations
- Store credentials securely in n8n
- Use environment variables for sensitive data
- Validate webhook inputs to prevent injection

## 🚀 Next Steps

1. **Install the n8n MCP server** following the installation guide
2. **Create your first workflow** using one of the examples above
3. **Test thoroughly** using the validation tools
4. **Deploy and monitor** your workflows
5. **Iterate and improve** based on execution results

---

**Happy workflow building with n8n MCP!** 🎉
