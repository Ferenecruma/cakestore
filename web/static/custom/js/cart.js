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

    async function GetData(url = '') {
      const response = await fetch(url, {
        method: 'GET', // *GET, POST, PUT, DELETE, etc.
        mode: 'same-origin', // no-cors, *cors, same-origin
        headers: {
          "X-Requested-With": "XMLHttpRequest",
        },
      });
      return response.text(); // parses JSON response into native JavaScript objects
    }

    function change_cart_counter(count){
      let counter = document.getElementById('items-counter');
      counter.setAttribute('data-count', count);
      if (count === '0'){
        counter.classList.add("fa-stack-empty");
      }
      else{
        counter.classList.remove("fa-stack-empty");
      }
    }

    function add_item_to_cart(item_id){
      let url = "/cart/add/" + String(item_id) + "/";
      let bottom = document.getElementById('bottom-' + String(item_id));

      postData(url, {'data': 'somedata'}).then(data => {
      change_cart_counter(data['items_num'])
      });

      bottom.classList.add('clicked');
    }

    function delete_item_from_cart(item_id, reload=false){
      let url = "/cart/remove/" + String(item_id) + "/";
      let main_content = document.getElementById('content');

      postData(url).then(data => {
      change_cart_counter(data['items_num'])  // JSON data parsed by `data.json()` call
      });

      if (reload){
        GetData("/cart/").then(data  => {
          main_content.innerHTML = data });
      }
      else{
        let bottom = document.getElementById('bottom-' + String(item_id));
        bottom.classList.remove('clicked');
      }
    }
