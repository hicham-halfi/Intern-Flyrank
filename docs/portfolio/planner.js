"use strict";
const form=document.getElementById("budget-form");
const result=document.getElementById("budget-result");
function capacity(budget,rate,effort){
  if(![budget,rate,effort].every(Number.isFinite)||budget<0||rate<=0||effort<=0) return null;
  const unit=rate*effort;
  if(!Number.isFinite(unit)||unit<=0)return null;
  const pages=Math.floor((budget+Number.EPSILON)/unit);
  return {pages,hours:pages*effort,cost:pages*unit,remaining:Math.max(0,budget-pages*unit)};
}
form.addEventListener("submit",event=>{
  event.preventDefault();
  if(!form.reportValidity())return;
  const value=capacity(Number(form.elements.budget.value),Number(form.elements.rate.value),Number(form.elements.effort.value));
  if(!value){result.textContent="Enter a valid budget, positive rate, and positive review time.";return;}
  const money=new Intl.NumberFormat("en-US",{style:"currency",currency:"USD"});
  result.textContent=`${value.pages} complete review${value.pages === 1 ? "" : "s"} · ${value.hours.toFixed(2)} editor-hours · ${money.format(value.cost)} planned cost · ${money.format(value.remaining)} unallocated`;
});
