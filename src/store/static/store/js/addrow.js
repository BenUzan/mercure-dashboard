
const order_form = document.querySelector('form');
const order_tbody  = document.querySelector('tbody');


function onAddWebsite(e){
    e.preventDefault();
   
    order_tbody.innerHTML += `
    
        <tr>
            <td>
                    <input type="datetime" name="row-1-date" id="row-1-date">
            
            </td>
            <td>
                    <input type="datetime" name="row-1-date" id="row-1-date">
                
            </td>
            <td>
                    <input type="datetime" name="row-1-date" id="row-1-date">
            
            </td>
            <td>
                    <input type="datetime" name="row-1-date" id="row-1-date">
            
            </td>
            <td>
                    <input type="datetime" name="row-1-date" id="row-1-date">
            
            </td>
            <td>
                    <input type="datetime" name="row-1-date" id="row-1-date">
            
            </td>
        </tr>
    `;
}

order_form.addEventListener("submit", onAddWebsite);