// Replace footer content with custom information
document.addEventListener('DOMContentLoaded', function() {
  // Force the entire footer area to have black background
  const footer = document.querySelector('footer');
  if (footer) {
    footer.style.backgroundColor = '#0c0c0c';
    footer.style.borderTop = '2px solid #00ff00';
  }
  
  const footerMeta = document.querySelector('.md-footer-meta');
  if (footerMeta) {
    footerMeta.style.backgroundColor = '#0c0c0c';
  }
  
  const footerInner = document.querySelector('.md-footer-meta__inner');
  if (footerInner) {
    footerInner.style.backgroundColor = '#0c0c0c';
  }
  
  // Find the footer copyright section
  const footerCopyright = document.querySelector('.md-footer-copyright');
  
  if (footerCopyright) {
    // Force parent to have black background and center content
    footerCopyright.style.backgroundColor = '#0c0c0c';
    footerCopyright.style.textAlign = 'center';
    footerCopyright.style.width = '100%';
    footerCopyright.style.padding = '0';
    
    if (footerCopyright.parentElement) {
      footerCopyright.parentElement.style.backgroundColor = '#0c0c0c';
      footerCopyright.parentElement.style.textAlign = 'center';
    }
    
    // Replace the entire content with terminal-styled footer
    footerCopyright.innerHTML = `
      <div style="background-color: #0c0c0c !important; text-align: center !important; font-family: 'Courier New', Courier, monospace; color: #00ff00 !important; padding: 20px; width: 100%; margin: 0 auto;">
        <p style="color: #00ff00 !important; margin: 10px 0; font-size: 16px;">
          Deepak Chhetri. | Site last generated: Nov 05, 2025
        </p>
        <p style="color: #00ff00 !important; margin: 10px 0; font-size: 16px;">
          <a href="https://github.com/dipaish" target="_blank" rel="noopener" style="color: #00ff00 !important; text-decoration: underline; margin: 0 10px;">GitHub</a> |
          <a href="https://www.linkedin.com/in/kcdeepak112/" target="_blank" rel="noopener" style="color: #00ff00 !important; text-decoration: underline; margin: 0 10px;">LinkedIn</a>
        </p>
      </div>
    `;
  }
  
  // Also try to find and replace any Dracula-specific footer elements
  const draculaFooter = document.querySelector('footer .drac-text-black');
  if (draculaFooter) {
    draculaFooter.style.backgroundColor = '#0c0c0c';
    draculaFooter.style.textAlign = 'center';
    
    draculaFooter.innerHTML = `
      <div style="background-color: #0c0c0c !important; text-align: center !important; font-family: 'Courier New', Courier, monospace; color: #00ff00 !important; padding: 20px; width: 100%;">
        <p style="color: #00ff00 !important; margin: 10px 0; font-size: 16px;">Deepak Chhetri | Site last generated: Nov 05, 2025</p>
        <p style="color: #00ff00 !important; margin: 10px 0; font-size: 16px;">
          <a href="https://github.com/dipaish" target="_blank" style="color: #00ff00 !important; text-decoration: underline; margin: 0 10px;">GitHub</a> |
          <a href="https://www.linkedin.com/in/kcdeepak112/" target="_blank" style="color: #00ff00 !important; text-decoration: underline; margin: 0 10px;">LinkedIn</a>
        </p>
      </div>
    `;
  }
});
