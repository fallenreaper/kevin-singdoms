
const http = require("http")
const auth = require('./auth.json');

exports.login = (bot, args) => {
    console.log(`App Details: '${args.userID || ''}:${args.channelID || ''}'`)
    console.log("DUMP", args)
    get(`http://${auth.url}${auth.port ? ':' : ''}${auth.port}/link?channelId=${args.channelID}&characterId=${args.userID}`, () => {
        console.log(data)
        bot.sendMessage({
            to: args.channelID,
            message: data
        })
    });
}

const get = (url, fn) => {
    http.get(url, (response) => {
        data = ""
        response.on('data', (chunk) => {
            data += chunk;
        });
        response.on("end", () => fn(data))
    })
}

const CITADEL_INFO = {}
const CHANNEL_POLLING = new Map()
exports.turnOnPolling = (bot, args) => {
    this.turnOffPolling(bot, args)
    INTERVAL = 1000 * 60
    MINUTES = 0.25
    CHANNEL_POLLING.set(args.channelID, setInterval(() => {
        var data = '[{"chunk_arrival_time":"2020-03-27T14:31:02Z","extraction_start_time":"2020-03-13T14:33:10Z","moon_id":40348437,"natural_decay_time":"2020-03-27T17:31:02Z","structure_id":1029715999762},{"chunk_arrival_time":"2020-04-03T18:00:59Z","extraction_start_time":"2020-03-22T01:10:41Z","moon_id":40348461,"natural_decay_time":"2020-04-03T21:00:59Z","structure_id":1029718814021},{"chunk_arrival_time":"2020-04-07T19:01:00Z","extraction_start_time":"2020-03-25T01:30:17Z","moon_id":40348421,"natural_decay_time":"2020-04-07T22:01:00Z","structure_id":1031078668834}]'
        // get(`http://${auth.url}${auth.port ? ':' : ''}${auth.port}/getCitadelInfo?channelId=${args.channelID}`, (data) => {
            console.log(data)
            const d = JSON.parse(data)
            const now = new Date()
            for (let cit in d) {
                var message = ""
                if (!CITADEL_INFO[cit.structure_id] || CITADEL_INFO[cit.structure_id].extraction_start_time !== cit.extraction_start_time) {
                    CITADEL_INFO[cit.structure_id] = cit
                    CITADEL_INFO[cit.structure_id]["broadcastLevel"] = 0
                    message = `${cit.structureName || 'FOO'} has started Extractions.`
                }
                const arrival_time = new Date(CITADEL_INFO[cit.structure_id].chunk_arrival_time);
                const natural_decay_time = new Date(CITADEL_INFO[cit.structure_id].natural_decay_time);
                if ((arrival_time - now) < 0) {
                    if ((natural_decay_time - now) < INTERVAL * 60) {
                        // BLEW UP NOW
                        if (CITADEL_INFO[cit.structure_id]["broadcastLevel"] & 8 === 0) {
                            message = `${cit.structureName || 'FOO'} Achieved Critical Moon Mass`
                        }
                        CITADEL_INFO[cit.structure_id]["broadcastLevel"] |= 8;
                    } else {
                        // ARRIVED NOW
                        if (CITADEL_INFO[cit.structure_id]["broadcastLevel"] & 4 === 0) {
                            message = `${cit.structureName || 'FOO'} Moon Mass Ready for Harvest`
                        }
                        CITADEL_INFO[cit.structure_id]["broadcastLevel"] |= 4;
                    }
                } else if ((arrival_time - now) < INTERVAL * 60) {
                    // ARRIVES IN 1 HOUR
                    if (CITADEL_INFO[cit.structure_id]["broadcastLevel"] & 2 === 0) {
                        message = `${cit.structureName || 'FOO'} Moon Ready in 1 Hour.`
                    }
                    CITADEL_INFO[cit.structure_id]["broadcastLevel"] |= 2;
                } else if ((arrival_time - now) < INTERVAL * 60 * 24) {
                    // ARRIVES IN 24 HOURS
                    if (CITADEL_INFO[cit.structure_id]["broadcastLevel"] & 1 === 0) {
                        message = `${cit.structureName || 'FOO'} Moon Ready in 24 Hours.`
                    }
                    CITADEL_INFO[cit.structure_id]["broadcastLevel"] |= 1;
                }
                if (message)
                    bot.sendMessage({
                        to: args.channelID,
                        message
                    })
            }
        // })
    }, INTERVAL * MINUTES))
}
exports.turnOffPolling = (bot, args) => {
    const channel_interval = CHANNEL_POLLING.get(args.channelID);
    if (channel_interval) {
        clearInterval(channal_interval)
    }
}
