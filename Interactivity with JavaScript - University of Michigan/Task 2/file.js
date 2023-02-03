var form         = document.querySelector("form"),
    check        = document.getElementById("same"),
    fieldSet     = document.getElementsByTagName("fieldset")[1],
    shippingName = document.getElementById("shippingName"),
    shippingZip  = document.getElementById("shippingZip"),
    billingName  = document.getElementById("billingName"),
    billingZip   = document.getElementById("billingZip");

form.setAttribute("autocomplete", true);
fieldSet.style.display = "none";

function billingFunction() {
    if(check.checked) {
        fieldSet.style.display = "block";
        billingName.value = shippingName.value;
        billingZip.value  = shippingZip.value;
        billingName.setAttribute("required", true);
        billingZip.setAttribute("required", true)
    
    } else {
        fieldSet.style.display = "none";
        billingName.removeAttribute("required");
        billingZip.removeAttribute("required");
    }
}