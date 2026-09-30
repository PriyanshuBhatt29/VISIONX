const file=document.getElementById("file");
const run=document.getElementById("run");
const preview=document.getElementById("preview");
const result=document.getElementById("result");
const detections=document.getElementById("detections");
const log=document.getElementById("log");

function write(line){log.textContent += "\n"+line; log.scrollTop=log.scrollHeight}

run.onclick=async()=>{
  if(!file.files[0]){write("[WARN] No visual input selected.");return}
  const form=new FormData();form.append("file",file.files[0]);
  write("[CORE] Uploading frame...");
  const t=performance.now();
  try{
    const r=await fetch("/api/detect",{method:"POST",body:form});
    const data=await r.json();
    if(data.error)throw new Error(data.error);
    const ms=Math.round(performance.now()-t);
    document.getElementById("active").textContent=String(data.analytics.active_objects).padStart(2,"0");
    document.getElementById("unique").textContent=String(data.analytics.unique_objects).padStart(2,"0");
    document.getElementById("people").textContent=String(data.analytics.people).padStart(2,"0");
    document.getElementById("latency").textContent=data.analytics.latency_ms+" ms";
    const bytes=new Uint8Array(data.image_base64.match(/.{1,2}/g).map(x=>parseInt(x,16)));
    preview.src=URL.createObjectURL(new Blob([bytes],{type:"image/jpeg"}));
    detections.innerHTML=data.detections.map(d=>`<div style="padding:7px 0;border-bottom:1px solid #211015;font:11px JetBrains Mono;color:#aaa"><b style="color:#ff1744">#${d.track_id}</b> ${d.label.toUpperCase()} — ${(d.confidence*100).toFixed(1)}%</div>`).join("");
    result.classList.remove("hidden");
    write(`[OK  ] Inference complete in ${ms}ms — ${data.detections.length} detections.`);
  }catch(e){write("[ERR ] "+e.message)}
};

file.onchange=()=>{if(file.files[0])write("[INPUT] "+file.files[0].name+" loaded.");};
