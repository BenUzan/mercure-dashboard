function printInvoice() {
    window.print();
}

function addNewRow() {
    const tbody = document.querySelector('tbody');
    var code = document.order.code.value;
    var name = document.order.name.value;
    var qty = document.order.qty.value;
    var pu = document.order.pu.value;
    var discount = document.order.discount.value;

    var pt = qty * pu;

    var tr = document.createElement('tr');

    var td1 = tr.appendChild(document.createElement('td'));
    var td2 = tr.appendChild(document.createElement('td'));
    var td3 = tr.appendChild(document.createElement('td'));
    var td4 = tr.appendChild(document.createElement('td'));
    var td5 = tr.appendChild(document.createElement('td'));
    var td6 = tr.appendChild(document.createElement('td'));
    var td7 = tr.appendChild(document.createElement('td'));

    td1.innerHTML = '<input class="form-control" type="text" name="' + code + '" id="" value="' + code + '" disabled>';
    td2.innerHTML = '<input class="form-control" type="text" name="" id="" value="' + name + '" disabled>'
    td3.innerHTML = '<input class="form-control" type="number" name="" id="" value="' + qty + '" disabled>'
    td4.innerHTML = '<input class="form-control" type="number" name="" id="" value="' + pu + '" disabled>'
    td5.innerHTML = '<input class="form-control" type="number" name="" id="" value="' + discount + '" disabled>'
    td6.innerHTML = '<input class="form-control" type="number" name="quantity" id="" value="' + pt + '" disabled>'
    td7.innerHTML = '<input class="btn btn-outline-danger" type="button" name="delete" value="Supprimer" onclick="delRow(this);">'

    // document.getElementById("myTable").appendChild(tr);
    document.getElementById("code").value = "";
    document.getElementById("name").value = "";
    document.getElementById("qty").value = "";
    document.getElementById("pu").value = "";
    document.getElementById("discount").value = "";

    tbody.appendChild(tr);

}

function delRow(product) {
    var row = product.parentNode.parentNode;
    row.parentNode.removeChild(row);
    
}


const table = new DataTable('#myTable', {
    columnDefs: [
        {
            "targets": 0,
            "searchable": false
        }
    ]
});


// document.querySelector('#addRow').addEventListener('click', addNewRow);