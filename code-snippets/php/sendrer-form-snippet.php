<?php
/**
 * Conditionally load the Sender.net script on specific pages using Page IDs.
 * DEBUGGING LOGGING ADDED (to console if WP_DEBUG is true).
 */
function custom_load_sender_net_script() {
  $target_page_ids = array( 5849 ); // Using only the confirmed ID for now.

  // Get current page ID.
  $current_page_id = get_the_ID(); 

  // Output console logs only if WP_DEBUG is enabled
  if ( defined('WP_DEBUG') && WP_DEBUG === true ) {
    echo '<script>';
    echo 'console.log("custom_load_sender_net_script: Function started.");';
    echo 'console.log("custom_load_sender_net_script: Checking current page ID (' . $current_page_id . ') against target IDs: ' . implode( ', ', $target_page_ids ) . '");';
    echo '</script>';
  }
    
  if ( in_array( $current_page_id, $target_page_ids ) ) {
    if ( defined('WP_DEBUG') && WP_DEBUG === true ) {
      echo '<script>console.log("custom_load_sender_net_script: Condition met (current page ID is in target_page_ids). Script will be output.");</script>';
    }
   ?>
   <script>
      (function (s, e, n, d, er) {
        s['Sender'] = er;
        s[er] = s[er] || function () {
          (s[er].q = s[er].q || []).push(arguments)
        }, s[er].l = 1 * new Date();
        var a = e.createElement(n),
            m = e.getElementsByTagName(n)[0];
        a.async = 1;
        a.src = d;
        m.parentNode.insertBefore(a, m)
      })(window, document, 'script', 'https://cdn.sender.net/accounts_resources/universal.js', 'sender');
      sender('5ca723f52d2904');
   </script>
   <?php
  } else {
    if ( defined('WP_DEBUG') && WP_DEBUG === true ) {
      echo '<script>console.log("custom_load_sender_net_script: Condition NOT met (current page ID ' . $current_page_id . ' not in target_page_ids). Script will NOT be output.");</script>';
    }
  }
}
add_action( 'wp_head', 'custom_load_sender_net_script' );