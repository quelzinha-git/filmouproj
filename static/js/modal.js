function abrirModal() {
    const modal = document.getElementById('meuModal');
    if (modal) modal.showModal();
}

function fecharModal() {
    const modal = document.getElementById('meuModal');
    if (modal) modal.close();
}

function abrirModalCadastro() {
    const modal = document.getElementById('modalCadastro');
    if (modal) modal.showModal();
}

function fecharModalCadastro() {
    const modal = document.getElementById('modalCadastro');
    if (modal) modal.close();
}

function dispararModal() {
    const modal = document.getElementById('meuModal');
    if (modal) modal.showModal();
}

function encerrarModal() {
    const modal = document.getElementById('meuModal');
    if (modal) modal.close();
}

document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('meuModal');
    const msg = modal ? modal.querySelector('h3') : null;

    if (msg && msg.textContent.trim() !== '' && !msg.textContent.includes('{{msg}}')) {
        dispararModal();
    }
});