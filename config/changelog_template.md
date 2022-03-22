# Release Notes

## Pull Requests
{{#forEach runDetails.pull_requests}}
**{{this.number}}** {{this.title}}
### Commits
  {{#forEach this.commits}}
  - **{{this.sha}}** {{this.commit.message}}
  {{/forEach}}
### Comments
 {{#forEach this.comments}}
 - {{this.body}}
 {{/forEach}}

### linkedIssues
 {{#forEach this.linkedIssues}}
 - **{{this.number}}** {{this.title}}
 {{/forEach}}
    
{{/forEach}}
