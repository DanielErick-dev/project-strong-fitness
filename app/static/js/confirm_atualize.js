const confirmAtualize = (pk, name, lastname, sexo) => {
    event.preventDefault()
    Swal.fire({
        title: "Você têm certeza",
        text: sexo === 'M' ?  `que deseja atualizar o pagamento do aluno ${name} ${lastname} ?` : `que deseja atualizar o pagamento da aluna ${name} ${lastname} ?`,
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Sim, Atualizar"
    }).then((result) => {
        if (result.isConfirmed) {
            event.preventDefault()
            Swal.fire({
            title: "Atualizado",
            text: sexo === 'M' ? `pagamento do aluno ${name} realizado com sucesso` : `pagamento da aluna ${name} realizado com sucesso`,
            icon: "success",
            
            });
            setTimeout(() => {
                window.location.href = (`/atualize/${pk}/`)
            }, 2000)
        }
    });
            
    }
    