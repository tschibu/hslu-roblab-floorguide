<?xml version="1.0" encoding="UTF-8" ?>
<Package name="FloorGuide_Map" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="main" src="main" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs />
    <Resources>
        <File name="position" src="html/json/position.json" />
        <File name="map" src="html/json/map.json" />
        <File name="jquery-3.3.1" src="html/js/jquery-3.3.1.js" />
        <File name="init" src="html/js/init.js" />
        <File name="path" src="html/js/path.js" />
        <File name="index" src="html/index.html" />
        <File name="style" src="html/css/style.css" />
        <File name="ftp-sync" src=".vscode/ftp-sync.json" />
        <File name="index_dummy" src="html/index_dummy.html" />
        <File name="localwebserver" src="html/localwebserver.py" />
        <File name="showwebapp" src="showwebapp.py" />
        <File name="team10_room_guide" src="team10_room_guide.log" />
        <File name="polyfill" src="html/js/polyfill.js" />
    </Resources>
    <Topics />
    <IgnoredPaths>
        <Path src=".metadata" />
    </IgnoredPaths>
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
