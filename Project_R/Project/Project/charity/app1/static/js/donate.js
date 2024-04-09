

    function EnableDisableTextBox() {
        var chkYes = document.getElementById("dtype_amt");
        var txtAmount = document.getElementById("amount");
        txtAmount.disabled = chkYes.checked ? false : true;
        if (!txtAmount.disabled) {
            txtAmount.focus();
        }
    }
