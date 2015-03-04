var RssActions = require('../actions/RssActions');
var Config = require('../../config');
var $ = require('jquery');

module.exports = {
    getData: function() {
        $.ajax({
            url: Config.BASE_URL + Config.API + '/rss/' + id,
            dataType: 'json',
            success: function(data) {
                RssActions.receiveData(data);
            }
        });
    }
};
