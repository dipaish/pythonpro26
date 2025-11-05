// Enhance visibility of Previous/Next links and add a floating sidebar toggle
(function(){
  function styleNavLink(a){
    if(!a) return;
    a.style.backgroundColor = '#2a2a2a';
    a.style.color = '#00ff00';
    a.style.border = '2px solid #00ff00';
    a.style.padding = '10px 16px';
    a.style.borderRadius = '6px';
    a.style.fontWeight = '600';
    a.style.fontFamily = "Courier New, Courier, monospace";
    a.style.display = 'inline-flex';
    a.style.alignItems = 'center';
    a.style.gap = '8px';
    a.style.textDecoration = 'none';
    a.style.boxShadow = '0 0 15px rgba(0,255,0,0.8)';
    a.style.textShadow = '0 0 8px rgba(0,255,0,0.8)';
  }

  function brightenOnHover(a){
    if(!a) return;
    a.addEventListener('mouseenter', ()=>{
      a.style.backgroundColor = '#333333';
      a.style.boxShadow = '0 0 20px rgba(0,255,0,1)';
      a.style.textShadow = '0 0 10px rgba(0,255,0,1)';
    });
    a.addEventListener('mouseleave', ()=>{
      a.style.backgroundColor = '#2a2a2a';
      a.style.boxShadow = '0 0 15px rgba(0,255,0,0.8)';
      a.style.textShadow = '0 0 8px rgba(0,255,0,0.8)';
    });
  }

  function findNavLinks(){
    const selectors = [
      'a[rel="prev"]',
      'a[rel="next"]',
      'a[class*="prev" i]',
      'a[class*="next" i]',
      'a[aria-label^="Previous" i]',
      'a[aria-label^="Next" i]'
    ];
    const links = Array.from(document.querySelectorAll(selectors.join(',')));
    return {
      prev: links.find(a=>/prev|previous/i.test(a.rel||a.className||a.getAttribute('aria-label')||'')) || links.find(a=>/previous/i.test((a.textContent||''))),
      next: links.find(a=>/next/i.test(a.rel||a.className||a.getAttribute('aria-label')||'')) || links.find(a=>/next/i.test((a.textContent||'')))
    };
  }

  function colorizeSvg(a){
    if(!a) return;
    a.querySelectorAll('svg path').forEach(p=>{ p.style.fill = '#00ff00'; });
  }

  function applyNavStyles(){
    const {prev, next} = findNavLinks();
    [prev, next].forEach(a=>{ styleNavLink(a); brightenOnHover(a); colorizeSvg(a); });
  }

  function addFloatingMenuButton(){
    // Create a floating menu button to reopen sidebar when collapsed
    const btn = document.createElement('button');
    btn.textContent = '☰ Menu';
    Object.assign(btn.style, {
      position: 'fixed', top: '16px', left: '16px', zIndex: '10000',
      backgroundColor: '#0c0c0c', color: '#00ff00', border: '2px solid #00ff00',
      borderRadius: '6px', padding: '8px 12px', fontFamily: 'Courier New, Courier, monospace',
      cursor: 'pointer', boxShadow: '0 0 10px rgba(0,255,0,0.8)'
    });

    function tryToggle(){
      // Material: checkbox drawer
      const drawer = document.getElementById('__drawer');
      if (drawer) { drawer.checked = !drawer.checked; return; }
      // Label for drawer
      const label = document.querySelector('[for="__drawer"]');
      if (label) { label.click(); return; }
      // Buttons with menu/nav labels
      const btns = document.querySelectorAll('button[aria-label*="menu" i], button[aria-label*="nav" i], button[aria-label*="navigation" i], .navbar-burger, .nav-toggle');
      if (btns.length) { btns[0].click(); return; }
    }

    btn.addEventListener('click', tryToggle);

    document.body.appendChild(btn);
  }

  document.addEventListener('DOMContentLoaded', function(){
    applyNavStyles();
    addFloatingMenuButton();
  });
})();
