# n8n MCP Server Installation and Workflow Creation Guide

## 📋 Overview

This guide will help you install the n8n MCP (Model Context Protocol) server on Augment Code and create workable n8n workflows based on the EP-34 examples.

## 🚀 Installation Steps

### Step 1: Install n8n MCP Server

The n8n MCP server is already configured in your Augment environment. The server configuration is stored in:
- `Augment/mcp_servers/n8n_mcp_server.json`

### Step 2: Configure Augment Code MCP Settings

Add the following configuration to your Augment Code MCP settings:

#### Basic Configuration (Documentation Only)
```json
{
  "mcpServers": {
    "n8n-mcp": {
      "command": "npx",
      "args": ["n8n-mcp"],
      "env": {
        "MCP_MODE": "stdio",
        "LOG_LEVEL": "error",
        "DISABLE_CONSOLE_OUTPUT": "true"
      }
    }
  }
}
```

#### Full Configuration (With n8n API Access)
```json
{
  "mcpServers": {
    "n8n-mcp": {
      "command": "npx",
      "args": ["n8n-mcp"],
      "env": {
        "MCP_MODE": "stdio",
        "LOG_LEVEL": "error",
        "DISABLE_CONSOLE_OUTPUT": "true",
        "N8N_API_URL": "http://localhost:5678",
        "N8N_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

### Step 3: Restart Augment Code

After adding the MCP configuration, restart Augment Code to load the n8n MCP server.

## 📊 Available MCP Tools

Once installed, you'll have access to these powerful tools:

### Core Documentation Tools
- `tools_documentation()` - Get documentation for any MCP tool
- `list_nodes()` - List all n8n nodes with filtering
- `search_nodes()` - Search nodes by functionality
- `get_node_essentials()` - Get essential properties (10-20 instead of 200+)
- `get_node_for_task()` - Pre-configured settings for common tasks

### Validation Tools
- `validate_node_operation()` - Validate node configurations
- `validate_workflow()` - Complete workflow validation
- `validate_workflow_connections()` - Check workflow structure

### n8n Management Tools (Requires API Configuration)
- `n8n_create_workflow()` - Create new workflows
- `n8n_get_workflow()` - Get workflow by ID
- `n8n_update_partial_workflow()` - Update workflows efficiently
- `n8n_trigger_webhook_workflow()` - Trigger workflows
- `n8n_list_executions()` - Monitor workflow executions

## 🔧 Workflow Creation Process

### 1. Discovery Phase
```javascript
// Find the right nodes for your task
search_nodes({query: 'email gmail'})
list_nodes({category: 'trigger'})
```

### 2. Configuration Phase
```javascript
// Get essential properties for quick setup
get_node_essentials('n8n-nodes-base.gmail')

// Get pre-configured templates
get_node_for_task('send_email')
```

### 3. Validation Phase
```javascript
// Validate node configuration
validate_node_operation({
  nodeType: 'n8n-nodes-base.gmail',
  config: {resource: 'message', operation: 'send'},
  profile: 'runtime'
})

// Validate complete workflow
validate_workflow(workflowJson)
```

### 4. Deployment Phase
```javascript
// Create workflow in n8n (if API configured)
n8n_create_workflow(validatedWorkflow)

// Validate deployed workflow
n8n_validate_workflow({id: 'workflow-id'})
```

## 📝 Example Workflows

Based on the EP-34 examples, here are two workflows you can create:

### 1. AI Parents Daily Reminder (Mom.json)
- **Trigger**: Schedule (daily at 8 AM)
- **Process**: Generate AI-powered caring messages
- **Action**: Send email via Gmail
- **Features**: Uses OpenAI for content generation

### 2. Simple MCP Test Workflow (simple_n8n_mcp_workflow_test.json)
- **Trigger**: Webhook
- **Process**: Set response data with timestamp
- **Action**: Return formatted response
- **Features**: Basic webhook testing and data processing

## 🛠️ Next Steps

1. **Install the MCP server** using the configuration above
2. **Test the connection** by running `tools_documentation()`
3. **Explore available nodes** with `list_nodes()`
4. **Create your first workflow** using the examples as templates
5. **Validate and deploy** your workflows

## 📚 Additional Resources

- [n8n MCP GitHub Repository](https://github.com/czlonkowski/n8n-mcp)
- [n8n Official Documentation](https://docs.n8n.io/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)

## 🔍 Troubleshooting

### Common Issues

1. **MCP Server Not Loading**
   - Check Node.js is installed
   - Verify MCP configuration syntax
   - Restart Augment Code

2. **API Tools Not Available**
   - Ensure N8N_API_URL and N8N_API_KEY are set
   - Check n8n instance is running
   - Verify API key permissions

3. **Workflow Validation Errors**
   - Use `validate_node_minimal()` for quick checks
   - Check required fields are populated
   - Verify node type names are correct

### Getting Help

If you need support during the installation or workflow creation process:

1. Check the MCP server logs for error messages
2. Use `n8n_diagnostic()` to troubleshoot API connectivity
3. Validate your workflow step-by-step using the validation tools
4. Refer to the EP-34 examples for working configurations

---

**Ready to start building powerful n8n workflows with AI assistance!** 🚀
