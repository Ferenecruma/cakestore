const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value; // CSRF token for POST in fetch

    async function postData(url = '', data = {}) {
      const response = await fetch(url, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        mode: 'same-origin', // no-cors, *cors, same-origin
        headers: {
          'X-CSRFToken': csrftoken,
          'Content-Type': 'application/json',
          "X-Requested-With": "XMLHttpRequest",
        },
      });
      return response.json(); // parses JSON response into native JavaScript objects
    }

    function add_item_to_cart(item_id){
      let url = "/cart/add/" + String(item_id) + "/";
      let bottom = document.getElementById('bottom-' + String(item_id));
      let cart_icon = document.querySelector('.shopping-cart');

      postData(url, {'data': 'somedata'}).then(data => {
      console.log(data); // JSON data parsed by `data.json()` call
      });

      cart_icon.classList.add('shopping-cart-active')
      bottom.classList.add('clicked')
    }

    function delete_item_from_cart(item_id){
      let url = "/cart/remove/" + String(item_id) + "/";
      let bottom = document.getElementById('bottom-' + String(item_id));
      
      postData(url).then(data => {
      console.log(data); // JSON data parsed by `data.json()` call
      });

      bottom.classList.remove('clicked');
    }