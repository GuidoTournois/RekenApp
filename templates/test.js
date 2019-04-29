$(document).ready(function(){

    $(".btn").click(function(){

        if ( $(this).attr('id') == {{juist}} ){
            console.log('juist');
        } else {
            console.log('fout');
        }

        setTimeout(
          function()
          {
                location.reload(true);
          }, 1000);

    });
});