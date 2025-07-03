function confirmDelete(pk, name, lastname) {
    Swal.fire({
        title: 'Tem certeza?',
        text: `Deseja excluir o aluno: ${name} ${lastname}?`,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Sim, Deletar'
    }).then((result) => {
        if (result.isConfirmed) {
            fetch(`/students/delete/${pk}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCSRFToken(),
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => {
                if (response.ok){
                    showToast('Aluno excluido com sucesso!', 'success');
                    setTimeout(() => {
                        window.location.href = '/students/list/'
                    }, 1500);
                } else {
                    showToast('Erro ao excluir Aluno!', 'error');
                }
            });
        }
    });
}

function getCSRFToken(){
    const cookie = document.cookie.split('; ').find(row => row.startsWith('csrftoken='));
    return cookie ? cookie.split('=')[1] : '';

}

function showToast(message, icon){
    Swal.fire({
        toast: true,
        position: 'top-end',
        icon: icon,
        title: message,
        showConfirmButton: false,
        timer: 2000,
        timerProgressBar: true,
    });
}