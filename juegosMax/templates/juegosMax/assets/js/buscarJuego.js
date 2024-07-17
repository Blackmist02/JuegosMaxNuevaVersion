function fetchResults() {
    const query = document.getElementById('search-input').value;
    const resultsDropdown = document.getElementById('search-results');
    if (query.length > 0) {
        fetch(`/buscar?q=${query}`)
            .then(response => response.json())
            .then(data => {
                resultsDropdown.innerHTML = '';
                data.results.forEach(juego => {
                    const li = document.createElement('li');
                    li.classList.add('dropdown-item');
                    const a = document.createElement('a');
                    a.href = juego.url;
                    a.textContent = juego.nombre;
                    li.appendChild(a);
                    resultsDropdown.appendChild(li);
                });
                resultsDropdown.style.display = 'block';
            });
    } else {
        resultsDropdown.innerHTML = '';
        resultsDropdown.style.display = 'none';
    }
}