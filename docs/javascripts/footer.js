// Replace footer content with custom information
document.addEventListener('DOMContentLoaded', function() {
  // Find the footer copyright section
  const footerCopyright = document.querySelector('.md-footer-copyright');
  
  if (footerCopyright) {
    // Replace the entire content with terminal-styled footer
    footerCopyright.innerHTML = `
      <div style="background-color: #0c0c0c !important; text-align: center; font-family: 'Courier New', Courier, monospace; color: #00ff00 !important; padding: 20px; border-top: 2px solid #00ff00;">
        <p style="color: #00ff00 !important; margin: 10px 0; font-size: 14px;">
          ©2024 Deepak KC. All rights reserved. | Site last generated: Nov 05, 2025
        </p>
        <p style="color: #00ff00 !important; margin: 10px 0; font-size: 14px;">
          <a href="https://github.com/dipaish" target="_blank" rel="noopener" style="color: #00ff00 !important; text-decoration: underline; margin: 0 10px;">GitHub</a> |
          <a href="https://www.linkedin.com/in/kcdeepak112/" target="_blank" rel="noopener" style="color: #00ff00 !important; text-decoration: underline; margin: 0 10px;">LinkedIn</a>
        </p>
        <p style="color: #00ff00 !important; margin: 10px 0; font-size: 12px;">
          user@pythonpro26:~$ █
        </p>
      </div>
    `;
    
    // Force parent elements to have black background too
    if (footerCopyright.parentElement) {
      footerCopyright.parentElement.style.backgroundColor = '#0c0c0c';
    }
  }
  
  // Also try to find and replace any Dracula-specific footer elements
  const draculaFooter = document.querySelector('footer .drac-text-black');
  if (draculaFooter) {
    draculaFooter.innerHTML = `
      <div style="background-color: #0c0c0c !important; text-align: center; font-family: 'Courier New', Courier, monospace; color: #00ff00 !important; padding: 20px; border-top: 2px solid #00ff00;">
        <p style="color: #00ff00 !important; margin: 10px 0; font-size: 14px;">©2024 Deepak KC. All rights reserved. | Site last generated: Nov 05, 2025</p>
        <p style="color: #00ff00 !important; margin: 10px 0; font-size: 14px;">
          <a href="https://github.com/dipaish" target="_blank" style="color: #00ff00 !important; text-decoration: underline; margin: 0 10px;">GitHub</a> |
          <a href="https://www.linkedin.com/in/kcdeepak112/" target="_blank" style="color: #00ff00 !important; text-decoration: underline; margin: 0 10px;">LinkedIn</a>
        </p>
        <p style="color: #00ff00 !important; margin: 10px 0; font-size: 12px;">user@pythonpro26:~$ █</p>
      </div>
    `;
  }
  
  // Force the entire footer to have black background
  const footer = document.querySelector('footer');
  if (footer) {
    footer.style.backgroundColor = '#0c0c0c';
  }
  
  const footerMeta = document.querySelector('.md-footer-meta');
  if (footerMeta) {
    footerMeta.style.backgroundColor = '#0c0c0c';
  }
});
