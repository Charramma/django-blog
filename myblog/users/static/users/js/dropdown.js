// bulma下拉组件（Dropdown）配套生效的js文件
// https://www.bulmacss.cn/article/read/6.htm
// $(document).ready(function () {
//     $(".dropdown .button").click(function () {
//         var dropdown = $(this).parents('.dropdown');
//         dropdown.toggleClass('is-active');
//         dropdown.focusout(function () {
//             $(this).removeClass('is-active');
//         });
//     });
// });

$(document).ready(function () {
    const dropdowns = document.querySelectorAll('.dropdown:not(.is-hoverable)');

    if (dropdowns.length > 0) {
    // For each dropdown, add event handler to open on click.
    dropdowns.forEach(function(el) {
        el.addEventListener('click', function(e) {
        e.stopPropagation();
        el.classList.toggle('is-active');
        });
    });

    // If user clicks outside dropdown, close it.
    document.addEventListener('click', function(e) {
        closeDropdowns();
    });
    }

    /*
    * Close dropdowns by removing `is-active` class.
    */
    function closeDropdowns() {
    dropdowns.forEach(function(el) {
        el.classList.remove('is-active');
    });
    }

    // Close dropdowns if ESC pressed
    document.addEventListener('keydown', function (event) {
    let e = event || window.event;
    if (e.key === 'Esc' || e.key === 'Escape') {
        closeDropdowns();
    }
    });
});
// $(document).ready(function() {
//     // Get all dropdowns on the page that aren't hoverable.
//     var dropdowns = document.querySelectorAll('.dropdown:not(.is-hoverable)');
  
//     if (dropdowns.length > 0) {
//       // For each dropdown, add event handler to open on click.
//       dropdowns.forEach(function(el) {
//         el.addEventListener('click', function(e) {
//         $(".dropdown-menu").toggle();
//           if (!el.classList.contains("is-active")) {
//             el.classList.toggle('is-active');
            
//             e.stopPropagation();
//             e.preventDefault();
//           }
//         });
//       });
  
//       // If user clicks outside dropdown, close it.
//       document.addEventListener('click', function(e) {
//         closeDropdowns();
//       });
//     }
  
//     /*
//      * Close dropdowns by removing `is-active` class.
//      */
//     function closeDropdowns() {
//       dropdowns.forEach(function(el) {
//         el.classList.remove('is-active');
//       });
//     }
  
//     // Close dropdowns if ESC pressed
//     document.addEventListener('keydown', function(event) {
//       let e = event || window.event;
//       if (e.key === 'Esc' || e.key === 'Escape') {
//         closeDropdowns();
//       }
//     });
//   });