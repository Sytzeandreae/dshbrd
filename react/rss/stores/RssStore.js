var AppDispatcher = require('../../dshbrd/dispatcher/AppDispatcher');
var EventEmitter = require('events').EventEmitter;
var _ = require('underscore');

var RssApi = require('../utils/RssApi');
var RssConstants = require('../constants/RssConstants');

_data = {};

function setData(data) {
    _data = data;
}

var RssStore = _.extend({}, EventEmitter.prototype, {
    getData: function() {
        return _data; 
    },

    fetchData: function() {
        RssApi.fetchData(); 
    },

    emitChange: function() {
        this.emit('change');         
    },

    addChangeListener: function(callback) {
        this.on('change', callback);
    },

    removeChangeListener: function(callback){
        this.removeChangeListener('change', callback);
    }
});

AppDispatcher.register(function(payload) {
    var action = payload.action;
    var data = data;

    switch (action.actionType) {
        case RssConstants.RSS_FETCH_DATA:
            setData(action.data);
            break;

        default:
            return true;
    }

    RssStore.emitChange();

    return true;
});

module.exports = RssStore;
