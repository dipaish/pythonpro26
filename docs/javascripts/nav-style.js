// Enhance visibility of Previous/Next links with white color for accessibility
(function(){
  function styleNavLink(a){
    if(!a) return;
    // White text on dark background for high contrast accessibility
    a.style.backgroundColor = '#2a2a2a';
    a.style.color = '#ffffff';
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
    a.style.textShadow = 'none'; // Remove green glow on text for better readability
  }

  function brightenOnHover(a){
    if(!a) return;
    a.addEventListener('mouseenter', ()=>{
      a.style.backgroundColor = '#333333';
      a.style.color = '#ffffff';
      a.style.boxShadow = '0 0 20px rgba(0,255,0,1)';
    });
    a.addEventListener('mouseleave', ()=>{
      a.style.backgroundColor = '#2a2a2a';
      a.style.color = '#ffffff';
      a.style.boxShadow = '0 0 15px rgba(0,255,0,0.8)';
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
    a.querySelectorAll('svg path').forEach(p=>{ p.style.fill = '#ffffff'; }); // White SVG icons
  }

  function applyNavStyles(){
    const {prev, next} = findNavLinks();
    [prev, next].forEach(a=>{ styleNavLink(a); brightenOnHover(a); colorizeSvg(a); });
  }

  document.addEventListener('DOMContentLoaded', function(){
    applyNavStyles();
  });
})();
