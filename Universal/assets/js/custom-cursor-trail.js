
document.addEventListener('DOMContentLoaded', () => {
    const container = document.createElement('div');
    container.id = 'cursor-trail-container';
    container.style.position = 'fixed';
    container.style.top = '0';
    container.style.left = '0';
    container.style.width = '100vw';
    container.style.height = '100vh';
    container.style.pointerEvents = 'none';
    container.style.zIndex = '999999';
    document.body.appendChild(container);

    let lastX = 0;
    let lastY = 0;

    document.addEventListener('mousemove', (e) => {
        const x = e.clientX;
        const y = e.clientY;

        const dist = Math.hypot(x - lastX, y - lastY);
        if (dist > 15) {
            spawnParticle(x, y);
            lastX = x;
            lastY = y;
        }
    });

    function spawnParticle(x, y) {
        const particle = document.createElement('div');
        particle.className = 'fuel-particle';
        particle.style.left = `${x}px`;
        particle.style.top = `${y}px`;
        
        const driftX = (Math.random() - 0.5) * 30; // wide spread
        particle.style.setProperty('--drift-x', `${driftX}px`);
        
        container.appendChild(particle);

        setTimeout(() => {
            if (particle.parentNode) {
                particle.parentNode.removeChild(particle);
            }
        }, 1500);
    }
});
