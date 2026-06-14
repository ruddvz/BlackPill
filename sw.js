/* Hospital in a Box - offline service worker (stale-while-revalidate) */
var CACHE = 'hib-v2';
var ASSETS = ['./','./index.html','./manifest.webmanifest','./icon-192.png','./icon-512.png','./icon-maskable-512.png','./icon-180.png','./heroes/cold.png','./heroes/cough.png','./heroes/blood-thinner.png','./heroes/upper-respiratory.png','./heroes/constipation.png','./heroes/fever.png','./heroes/headache.png','./heroes/indigestion.png','./heroes/nausea.png','./heroes/joint-pain.png','./heroes/diarrhea.png','./heroes/skin-rashes.png','./heroes/stomach-ache.png','./heroes/tooth-ache.png','./heroes/cuts-wounds.png','./heroes/burns.png','./heroes/ear-pain.png','./heroes/hypertension.png','./heroes/diabetes.png','./heroes/impotency.png','./heroes/female-reproductive.png','./heroes/tooth-powder.png','./heroes/head-wash.png','./heroes/face-wash.png','./heroes/heart-attack.png'];

self.addEventListener('install', function(e){
  e.waitUntil(caches.open(CACHE).then(function(c){return c.addAll(ASSETS);}).then(function(){return self.skipWaiting();}));
});
self.addEventListener('activate', function(e){
  e.waitUntil(caches.keys().then(function(keys){
    return Promise.all(keys.map(function(k){ if(k!==CACHE) return caches.delete(k); }));
  }).then(function(){ return self.clients.claim(); }));
});
self.addEventListener('fetch', function(e){
  if(e.request.method !== 'GET') return;
  e.respondWith(
    caches.match(e.request).then(function(cached){
      var net = fetch(e.request).then(function(resp){
        if(resp && resp.status===200 && resp.type==='basic'){
          var cp = resp.clone();
          caches.open(CACHE).then(function(c){ c.put(e.request, cp); });
        }
        return resp;
      }).catch(function(){ return cached; });
      return cached || net;
    })
  );
});
