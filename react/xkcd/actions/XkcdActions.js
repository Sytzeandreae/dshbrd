var AppDispatcher = require('../../dshbrd/dispatcher/AppDispatcher');
var RssConstants = require('../constants/XkcdConstants');

var XkcdActions = {
    receiveData: function(data) {
        AppDispatcher.handleAction({
            actionType: XkcdConstants.RECEIVE_DATA,
            data: data
        });
    }
};

module.exports = XkcdActions;
