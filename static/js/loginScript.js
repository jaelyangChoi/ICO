function onSignUp(googleUser) {
    const id_token = googleUser.getAuthResponse().id_token;

    let data = {'id_token': id_token};

    $.ajax({
        url: 'googleCallback',
        type: 'post',
        data: data,
        dataType: 'text',
        success: (result) => {
            alert(result);
            localStorage['id_token'] = id_token;
        },
        error: (result) => {
            alert(result);
        }
    });
}

function onSignIn(googleUser) {
    const id_token = googleUser.getAuthResponse().id_token;

    let data = {'id_token': id_token};

    $.ajax({
        url: 'googleCallback',
        type: 'post',
        data: data,
        dataType: 'text',
        success: (result) => {
            alert(result);
            localStorage['id_token'] = id_token;
        },
        error: (result) => {
            alert(result);
        }
    });
}