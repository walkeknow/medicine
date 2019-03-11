// Drawer stuff
		$(".hamburger").click(function() {
			$(this).toggleClass("is-active");
			const nav = $("#nav-bar");
			if(nav.css("display") == 'none') {
				nav.show("slide", { direction: "right" }, 200);
				items = nav.find("ul").children();
				for(let i = 0; i < items.length; i++) {
					items.eq(i).show("slide", { direction: "left" }, i * 75 + 325);
				}
			} else {
				nav.hide('slide', {direction: 'right'}, 200);
				nav.find("ul").children().hide();
			}
		});