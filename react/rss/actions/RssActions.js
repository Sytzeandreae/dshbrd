var AppDispatcher = require('../../dshbrd/dispatcher/AppDispatcher');
var DshbrdConstants = require('../constants/RssConstants');

var RssActions = {
    receiveData: function() {
        AppDispatcher.handleAction({
            actionType: RssConstants.RECEIVE_DATA,
            data: data
        }); 
    }
};

module.exports = RssActions;
