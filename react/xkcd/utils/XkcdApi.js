var XkcdActions = require('../actions/XkcdActions');
var Config = require('../../config');
var $ = require('jquery');

module.exports = {
    getData: function(id) {
        $.ajax({
            url: Config.BASE_URL + Config.API + '/block/xkcd/' + id,
            dataType: 'json',
            success: function(data) {
                XkcdActions.receiveData(data);
            }
        });
    }
};
