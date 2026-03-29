// =================== AI "Neural Field" Background 2.1 (stable) ===================
// 2D field + depth-based parallax (stable, performant)

const canvas = document.getElementById('fx');
if (canvas) {
    const ctx = canvas.getContext('2d');
    let dpr = Math.min(window.devicePixelRatio || 1, 2);
    let W, H, nodes = [], lastT = 0, mouse={x:null,y:null,down:false};
    let cam = {x:0,y:0,t:0}; // parallax drift only

    const CFG = { baseNodes: 80, maxDist: 170, speed: 0.55, hueA: 224, hueB: 266, pulseEvery: 2200, separation: 34, jitter: 0.12, depthMin: 0.7, depthMax: 1.6 };

    function resize(){
        W = canvas.width = Math.floor(innerWidth * dpr);
        H = canvas.height = Math.floor(innerHeight * dpr);
        canvas.style.width = innerWidth + 'px';
        canvas.style.height = innerHeight + 'px';
        ctx.setTransform(dpr,0,0,dpr,0,0);
        const area = innerWidth * innerHeight;
        const n = Math.max(50, Math.min(160, Math.round(CFG.baseNodes * (area / (1200*800)))));
        nodes = new Array(n).fill(0).map(()=>spawn());
    }

    function rnd(a=1){return Math.random()*a}
    function randRange(a,b){return a + Math.random()*(b-a)}

    function spawn(){ return { x: rnd(innerWidth), y: rnd(innerHeight), vx: rnd(1)-.5, vy: rnd(1)-.5, r: 1 + rnd(1.6), z: randRange(CFG.depthMin, CFG.depthMax), phase: rnd(Math.PI*2) } }

    function field(x,y,t){
        const s1 = 0.0009 + Math.sin(t*0.07)*0.0002;
        const s2 = 0.0013 + Math.cos(t*0.05)*0.00025;
        const a = Math.sin(x*s1 + t*0.6) + Math.cos(y*s1*1.2 - t*0.5);
        const b = Math.cos(x*s2 - t*0.4) - Math.sin(y*s2*1.1 + t*0.7);
        return [a, b];
    }

    let lastPulse = 0;
    function tick(ms){
        const t = ms/1000; const dt = lastT ? Math.min(0.05, t - lastT) : 0.016; lastT = t;
        cam.t += dt; cam.x = Math.sin(cam.t*0.08)*60; cam.y = Math.cos(cam.t*0.06)*40;
        ctx.clearRect(0,0,innerWidth,innerHeight);

        const grd = ctx.createRadialGradient(innerWidth*0.15, innerHeight*0.1, 0, innerWidth*0.5, innerHeight*0.7, Math.hypot(innerWidth,innerHeight)*0.9);
        grd.addColorStop(0, 'rgba(45,106,227,0.10)');
        grd.addColorStop(1, 'rgba(0,0,0,0)');
        ctx.fillStyle = grd; ctx.fillRect(0,0,innerWidth,innerHeight);

        const maxD = CFG.maxDist; const sep = CFG.separation; const sep2 = sep*sep;
        const pulse = (ms - lastPulse) < 520; if(ms - lastPulse > CFG.pulseEvery) lastPulse = ms;

        for(let i=0;i<nodes.length;i++){
        const n = nodes[i];
        const [fx,fy] = field(n.x, n.y, t*CFG.speed + n.phase*0.2);
        n.vx += fx*0.05 + (Math.random()-0.5)*CFG.jitter;
        n.vy += fy*0.05 + (Math.random()-0.5)*CFG.jitter;
        for(let j=i+1;j<nodes.length;j++){
            const m = nodes[j]; const dx = n.x - m.x, dy = n.y - m.y; const d2 = dx*dx + dy*dy;
            if(d2 < sep2){ const d = Math.sqrt(d2) || 0.001; const f = (sep - d)/sep * 0.12; const ux = dx/d, uy = dy/d; n.vx += ux*f; n.vy += uy*f; m.vx -= ux*f; m.vy -= uy*f; }
        }
        if(mouse.x!=null){ const dx = n.x - mouse.x, dy = n.y - mouse.y, d = Math.hypot(dx,dy);
            if(d < 160){ const f = (mouse.down? -1:1) * (160-d)/160 * 0.9; n.vx += (dx/d||0)*f; n.vy += (dy/d||0)*f; }
        }
        n.vx *= 0.96; n.vy *= 0.96; n.x += n.vx; n.y += n.vy;
        if(n.x < -60) n.x = innerWidth+60; if(n.x > innerWidth+60) n.x = -60;
        if(n.y < -60) n.y = innerHeight+60; if(n.y > innerHeight+60) n.y = -60;
        }

        // draw links with parallax
        for(let i=0;i<nodes.length;i++){
        const a = nodes[i]; const ax = a.x - cam.x*a.z, ay = a.y - cam.y*a.z;
        ctx.beginPath(); ctx.fillStyle = 'rgba(220,235,255,.08)'; ctx.arc(ax,ay, a.r*3,0,Math.PI*2); ctx.fill();
        for(let j=i+1;j<nodes.length;j++){
            const b = nodes[j]; const bx = b.x - cam.x*b.z, by = b.y - cam.y*b.z; const dx = ax - bx, dy = ay - by; const d = Math.hypot(dx,dy);
            if(d < maxD){ const w = 1 - d/maxD; const hue = CFG.hueA*(1-w) + CFG.hueB*w; ctx.strokeStyle = `hsla(${hue}, 86%, 66%, ${w*0.7})`;
            if(pulse && (i%7===0 || j%11===0)) ctx.strokeStyle = `hsla(${hue}, 96%, 78%, ${w})`;
            ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(ax,ay); ctx.lineTo(bx,by); ctx.stroke(); }
        }
        }
        for(const n of nodes){ const nx = n.x - cam.x*n.z, ny = n.y - cam.y*n.z; ctx.beginPath(); ctx.fillStyle = 'rgba(240,245,255,.75)'; ctx.arc(nx,ny, Math.max(1, n.r*n.z*0.9), 0, Math.PI*2); ctx.fill(); }
        requestAnimationFrame(tick);
    }

    function onMove(e){ if(e.touches && e.touches[0]){ mouse.x = e.touches[0].clientX; mouse.y = e.touches[0].clientY; } else { mouse.x = e.clientX; mouse.y = e.clientY; } }
    function onLeave(){ mouse.x = mouse.y = null; }

    window.addEventListener('resize', resize);
    window.addEventListener('pointermove', onMove);
    window.addEventListener('pointerdown', e=>{mouse.down=true; onMove(e)});
    window.addEventListener('pointerup', ()=>mouse.down=false);
    window.addEventListener('pointerleave', onLeave);

    resize(); requestAnimationFrame(tick);
}
