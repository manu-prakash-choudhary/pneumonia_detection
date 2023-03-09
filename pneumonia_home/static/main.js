// let submitBtn= document.querySelector('#submit_img')
// let image = document.getElementById('file')

// // submitBtn.addEventListener('click',function (e) {
    
// //         imgData = image.toDataURL();
// //         var url1 = "http://127.0.0.1:5000/predict"
// //     console.log(imgData)
    
// //         $.post(url1, {
// //             image_data: imgData
// //         }, function (result) {
// //             console.log(result)
// //         });
// //     e.preventDefault();
    
// // })

// function base64ToBlob(base64, mime) 
// {
//     mime = mime || '';
//     var sliceSize = 1024;
//     var byteChars = window.atob(base64);
//     var byteArrays = [];

//     for (var offset = 0, len = byteChars.length; offset < len; offset += sliceSize) {
//         var slice = byteChars.slice(offset, offset + sliceSize);

//         var byteNumbers = new Array(slice.length);
//         for (var i = 0; i < slice.length; i++) {
//             byteNumbers[i] = slice.charCodeAt(i);
//         }

//         var byteArray = new Uint8Array(byteNumbers);

//         byteArrays.push(byteArray);
//     }

//     return new Blob(byteArrays, {type: mime});
// }

// // $( '#submit_img' )
// //   .submit( function( e ) {
// //     $.ajax( {
// //       url: 'http://127.0.0.1:5000/predict/',
// //       type: 'POST',
// //       data: image,
// //       processData: false,
// //       contentType: false
// //     } );
// //     e.preventDefault();
// //   } );
