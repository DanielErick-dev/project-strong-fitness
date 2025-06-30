// Deixe claro que carregou
console.log('confirm_atualize.js foi carregado');

// Coloque a função no escopo global
window.confirmAtualize = (event, pk, name, lastname, sexo) => {
    console.log('confirmAtualize sendo executado');
    event.preventDefault();

    Swal.fire({
        title: "Você tem certeza?",
        text: sexo === 'M'
            ? `Deseja atualizar o pagamento do aluno ${name} ${lastname}?`
            : `Deseja atualizar o pagamento da aluna ${name} ${lastname}?`,
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Sim, Atualizar"
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: "Atualizado",
                text: sexo === 'M'
                    ? `Pagamento do aluno ${name} realizado com sucesso`
                    : `Pagamento da aluna ${name} realizado com sucesso`,
                icon: "success",
            });

            setTimeout(() => {
                window.location.href = `atualize/${pk}/`;
            }, 2000);
        }
    });
};
