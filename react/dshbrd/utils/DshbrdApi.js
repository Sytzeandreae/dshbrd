var DshbrdActions = require('../actions/DshbrdActions');
var Config = require('../../config');
var $ = require('jquery');

module.exports = {
    getBlocksForUser: function() {
        $.ajax({
            url: Config.BASE_URL + Config.API + '/user/blocks',
            dataType: 'json',
            success: function(data) {
                DshbrdActions.receiveBlocks(data);
            }
        });
    }
};
