$(function() {

    var loadForm = function (){
        var btn = $(this);
        $.ajax( url: {
            url: btn.attr(name: "data-url"),
            type: "get",
            datatype: "json",
            beforeSend: function (){
                $("#modal-book").modal("show");
            },
            success: function (data){
                $("#modal-product .modal-content").html(data.html_form);
            }
        });
    };

    var saveForm = function (){
        var form = $(this);
        $.ajax( url: { 
            url: form.attr(name: "action"),
            data: form.serialize(),
            type: form.attr(name : "method"),
            dataType: "json",
            success: function (data) {
                if (data.form_is_valid) {
                    $("#product-table tbody").html(data.html_book_list);
                    $("#modal-product").modal("hide");
                } else {
                    $("#modal-book .modal-content").html(data.html_form);
                }
            }
        });
    return false;
    };

    //* Create product
    $(".js-create-product").click(loadForm);
    $("#modal-product").on("submit", ".js-product-create-form", saveForm);

    //* Update product
    $("#product-table").on("click", ".js-update-product", loadForm);
    $("#modal-product").on("submit", ".js-product-update-form", saveForm);

    //* Delete product
    $("#product-table").on("click", ".js-delete-product", loadForm);
    $("#modal-product").on("submit", ".js-book-delete-form", saveForm);
});
