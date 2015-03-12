var RssActions = require('../actions/RssActions');
var Config = require('../../config');
var $ = require('jquery');

module.exports = {
    getData: function(id) {
        $.ajax({
            url: Config.BASE_URL + Config.API + '/block/rss/' + id,
            dataType: 'json',
            success: function(data) {
                RssActions.receiveData(data);
            }
        });
    },

    fetchData: function(url) {
        $.ajax({
            
        })
    }
};
