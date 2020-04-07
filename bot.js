
var Discord = require('discord.io');
var logger = require('winston');
var auth = require('./auth.json');
var utils = require("./utils.js")
// Configure logger settings
logger.remove(logger.transports.Console);
logger.add(new logger.transports.Console, {
    colorize: true
});
logger.level = 'debug';
// Initialize Discord Bot
var bot = new Discord.Client({
    token: auth.token,
    autorun: true
});
bot.on('ready', function (evt) {
    logger.info('Connected');
    logger.info('Logged in as: ');
    logger.info(bot.username + ' - (' + bot.id + ')');
});
bot.on('message', function (user, userID, channelID, message, evt) {
    console.log("Bot", Object.values(bot.servers[evt.d.guild_id].roles))
    var roles = Object.values(bot.servers[evt.d.guild_id].roles)
    var adminRoles = roles.filter(r => r._permissions & 0x8 === 0x8)
    var isAdmin = evt.d.member.roles.map(roleId => bot.servers[evt.d.guild_id].roles[roleId]).filter(r => r._permissions & 0x8 === 0x8).length > 0
    console.log(`All Roles: ${roles.map(r => r.name)}\nAdmin Roles: ${adminRoles.map(r => r.name)}`)
    if (evt.d.author.bot) return;
    if (message.substring(0, 1) != "!") return
    var args = message.substring(1).split(' ');
    var cmd = args[0];
    args = args.splice(1);
    switch (cmd) {
        // !ping
        case 'ping':
            bot.sendMessage({
                to: channelID,
                message: 'Pong!'
            });
            break;
        // Just add any case commands if you want to..
        case "whoami":
            bot.sendMessage({
                to: channelID,
                message: `${userID}: ${user}`
            })
            break;
        case "link":
        case "login":
            if (!isAdmin) return;
            utils.login(bot, {
                user, userID, channelID, message, evt
            })
            break;

        case "init":
            bot.sendMessage({
                to: channelID,
                message: "Initializing...."
            })
            utils.turnOnPolling(bot, {
                user, userID, channelID, message, evt
            });
            break
        case "shutdown":
            utils.turnOnPolling(bot, {
                user, userID, channelID, message, evt
            });
            break;
    }
});

