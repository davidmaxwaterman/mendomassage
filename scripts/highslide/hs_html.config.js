hs.graphicsDir = 'scripts/highslide/graphics/';
hs.showCredits = false;
hs.outlineType = 'custom';
hs.dimmingOpacity = 0.2;
hs.align = 'center';
// hs.headingEval = 'this.thumb.alt';
hs.registerOverlay({
	html: '<div class="closebutton" onclick="return hs.close(this)" title="Close"></div>',
	position: 'top right',
	useOnHtml: true
});

