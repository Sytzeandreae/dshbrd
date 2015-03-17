var AppDispatcher = require('../../dshbrd/dispatcher/AppDispatcher');
var EventEmitter = require('events').EventEmitter;
var _ = require('underscore');

var XkcdApi = require('../utils/XkcdApi');
var XkcdConstants = require('../constants/XkcdConstants');

_data = {};

function setData(data) {
    _data = data;
}

var XkcdStore = _.extend({}, EventEmitter.prototype, {
    getData: function() {
        return _data;
    },

    fetchData: function(id) {
        XkcdApi.fetchData(id);
    },

    emitChange: function() {
        this.emit('change');
    },

    addChangeListener: function(callback) {
        this.on('change', callback);
    },

    removeChangeListener: function(callback) {
        this.removeEventListener('change', callback);
    }
});

AppDispatcher.register(function(payload) {
    var action = payload.action;

    switch (action.actionType) {
        case XkcdConstants.RECEIVE_DATA:
            setData(action.data);
            break;

        default:
            return true;
    }

    XkcdStore.emitChange();

    return true;
});

module.exports = XkcdStore;
