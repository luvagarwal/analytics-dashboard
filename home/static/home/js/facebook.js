var currentdate = new Date();
var datetime = "Last Sync: " + currentdate.getDate() + "/"
+ (currentdate.getMonth()+1)  + "/"
+ currentdate.getFullYear() + " @ "
+ currentdate.getHours() + ":"
+ currentdate.getMinutes() + ":"
+ currentdate.getSeconds();

window.fbAsyncInit = function () {
	FB.init({
                appId: '1463271033954595',
                status: true,
                cookie: true,
                xfbml: true,
                oauth: true
        });
};

function updateButton(response) {
        if (response.authResponse) {
                FB.api('/me', function (info) {
                        login(response, info);
                });
        } else {
                FB.login(function (response) {
                        if (response.authResponse) {
                                FB.api('/me', function (info) {
                                        login(response, info);
                                });
                        } else {}
                }, {
                        scope: 'status_update,publish_stream,user_about_me'
                });
        }
}

function fb_invite() {
        FB.getLoginStatus(updateButton);
        FB.Event.subscribe('auth.statusChange', updateButton);
}(function () {
        var e = document.createElement('script');
        e.async = true;
        e.src = document.location.protocol + '//connect.facebook.net/en_US/all.js';
        document.getElementById('fb-root').appendChild(e);
}());

function login(response, info) {
        if (response.authResponse) {
                // console.log(response);
                var token = response.authResponse.accessToken;
                var userid = response.authResponse.userID;
                var provider = 'facebook';
                $.getJSON('https://graph.facebook.com/' + userid + '/friends?fields=name&access_token=' + token, function (result) {});
        }
}
var p;

function post_photo(object) {
        var u = object.id
        a = document.getElementsByClassName("img-responsive img-thumbnail")
        for (i = 0; i < 9; i++) {
                //   console.log(a[i].src);
                if (a[i].id == object.id) {
                        p = a[i].src;
			q=a[i].id;
                        console.log(p);
                        break;
                }
        }
        userid = getUserID();
        FB.ui({
                method: 'feed',
                type: 'photo',
                //console.log("photo"),
                picture: p,
                //console.log(q.image),
                link: 'localhost:8000/Analytics/follow?appid='+q+'&userid='+userid+'&datetime='+datetime,
        }, function (response) {});
}﻿ (function (i, s, o, g, r, a, m) {
        i['GoogleAnalyticsObject'] = r;
        i[r] = i[r] ||
        function () {
                (i[r].q = i[r].q || []).push(arguments)
        }, i[r].l = 1 * new Date();
        a = s.createElement(o), m = s.getElementsByTagName(o)[0];
        a.async = 1;
        a.src = g;
        m.parentNode.insertBefore(a, m)
})(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');
ga('create', 'UA-53496334-1');
ga('send', 'pageview');
