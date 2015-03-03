var AppDispatcher = require('../dispatcher/AppDispatcher');
var EventEmitter = require('events').EventEmitter;
var DshbrdConstants = require('../constants/DshbrdConstants');
var _ = require('underscore');

var _blocks = {};

function setBlocks(data) {
    _blocks = data;
}

var DshbrdStore = _.extend({}, EventEmitter.prototype, {
    getBlocks: function() {
        return _blocks;
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
    var data = data;

    switch (action.actionType) {
        case DshbrdConstants.RECEIVE_DATA:
            setBlocks(action.data);
            break;

        default:
            return true;
    }

    DshbrdStore.emitChange();

    return true;
});

module.exports = DshbrdStore;
