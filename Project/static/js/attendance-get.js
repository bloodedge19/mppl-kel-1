// section fetch
// api url
const api_url =
	"/api-overtime";

// Defining async function
async function getapi(url) {
	
	// Storing response
	const response = await fetch(url, {	
		method: 'GET',
		credentials: 'include'
	});
	// Storing data in form of JSON
	var data = await response.json();
	console.log(data);
	console.log(data.list)
	show(data);
	
}
// Calling that async function
getapi(api_url);

// Function to define innerHTML for HTML table
function show(data) {
	let tab =
		`<tr>
		<th>Date</th>
		<th>Start Time</th>
		<th>End time</th>
		<th>Working Hours</th>
		</tr>`;
	
	// Loop to access all rows
	for (let r of data) {
		tab += `<tr>
	<td>${r.date} </td>
	<td>${r.start}</td>
	<td>${r.end}</td>
	<td>${r.working_hours}</td>		
</tr>`;
	}
	// Setting innerHTML as tab variable
	document.getElementById("attendance-table").innerHTML = tab;
}