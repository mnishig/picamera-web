
deps-install:
	yarn add bulma


setup:
	install -d ./front/css
	cp ./node_modules/bulma/css/bulma.css ./front/css
	cp ./node_modules/bulma/css/bulma.css.map ./front/css
	install -d ./front/imgs
	cp ./material/photo_camera_black_36dp.svg ./front/imgs
	cp ./material/photo_camera_black_48dp.svg ./front/imgs
	cp ./material/settings_black_18dp.svg ./front/imgs
	cp ./material/settings_black_24dp.svg ./front/imgs
	cp ./material/settings_black_36dp.svg ./front/imgs
