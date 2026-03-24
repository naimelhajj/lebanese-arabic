<?php
add_action('wp_head', function() {
	if (is_page('lebanese-lessons-v3')) {
        echo '<link rel="preload" fetchpriority="high" as="image" href="https://lebanese-arabic.com/wp-content/uploads/2025/10/girl-taking-lebanese-lessons-online.webp">';
	}
});

add_action('wp_head', function() {
	if (is_page('lebanese-lessons')) {
        echo '<link rel="preload" fetchpriority="high" as="image" href="https://lebanese-arabic.com/wp-content/uploads/2023/06/Blog-Header-1200x600-px-compressed-1024x512.webp imagesrcset="https://lebanese-arabic.com/wp-content/uploads/2023/06/Blog-Header-1200x600-px-compressed-1024x512.web 1024w, https://lebanese-arabic.com/wp-content/uploads/2023/06/Blog-Header-1200x600-px-compressed-300x150.webp 300w, https://lebanese-arabic.com/wp-content/uploads/2023/06/Blog-Header-1200x600-px-compressed-768x384.webp 768w, https://lebanese-arabic.com/wp-content/uploads/2023/06/Blog-Header-1200x600-px-compressed.webp 1200w" imagesizes="(max-width: 1024px) 100vw, 1024px" type="image/webp">';
	}
});

add_action('wp_head', function() {
	if (is_front_page() || is_page(['ppc-trial-offer', 'ppc-trial-offer-v2', 'ppc-trial-offer-v3'])) {
        echo '<link rel="preload" as="image" href="https://lebanese-arabic.com/wp-content/uploads/2025/11/lebanese-arabic-hero-compressed.jpg" imagesrcset="https://lebanese-arabic.com/wp-content/uploads/2025/11/lebanese-arabic-hero-compressed.jpg 768w, https://lebanese-arabic.com/wp-content/uploads/2025/11/lebanese-arabic-hero-compressed.jpg 1024w, https://lebanese-arabic.com/wp-content/uploads/2025/11/lebanese-arabic-hero-compressed.jpg 1410w" imagesizes="100vw" fetchpriority="high">';
	}
});