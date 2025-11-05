// Replace footer content with custom information
document.addEventListener('DOMContentLoaded', function() {
  // Find the footer copyright section
  const footerCopyright = document.querySelector('.md-footer-copyright');
  
  if (footerCopyright) {
    // Replace the entire content
    footerCopyright.innerHTML = `
      <div style="text-align: center; font-family: 'Courier New', Courier, monospace; color: #00ff00 !important; padding: 20px;">
        <p style="color: #00ff00 !important; margin: 8px 0; font-size: 14px;">
          ©2024 Deepak KC. All rights reserved. | Site last generated: Nov 05, 2025
        </p>
        <p style="color: #00ff00 !important; margin: 8px 0; font-size: 14px;">
          <a href="https://github.com/dipaish" target="_blank" rel="noopener" style="color: #00ff00 !important; text-decoration: underline; margin: 0 10px;">GitHub</a> |
          <a href="https://www.linkedin.com/in/kcdeepak112/" target="_blank" rel="noopener" style="color: #00ff00 !important; text-decoration: underline; margin: 0 10px;">LinkedIn</a>
        </p>
        <p style="color: #00ff00 !important; margin: 8px 0; font-size: 12px;">
          user@pythonpro26:~$ █
        </p>
      </div>
    `;
  }
  
  // Also try to find and replace any Dracula-specific footer elements
  const draculaFooter = document.querySelector('footer .drac-text-black');
  if (draculaFooter) {
    draculaFooter.innerHTML = `
      <div style="text-align: center; font-family: 'Courier New', Courier, monospace; color: #00ff00 !important;">
        <p style="color: #00ff00 !important;">©2024 Deepak KC. All rights reserved. | Site last generated: Nov 05, 2025</p>
        <p style="color: #00ff00 !important;">
          <a href="https://github.com/dipaish" target="_blank" style="color: #00ff00 !important; text-decoration: underline;">GitHub</a> |
          <a href="https://www.linkedin.com/in/kcdeepak112/" target="_blank" style="color: #00ff00 !important; text-decoration: underline;">LinkedIn</a>
        </p>
        <p style="color: #00ff00 !important; font-size: 12px;">user@pythonpro26:~$ █</p>
      </div>
    `;
  }
});
