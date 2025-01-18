// API URL (replace with your API endpoint)
const apiUrl = "https://api.example.com/data"; 

// Function to fetch data from the API
async function fetchData() {
    try {
        const response = await fetch(apiUrl);
        const data = await response.json();
        updateTable(data);
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

// Function to update the table with fetched data
function updateTable(data) {
    const tableBody = document.querySelector("#dataTable tbody");
    tableBody.innerHTML = ""; // Clear existing rows

    data.forEach(item => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${item.id}</td>
            <td>${item.name}</td>
            <td>${item.value}</td>
        `;
        tableBody.appendChild(row);
    });
}

// Fetch data every 5 seconds
setInterval(fetchData, 5000);

// Initial fetch
fetchData();
