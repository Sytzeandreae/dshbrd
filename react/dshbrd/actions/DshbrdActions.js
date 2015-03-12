var AppDispatcher = require('../dispatcher/AppDispatcher');
var DshbrdConstants = require('../constants/DshbrdConstants');

var DshbrdActions = {
    receiveBlocks: function(data) {
        AppDispatcher.handleAction({
            actionType: DshbrdConstants.RECEIVE_DATA,
            data: data
        });    
    }  
};

module.exports = DshbrdActions;
