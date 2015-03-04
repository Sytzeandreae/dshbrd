window.React = require('react');
var DshbrdApp = require('./dshbrd/components/DshbrdApp.react');
var DshbrdApi = require('./dshbrd/utils/DshbrdApi');


DshbrdApi.getBlocksForUser();


React.render(
    <DshbrdApp />,
    document.getElementById('app')    
);
