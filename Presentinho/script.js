const resposta = document.getElementById('texto')
resposta.addEventListener('submit', (read) => {
    const input = resposta.value
    if(input == 'eu'){
        alert('Acertou')
    }
    else{
        alert('Errou!')
    }
})

read()