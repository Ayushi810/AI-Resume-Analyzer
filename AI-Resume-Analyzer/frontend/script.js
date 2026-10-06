const form = document.getElementById("resumeForm");
const button = document.getElementById("analyzeBtn");
const message = document.getElementById("message");
const results = document.getElementById("results");
function showMessage(text){ message.textContent=text; message.classList.remove("hidden"); }
function hideMessage(){ message.classList.add("hidden"); }
function renderChips(id, items, missing=false){
  const box=document.getElementById(id); box.innerHTML="";
  if(!items || !items.length){ box.innerHTML="<span class='chip'>None detected</span>"; return; }
  items.forEach(item=>{ const span=document.createElement("span"); span.className="chip"+(missing?" missing":""); span.textContent=item; box.appendChild(span); });
}
form.addEventListener("submit", async (event)=>{
  event.preventDefault(); hideMessage();
  const file=document.getElementById("resume").files[0];
  const jobDescription=document.getElementById("job_description").value.trim();
  if(!file || !jobDescription){ showMessage("Please select a resume and enter the job description."); return; }
  if(file.size>5*1024*1024){ showMessage("File is larger than 5 MB. Please upload a smaller resume."); return; }
  const data=new FormData(); data.append("resume",file); data.append("job_description",jobDescription);
  button.disabled=true; button.textContent="Analyzing...";
  try{
    const response=await fetch("/analyze",{method:"POST",body:data});
    const result=await response.json(); if(!response.ok) throw new Error(result.error||"Analysis failed.");
    document.getElementById("score").textContent=`${result.ats_score}%`;
    document.getElementById("scoreText").textContent=result.score_message;
    renderChips("matchingSkills",result.matching_skills); renderChips("missingSkills",result.missing_skills,true);
    const sectionBox=document.getElementById("sections"); sectionBox.innerHTML="";
    Object.entries(result.sections).forEach(([name,found])=>{ const div=document.createElement("div"); div.className=`section-item ${found?"ok":"no"}`; div.textContent=`${found?"✓":"✗"} ${name}`; sectionBox.appendChild(div); });
    const suggestions=document.getElementById("suggestions"); suggestions.innerHTML="";
    result.suggestions.forEach(item=>{ const li=document.createElement("li"); li.textContent=item; suggestions.appendChild(li); });
    results.classList.remove("hidden"); results.scrollIntoView({behavior:"smooth"});
  }catch(error){ showMessage(error.message); }
  finally{ button.disabled=false; button.textContent="Analyze Resume"; }
});
