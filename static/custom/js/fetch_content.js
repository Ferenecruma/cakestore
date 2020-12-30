function AjaxFetch(id, url){

    document.querySelector(id).addEventListener(
    "click",
    function fetch_categories(event)
    {
      event.preventDefault();
      $.ajax(url, {
            type: 'get',
            success: function(result) {
                // success code execution here
                $('#content').html(result); // Update UI.
                let mq = window.matchMedia( "(max-width: 768px)" );
                if (mq.matches){
                    NavSlide(); // Navbar slider animation
                };
            },
            error: function(xhr,status,error) {
                // error code here
            },
            complete: function(xhr,status) {
                // completion code here
            }
        });
    },
    false);
  };
