var AppDispatcher = require('../../dshbrd/dispatcher/AppDispatcher');
var RssConstants = require('../constants/RssConstants');

var RssActions = {
    receiveData: function(data) {
        AppDispatcher.handleAction({
            actionType: RssConstants.RECEIVE_DATA,
            data: data
        }); 
    }
};

module.exports = RssActions;
