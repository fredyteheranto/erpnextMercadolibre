// Copyright (c) 2018, fredyteheranto and contributors
// For license information, please see license.txt

/*var script = document.createElement("script");
script.type = "text/javascript";
script.src = "/assets/mercadolibre/js/mercadolibre.js";
script.onload = function(){
console.log("Agent_Calculator Ldddddddaded");
};
 */
//document.head.appendChild(script);
frappe.render(frappe.templates.address_list, {[context]})
frappe.ui.form.on('mercadolibre', {
	
	refresh: function(frm) {
		console.log('fredy teheran tovar,',frm)
		$.get("http://dummy.restapiexample.com/api/v1/employees", function(data, status){
        console.log("Data: " + data + "\nStatus: " + status);
    	});


	}
});
