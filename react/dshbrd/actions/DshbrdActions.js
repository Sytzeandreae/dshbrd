var AppDispatcher = require('../dispatcher/AppDispatcher');
var DshbrdConstants = require('../constants/DshbrdConstants');

var DshbrdActions = {
    receiveBlocks: function() {
        AppDispatcher.handleAction({
            actionType: DshbrdConstants.RECEIVE_DATA,
            data: data
        });    
    }  
};

module.exports = DshbrdActions;
