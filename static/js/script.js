
var splidelandingpage = new Splide( '#landing-page', {
    type: 'loop',
    autoplay: true,
    arrows: false,
    drag: true
} );
splidelandingpage.mount();

var splidebrands = new Splide( '#featured-brands-splide', {
    autoplay: true,
    gap: "1rem",
    perPage: 4,
    arrows: false,
    drag: true,
    breakpoints: {
		480: {
			perPage: 1,

		},
    }
} );
splidebrands.mount();


