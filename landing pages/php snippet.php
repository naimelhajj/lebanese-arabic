<?php
/**
 * Smart Optimiser – v5.5 (A/B Test Script Interference Removed)
 * • All references to 'bt-conversion' have been removed to allow the A/B test
 *   plugin to load normally, pending investigation of its internal consent mode features.
 */

/* ─── helpers ────────────────────────────────────────────────────────── */
function ho_is_reservation() : bool {
	$slugs = [ 'reserve-lebanese-trial', 'book-lebanese-trial-v1', 'book-lebanese-trial-v2', 'lebanese-lessons' ];
	return !is_admin()
	       && !is_preview()
	       && is_page( $slugs );
}
function ho_is_home_v2() : bool {
    return !is_admin()
           && !is_preview()
           && is_page( 'home-v2' );
}
function ho_is_lesson() : bool {
	return !is_admin() && !is_preview()
	       && is_singular( 'post' )
	       && has_category( [ 'lessons', 'learn lebanese: videos', 'blogposts' ] );
}
function ho_has_ab_test() : bool {
	if ( ! ho_is_lesson() ) return false;
	global $post;
	return has_shortcode( $post->post_content, 'bt_bb_ab' ) ||
	       (bool) get_post_meta( $post->ID, '_fl_builder_ab_version', true );
}

/* ─── 0. silence MailMunch inline JS on specific pages ───────────── */
add_action( 'wp_footer', function () {
	if ( ho_is_reservation() || ho_is_home_v2() ) {
		if ( ! defined( 'MAILMUNCH_NO_RENDER' ) ) define( 'MAILMUNCH_NO_RENDER', true );
		remove_action( 'wp_footer', 'mailmunch_insert_script' );
	}
}, 999);

/* ─── 1. drop jquery-migrate everywhere ─────────────────────────────── */
add_action( 'wp_default_scripts', function ( $s ) {
	if ( ! ho_is_reservation() && ! ho_is_lesson() && ! ho_is_home_v2() ) return;
	if ( isset( $s->registered['jquery'] ) )
		$s->registered['jquery']->deps = [ 'jquery-core' ];
	$s->remove( 'jquery-migrate' );
}, 10);
add_action( 'wp_print_scripts', function () {
	if ( ho_is_reservation() || ho_is_lesson() || ho_is_home_v2() )
		wp_deregister_script( 'jquery-migrate' );
}, 100);

/* ─── 2. kill unused assets on specific pages ────────────────────── */
add_action( 'wp_enqueue_scripts', function () {
	if ( ! ho_is_reservation() && ! ho_is_home_v2() ) return;
	$kill = [
		'site','mailmunch','mailmunch-forms','mailmunch-popover',
		'wp-customer-reviews','wp-customer-reviews-css',
		'social-pug','social-pug-style','ai-share-summarize-css',
		'cv','cv-css','yarpp-thumbnails','yarpp-thumbnails-css',
	];
	foreach ( $kill as $h ) {
		wp_dequeue_style( $h );  wp_deregister_style( $h );
		wp_dequeue_script( $h ); wp_deregister_script( $h );
	}
}, 99);

/* ─── 3. smart-load heavy JS (defer & delay) ────────────────────── */
add_filter( 'script_loader_tag', function ( $tag, $handle ) {

	// Define which scripts to defer and which to delay
	$defer_handles = [];
	$delay_handles = [];

	if ( ho_is_reservation() || ho_is_home_v2() ) {
		// Defer theme scripts, but delay tracking scripts
		$defer_handles = [ 'astra-frontend' ];
		$delay_handles = [ 'pys-public', 'pys-tld', 'js-cookie' ];
	}
	elseif ( ho_is_lesson() ) {
		$defer_handles = [ 'astra-frontend', 'wp-customer-reviews', 'social-pug', 'site' ];
		// No scripts delayed on lesson pages for now
		$delay_handles = [];
	}
	else {
		return $tag; // Exit if not a target page
	}

	// Apply DEFER attribute
	if ( in_array( $handle, $defer_handles, true ) && ! str_contains( $tag, ' defer ' ) ) {
		return str_replace( ' src', ' defer src', $tag );
	}

	// Apply DELAY attribute (by changing 'src' to 'data-src')
	if ( in_array( $handle, $delay_handles, true ) ) {
		// Ensure it's a valid script tag with a src attribute
		if ( preg_match( '/<script\s+(.*?)src=[\'"]([^\'"]+)[\'"](.*?)>/i', $tag ) ) {
			return str_replace( ' src=', ' data-src=', $tag );
		}
	}

	return $tag;
}, 99, 2);

/* ─── 4. async-load Astra & plugin CSS (core block CSS untouched) ───── */
add_filter( 'style_loader_tag', function ( $html, $handle ) {

	if ( ho_is_reservation() || ho_is_home_v2() ) {
		$async = [ 'wp-customer-reviews-3-frontend','pt-cv-public-style','astra-theme-css','astra-menu-animation','ayudawp-aiss-styles','wp-block-library' ];
	}
	elseif ( ho_is_lesson() ) {
		$async = [ 'astra-main','astra-menu-animation','experiment-frontend',
		           'wp-customer-reviews-css','social-pug-style',
		           'ai-share-summarize-css','cv-css',
		           'spectra-block-positioning','uaspectra-block-css',
		           'content-views-bootstrap' ];
	}
	else return $html;

	if ( in_array( $handle, $async, true ) && ! str_contains( $html, 'rel=\'preload\'' ) ) {
		return str_replace(
			"rel='stylesheet'",
			"rel='preload' as='style' onload=\"this.onload=null;this.rel='stylesheet'\"",
			$html
		) . "<noscript>{$html}</noscript>";
	}
	return $html;
}, 99, 2);

/* ─── 5. resource hints ─────────────────────────────────────────────── */
add_action( 'wp_head', function () {
	if ( ho_is_reservation() ) : ?>
		<!-- Smart Optimiser is Active -->
		<link rel="preconnect" href="https://cdn.jotfor.ms" crossorigin>
		<link rel="preconnect" href="https://form.jotform.com" crossorigin>
		<link rel="preconnect" href="https://js.stripe.com" crossorigin>
		<link rel="preconnect" href="https://clickiocmp.com" crossorigin>
		<link rel="dns-prefetch" href="https://cdn.jotfor.ms">
		<link rel="dns-prefetch" href="//www.googletagmanager.com">
		<link rel="dns-prefetch" href="//connect.facebook.net">
	<?php elseif ( ho_is_home_v2() ) : ?>
        <!-- Smart Optimiser is Active for Home-V2 -->
        <link rel="preconnect" href="https://player.vimeo.com" crossorigin>
        <link rel="dns-prefetch" href="//player.vimeo.com">
        <link rel="dns-prefetch" href="//www.googletagmanager.com">
        <link rel="dns-prefetch" href="//connect.facebook.net">
    <?php endif;
}, 1);

/* ─── 6. delay JS on user interaction ────────────────────────────── */
add_action( 'wp_footer', function () {
	if ( ! ho_is_reservation() && ! ho_is_home_v2() ) return;

	// This script looks for <script> tags with a "data-src" attribute
	// and changes it to "src" upon the first user interaction.
	echo "<script type='text/javascript' id='ho-delay-js-loader'>
	const HO_DELAY_JS_EVENTS = ['scroll', 'mousemove', 'touchstart', 'click'];
	function HO_LOAD_DELAYED_JS() {
		HO_DELAY_JS_EVENTS.forEach(e => window.removeEventListener(e, HO_LOAD_DELAYED_JS, { passive: true }));
		document.querySelectorAll('script[data-src]').forEach(s => {
			s.setAttribute('src', s.getAttribute('data-src'));
			s.removeAttribute('data-src');
		});
	}
	HO_DELAY_JS_EVENTS.forEach(e => window.addEventListener(e, HO_LOAD_DELAYED_JS, { passive: true }));
	</script>";
}, 99);
