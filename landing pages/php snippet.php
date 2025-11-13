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

/* ─── 3. defer heavy JS ─────────────────────────────────────────────── */
add_filter( 'script_loader_tag', function ( $tag, $handle ) {

	if ( ho_is_reservation() || ho_is_home_v2() ) {
		$defer = [ 'astra-frontend','pys-public','pys-tld','js-cookie' ];
	}
	elseif ( ho_is_lesson() ) {
		$defer = [ 'astra-frontend','pys-public','pys-tld','js-cookie',
		           'wp-customer-reviews','social-pug','site' ];
	}
	else return $tag;

	return in_array( $handle, $defer, true ) && ! str_contains( $tag, ' defer ' )
		? str_replace( ' src', ' defer src', $tag )
		: $tag;
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
