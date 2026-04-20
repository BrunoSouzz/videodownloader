document.getElementById('download-btn').addEventListener('click', function() {
    const videoUrl = document.getElementById('video-url').value;
    const statusMessage = document.getElementById('status-message');

    if (!videoUrl) {
        statusMessage.innerText = "Por favor, insira uma URL válida.";
        statusMessage.style.color = "#ff4444";
        return;
    }

    statusMessage.innerText = "Processando download... Aguarde.";
    statusMessage.style.color = "#38bdf8";

    window.location.href = `/download?url=${encodeURIComponent(videoUrl)}`;
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Rodando na porta ${PORT}`));