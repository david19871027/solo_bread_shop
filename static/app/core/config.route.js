angular.module('app')
    .config(function($stateProvider, $urlRouterProvider, $ocLazyLoadProvider, $authProvider, StripeCheckoutProvider, flowFactoryProvider) {
        $urlRouterProvider
            .otherwise('app2/ui/products');

        $stateProvider
            .state('app', {
                url: '/app',
                templateUrl: "/static/app/app.html"
            })
            .state('app2', {
                url: '/app2',
                templateUrl: "/static/app/app2.html" // No app-sidebar, the rest is the same with app.html
            })
            .state('app.dashboard', {
                url: '/dashboard',
                templateUrl: "/static/app/dashboard/dashboard.html"
            })
            .state('app2.login', {
                url: '/login',
                templateUrl: '/static/app/seller/templates/login.html'
            })
            .state('app2.ui-products', {
                url: '/ui/products',
                templateUrl: '/static/app/buy/templates/product_list.html'
            })
            .state('app2.product-detail', {
                url: '/ui/product/detail',
                templateUrl: '/static/app/buy/templates/product_detail.html'
            })
            .state('app2.product-add', {
                url: '/product/add',
                templateUrl: '/static/app/buy/templates/product_add.html'
            })
            .state('app2.page-about', {
                url: '/page/about',
                templateUrl: '/static/app/page/about.html'
            })
            .state('app2.page-cart', {
                url: '/page/cart',
                templateUrl: '/static/app/buy/templates/cart.html',
                resolve: {
                    stripe: StripeCheckoutProvider.load
                }
            })
            .state('app2.seller-profile', {
                url: '/seller/profile',
                templateUrl: '/static/app/seller/templates/profile.html'
            })
            .state('app2.seller-availability', {
                url: '/seller/availability',
                templateUrl: '/static/app/seller/templates/availability.html'
            })
            .state('404', {
                url: '/404',
                templateUrl: "/static/app/page-extra/404.html"
            })
            .state('500', {
                url: '/500',
                templateUrl: "/static/app/page-extra/500.html"
            })
            .state('maintenance', {
                url: '/maintenance',
                templateUrl: "/static/app/page-extra/maintenance.html"
            });

        $authProvider.oauth2({
            name: 'stripe',
            url: '/auth/stripe',
            clientId: 'ca_8Qcy5FPjST3HuFl7xXjisiodyjKE5d8V',
            redirectUri: window.location.origin || window.location.protocol + '//' + window.location.host,
            authorizationEndpoint: 'https://connect.stripe.com/oauth/authorize',
            scope: ['email'],
            scopeDelimiter: ',',
            display: 'popup',
            oauthType: '2.0',
            popupOptions: { width: 580, height: 400 }
        });

        StripeCheckoutProvider.defaults({
            key: "pk_test_egZpQehcB86xWgcr0n1eZluM"
        });

        flowFactoryProvider.defaults = {
            target: 'upload_product_photo',
            permanentErrors: [404, 500, 501],
            maxChunkRetries: 1,
            chunkRetryInterval: 5000,
            simultaneousUploads: 4,
            singleFile: true,
            testChunks:false
        };

        flowFactoryProvider.on('catchAll', function(event) {
            console.log('catchAll', arguments);
        });
    });
