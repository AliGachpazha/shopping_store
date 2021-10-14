function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

let content = $('#product-container');
let pagination = $('.pagination');



$.ajax({
    type: "Get",
    url: "http://127.0.0.1:8000/api-auth/product",
    dataType: "json",
    success: function (resp) {
        for (let product of resp.results)
            {

            $(content).append(`<div class="col-md-3 card bg-light">
                                   <div class="m-4">
                                       <h4><a href=${product.slug}> ${product.title}</a></h4>
                                        <img src=${product.image} alt="" class="img-fluid" style="height: 200px; object-fit: contain;">
                                         <p class="mt-3">Price: <strike>Rs. ${product.marked_price}</strike> Rs. ${product.selling_price}</p>
                                         <a href=${product.slug} class="btn btn-primary">Add To Cart</a>
                                    </div>
                            </div>`);


        }

        $(pagination).append(`<button id="previous" class="page btn btn-secondary btn-sm" onclick="page('${resp.previous}')">&laquo;</button>`)
        for (let i = 1; i <= resp.num_pages; i++) {
            if (i === 1) {
                $(pagination).append(`
                    <button class="active page btn btn-secondary btn-sm" onclick="('http://127.0.0.1:8000/api-auth/product/?page=${i}')" disabled>${i}</button>`)
            } else {
                $(pagination).append(`
                    <button class="page page btn btn-secondary btn-sm" onclick="page('http://127.0.0.1:8000/api-auth/product/?page=${i}')">${i}</button>`)
            }
        }
        $(pagination).append(`<button id="next" class="page btn btn-secondary btn-sm" onclick="page('${resp.next}')">&raquo;</button>`);

        $('#previous').prop('disabled', true);
    }
});

function page(url) {
    if (url != null) {
        $.ajax({
            type: "Get",
            url: `${url}`,
            dataType: "json",
            success: function (resp) {
                $(content).empty();
                for (let product of resp.results) {
                    $(content).append(`<div class="col-md-3 card bg-light">
                                   <div class="m-4">
                                       <h4><a href=${product.slug}> ${product.title}</a></h4>
                                        <img src=${product.image} alt="" class="img-fluid" style="height: 200px; object-fit: contain;">
                                         <p class="mt-3">Price: <strike>Rs. ${product.marked_price}</strike> Rs. ${product.selling_price}</p>
                                         <a href=${product.slug} class="btn btn-primary">Add To Cart</a>
                                    </div>
                            </div>`);
                }

                $(pagination).empty();
                $(pagination).append(`<button class="page page btn btn-secondary btn-sm" id="previous" onclick="page('${resp.previous}')">&laquo;</button>`)
                for (let i = 1; i <= resp.num_pages; i++) {
                    $(pagination).append(`
                        <button class="page page btn btn-secondary btn-sm" onclick="page('http://127.0.0.1:8000/api-auth/product/?page=${i}')">${i}</button>`)
                }
                $(pagination).append(`<button id="next" class="page page btn btn-secondary btn-sm" onclick="page('${resp.next}')">&raquo;</button>`);

                if (url === 'http://127.0.0.1:8000/api-auth/product') {
                    url = 'http://127.0.0.1:8000/api-auth/product';
                }

                $('.page').each(function () {
                    if ($(this).attr('onclick') === `page('${url}')`) {
                        $(this).attr('class', 'active');
                        $(this).prop('disabled', true);
                    }
                });

                if (resp.next == null) {
                    $('#next').prop('disabled', true);
                } else if (resp.previous == null) {
                    $('#previous').prop('disabled', true);
                }
            }
        });
    }
}