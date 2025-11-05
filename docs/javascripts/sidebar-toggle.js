// Add a collapse/expand toggle button to the sidebar for desktop users
(function() {
  function addSidebarToggle() {
    // Find the sidebar container
    const sidebar = document.querySelector('#sidebar, nav#sidebar, .sidebar, .md-sidebar, [data-md-component="sidebar"]');
    
    if (!sidebar) return;

    // Create toggle button
    const toggleBtn = document.createElement('button');
    toggleBtn.innerHTML = '◀'; // Left arrow to collapse
    toggleBtn.setAttribute('aria-label', 'Toggle sidebar');
    toggleBtn.className = 'sidebar-toggle-btn';
    
    // Style the button
    Object.assign(toggleBtn.style, {
      position: 'absolute',
      top: '10px',
      right: '-15px',
      width: '30px',
      height: '30px',
      backgroundColor: '#1a1a1a',
      color: '#00ff00',
      border: '2px solid #00ff00',
      borderRadius: '50%',
      cursor: 'pointer',
      zIndex: '1000',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      fontSize: '16px',
      fontWeight: 'bold',
      boxShadow: '0 0 10px rgba(0,255,0,0.5)',
      transition: 'all 0.3s ease'
    });

    // Make sure sidebar has position relative
    if (window.getComputedStyle(sidebar).position === 'static') {
      sidebar.style.position = 'relative';
    }

    let isCollapsed = false;

    // Toggle function
    toggleBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      isCollapsed = !isCollapsed;
      
      if (isCollapsed) {
        // Collapse sidebar
        sidebar.style.width = '0';
        sidebar.style.minWidth = '0';
        sidebar.style.overflow = 'hidden';
        sidebar.style.marginLeft = '-250px'; // Adjust based on sidebar width
        toggleBtn.innerHTML = '▶'; // Right arrow to expand
        toggleBtn.style.right = 'auto';
        toggleBtn.style.left = '10px';
        toggleBtn.style.position = 'fixed';
      } else {
        // Expand sidebar
        sidebar.style.width = '';
        sidebar.style.minWidth = '';
        sidebar.style.overflow = '';
        sidebar.style.marginLeft = '';
        toggleBtn.innerHTML = '◀'; // Left arrow to collapse
        toggleBtn.style.right = '-15px';
        toggleBtn.style.left = 'auto';
        toggleBtn.style.position = 'absolute';
      }
    });

    // Add hover effect
    toggleBtn.addEventListener('mouseenter', function() {
      this.style.backgroundColor = '#2a2a2a';
      this.style.boxShadow = '0 0 15px rgba(0,255,0,0.8)';
    });

    toggleBtn.addEventListener('mouseleave', function() {
      this.style.backgroundColor = '#1a1a1a';
      this.style.boxShadow = '0 0 10px rgba(0,255,0,0.5)';
    });

    sidebar.appendChild(toggleBtn);
  }

  // Wait for DOM to be ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', addSidebarToggle);
  } else {
    addSidebarToggle();
  }
})();
