// Fonction pour afficher le graphique
function afficherGraphique() {
    // Récupération des données des cours de l'action Apple
    const ticker = 'AAPL';
    const url = `https://query1.finance.yahoo.com/v7/finance/download/${ticker}?period1=0&period2=999999999&interval=1d&events=history&includeAdjustedClose=true&format=json&corsDomain=finance.yahoo.com`;

    fetch(url)
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Erreur de connexion');
            }
        })
        .then(data => {
            // Création du graphique
            const labels = data['timestamp'].map(date => date.slice(0, 10));
            const values = data['close'].map(value => value);

            const ctx = document.getElementById('chart').getContext('2d');
            const chart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels,
                    datasets: [{
                        label: 'Cours',
                        data: values,
                        backgroundColor: 'rgba(255, 99, 132, 0.2)',
                        borderColor: 'rgba(255, 99, 132, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    title: {
                        display: true,
                        text: 'Cours de l\'action Apple'
                    },
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        })
        .catch(error => {
            // Affichage d'un graphique gris si la connexion échoue
            const ctx = document.getElementById('chart').getContext('2d');
            const chart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: [''],
                    datasets: [{
                        label: '',
                        data: [0],
                        backgroundColor: 'rgba(128, 128, 128, 0.2)',
                        borderColor: 'rgba(128, 128, 128, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    title: {
                        display: false
                    },
                    scales: {
                        y: {
                            display: false
                        }
                    }
                }
            });
        });
}

// Appel de la fonction pour afficher le graphique
afficherGraphique();