

exports.login = (bot, args) => {
    console.log(`App Details: '${args.userID || ''}:${args.channelID||''}'`)
    console.log("DUMP", args)
    bot.sendMessage({
        to: args.channelID,
        message: `WIN.`
    })
}
