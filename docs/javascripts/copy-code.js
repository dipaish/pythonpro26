// Add copy button to all code blocks
document.addEventListener('DOMContentLoaded', function() {
  // Find all pre elements with code blocks
  const codeBlocks = document.querySelectorAll('pre code');
  
  codeBlocks.forEach(function(codeBlock) {
    const pre = codeBlock.parentElement;
    
    // Create copy button
    const copyButton = document.createElement('button');
    copyButton.className = 'copy-code-button';
    copyButton.textContent = 'Copy';
    copyButton.setAttribute('aria-label', 'Copy code to clipboard');
    
    // Add click handler
    copyButton.addEventListener('click', function() {
      const code = codeBlock.textContent;
      
      // Copy to clipboard
      navigator.clipboard.writeText(code).then(function() {
        // Show success feedback
        copyButton.textContent = 'Copied!';
        copyButton.style.backgroundColor = '#00ff00';
        copyButton.style.color = '#0c0c0c';
        
        // Reset after 2 seconds
        setTimeout(function() {
          copyButton.textContent = 'Copy';
          copyButton.style.backgroundColor = '';
          copyButton.style.color = '';
        }, 2000);
      }).catch(function(err) {
        console.error('Failed to copy:', err);
        copyButton.textContent = 'Failed';
        setTimeout(function() {
          copyButton.textContent = 'Copy';
        }, 2000);
      });
    });
    
    // Add button to pre element
    pre.style.position = 'relative';
    pre.appendChild(copyButton);
  });
});
