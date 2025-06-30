document.addEventListener('DOMContentLoaded', function () {
    const tipoSelect = document.getElementById('tipo_veterinario');
    const centroContainer = document.getElementById('nombre-centro-container');

    if (tipoSelect) {
        tipoSelect.addEventListener('change', function () {
            if (this.value === 'CLIN') {
                centroContainer.style.display = 'block';
            } else {
                centroContainer.style.display = 'none';
            }
        });
    }
});
