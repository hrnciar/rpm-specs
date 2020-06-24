#
# Fedora spec file for drupal8
#
# Copyright (c) 2013-2020 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

# Disable automatic requires/provides processing
AutoReqProv: no

# core/composer.json
## "php": ">=7.0.8"
%global php_min_ver 7.0.8
## "asm89/stack-cors": "^1.1"
%global asm89_stack_cors_min_ver 1.1
%global asm89_stack_cors_max_ver 2.0
## "composer/semver": "^1.0"
%global composer_semver_min_ver 1.0
%global composer_semver_max_ver 2.0
## "doctrine/annotations": "^1.4"
%global doctrine_annotations_min_ver 1.4
%global doctrine_annotations_max_ver 2.0
## "doctrine/common": "^2.7"
%global doctrine_common_min_ver 2.7
%global doctrine_common_max_ver 3.0
## "easyrdf/easyrdf": "^0.9"
%global easyrdf_min_ver 0.9
%global easyrdf_max_ver 1.0
## "egulias/email-validator": "^2.0"
%global email_validator_min_ver 2.0
%global email_validator_max_ver 3.0
## "guzzlehttp/guzzle": "^6.3"
%global guzzle_min_ver 6.3
%global guzzle_max_ver 7.0
## "laminas/laminas-diactoros": "^1.8"
%global laminas_diactoros_min_ver 1.8
%global laminas_diactoros_max_ver 2.0
## "laminas/laminas-feed": "^2.12"
%global laminas_feed_min_ver 2.12
%global laminas_feed_max_ver 3.0
## "masterminds/html5": "^2.1"
%global masterminds_html5_min_ver 2.1
%global masterminds_html5_max_ver 3.0
## "pear/archive_tar": "^1.4.9"
%global pear_archive_tar_min_ver 1.4.9
%global pear_archive_tar_max_ver 2
## "phpunit/phpunit": "^4.8.35 || ^6.5"
%global phpunit_min_ver 4.8.35
## "psr/log": "^1.0"
%global psr_log_min_ver 1.0
%global psr_log_max_ver 2.0
## "stack/builder": "^1.0"
%global stack_builder_min_ver 1.0
%global stack_builder_max_ver 2.0
## "symfony/class-loader": "~3.4.0"
## "symfony/console": "~3.4.0"
## "symfony/dependency-injection": "~3.4.26"
## "symfony/event-dispatcher": "~3.4.0"
## "symfony/http-foundation": "~3.4.35"
## "symfony/http-kernel": "~3.4.14"
## "symfony/process": "~3.4.0"
## "symfony/routing": "~3.4.0"
## "symfony/serializer": "~3.4.0"
## "symfony/translation": "~3.4.0"
## "symfony/validator": "~3.4.0"
## "symfony/yaml": "~3.4.5"
%global symfony_min_ver 3.4.35
%global symfony_max_ver 4.0.0
## "symfony-cmf/routing": "^1.4"
%global symfony_cmf_routing_min_ver 1.4
%global symfony_cmf_routing_max_ver 2.0
## "symfony/psr-http-message-bridge": "^1.1.2"
%global symfony_psr_http_message_bridge_min_ver 1.1.2
%global symfony_psr_http_message_bridge_max_ver 2.0
## "twig/twig": "^1.38.2"
%global twig_min_ver 1.38.2
%global twig_max_ver 2.0
## "typo3/phar-stream-wrapper": "^3.1.3"
%global typo3_phar_stream_wrapper_min_ver 3.1.3
%global typo3_phar_stream_wrapper_max_ver 4.0

# composer.json
## "composer/installers": "^1.2"
### Note: No requirement because composer installs not supported

# Build using "--with tests" to enable tests
%global with_tests 0%{?_with_tests:1}

# Drupal 8 directories
%global drupal8      %{_datadir}/%{name}
%global drupal8_var  %{_localstatedir}/lib/%{name}
%global drupal8_conf %{_sysconfdir}/%{name}

%{!?phpdir:  %global phpdir  %{_datadir}/php}


Name:      drupal8
Version:   8.9.0
Release:   1%{?dist}
Summary:   An open source content management platform

# Licenses:
# - GPLv2+
#     - Drupal 8 itself
#     - core/assets/vendor/farbtastic (bundled)
#     - core/assets/vendor/html5shiv (bundled)
#     - core/assets/vendor/jquery-form (bundled)
#     - core/assets/vendor/jquery-once (bundled)
#     - core/assets/vendor/jquery-ui-touch-punch (bundled)
# - MIT
#     - core/assets/vendor/backbone (bundled)
#     - core/assets/vendor/domready (bundled)
#     - core/assets/vendor/jquery (bundled)
#     - core/assets/vendor/jquery-joyride (bundled)
#     - core/assets/vendor/jquery.cookie (bundled)
#     - core/assets/vendor/matchMedia (bundled)
#     - core/assets/vendor/modernizr (bundled)
#     - core/assets/vendor/normalize-css (bundled)
#     - core/assets/vendor/picturefill (bundled)
#     - core/assets/vendor/popperjs (bundled)
#     - core/assets/vendor/sortable (bundled)
#     - core/assets/vendor/underscore (bundled)
#     - core/vendor/composer (generated autoloader)
# - Pubic Domain
#     - core/assets/vendor/classList (bundled)
#     - core/assets/vendor/jquery.ui (bundled)
# - GPLv2+ or MPLv1.1+ or LGPLv2.1+
#     - core/assets/vendor/ckeditor (bundled)
License:   GPLv2+ and MIT and Public Domain and (GPLv2+ or MPLv1.1+ or LGPLv2+)

URL:       https://www.drupal.org/8
Source0:   http://ftp.drupal.org/files/projects/drupal-%{version}.tar.gz
# RPM README
Source1:   %{name}-README.md
# rpmbuild subpackage license
Source2:   %{name}-rpmbuild-LICENSE.txt
# Autoloader
Source3:   %{name}-autoload.php
# rpmbuild
Source4:   macros.%{name}
Source5:   %{name}.attr
Source6:   %{name}-find-provides.php
Source7:   %{name}-find-requires.php
Source8:   %{name}-get-dev-source.sh
Source9:   %{name}-prep-licenses-and-docs.sh
# Apache HTTPD conf
Source10:  %{name}.conf

BuildArch: noarch
# Version check
BuildRequires: php-cli
# Needed for %%pear_phpdir macro
BuildRequires: php-pear
# Scripts
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(symfony/console) >= %{symfony_min_ver} with php-composer(symfony/console) < %{symfony_max_ver})
%else
BuildRequires: php-composer(symfony/console) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/console) <  %{symfony_max_ver}
%endif
# Autoloader
BuildRequires: composer

# "/usr/bin/env php" usage
Requires:  php-cli
# core/composer.json
Requires:  php(language) >= %{php_min_ver}
Requires:  php-composer(phpunit/phpunit) >= %{phpunit_min_ver}
Requires:  php-date
Requires:  php-dom
Requires:  php-filter
Requires:  php-gd
Requires:  php-hash
Requires:  php-json
Requires:  php-pcre
Requires:  php-pdo
Requires:  php-session
Requires:  php-simplexml
Requires:  php-spl
Requires:  php-tokenizer
Requires:  php-xml
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:  (php-composer(asm89/stack-cors) >= %{asm89_stack_cors_min_ver} with php-composer(asm89/stack-cors) < %{asm89_stack_cors_max_ver})
Requires:  (php-composer(composer/semver) >= %{composer_semver_min_ver} with php-composer(composer/semver) < %{composer_semver_max_ver})
Requires:  (php-composer(doctrine/annotations) >= %{doctrine_annotations_min_ver} with php-composer(doctrine/annotations) < %{doctrine_annotations_max_ver})
Requires:  (php-composer(doctrine/common) >= %{doctrine_common_min_ver} with php-composer(doctrine/common) < %{doctrine_common_max_ver})
Requires:  (php-composer(easyrdf/easyrdf) >= %{easyrdf_min_ver} with php-composer(easyrdf/easyrdf) < %{easyrdf_max_ver})
Requires:  (php-composer(egulias/email-validator) >= %{email_validator_min_ver} with php-composer(egulias/email-validator) < %{email_validator_max_ver})
Requires:  (php-composer(guzzlehttp/guzzle) >= %{guzzle_min_ver} with php-composer(guzzlehttp/guzzle) < %{guzzle_max_ver})
Requires:  (php-composer(laminas/laminas-diactoros) >= %{laminas_diactoros_min_ver} with php-composer(laminas/laminas-diactoros) < %{laminas_diactoros_max_ver})
Requires:  (php-composer(laminas/laminas-feed) >= %{laminas_feed_min_ver} with php-composer(laminas/laminas-feed) < %{laminas_feed_max_ver})
Requires:  (php-composer(masterminds/html5) >= %{masterminds_html5_min_ver} with php-composer(masterminds/html5) < %{masterminds_html5_max_ver})
Requires:  (php-composer(psr/log) >= %{psr_log_min_ver} with php-composer(psr/log) < %{psr_log_max_ver})
Requires:  (php-composer(stack/builder) >= %{stack_builder_min_ver} with php-composer(stack/builder) < %{stack_builder_max_ver})
Requires:  (php-composer(symfony-cmf/routing) >= %{symfony_cmf_routing_min_ver} with php-composer(symfony-cmf/routing) < %{symfony_cmf_routing_max_ver})
Requires:  (php-composer(symfony/class-loader) >= %{symfony_min_ver} with php-composer(symfony/class-loader) < %{symfony_max_ver})
Requires:  (php-composer(symfony/config) >= %{symfony_min_ver} with php-composer(symfony/config) < %{symfony_max_ver})
Requires:  (php-composer(symfony/console) >= %{symfony_min_ver} with php-composer(symfony/console) < %{symfony_max_ver})
Requires:  (php-composer(symfony/dependency-injection) >= %{symfony_min_ver} with php-composer(symfony/dependency-injection) < %{symfony_max_ver})
Requires:  (php-composer(symfony/event-dispatcher) >= %{symfony_min_ver} with php-composer(symfony/event-dispatcher) < %{symfony_max_ver})
Requires:  (php-composer(symfony/http-foundation) >= %{symfony_min_ver} with php-composer(symfony/http-foundation) < %{symfony_max_ver})
Requires:  (php-composer(symfony/http-kernel) >= %{symfony_min_ver} with php-composer(symfony/http-kernel) < %{symfony_max_ver})
Requires:  (php-composer(symfony/process) >= %{symfony_min_ver} with php-composer(symfony/process) < %{symfony_max_ver})
Requires:  (php-composer(symfony/psr-http-message-bridge) >= %{symfony_psr_http_message_bridge_min_ver} with php-composer(symfony/psr-http-message-bridge) < %{symfony_psr_http_message_bridge_max_ver})
Requires:  (php-composer(symfony/routing) >= %{symfony_min_ver} with php-composer(symfony/routing) < %{symfony_max_ver})
Requires:  (php-composer(symfony/serializer) >= %{symfony_min_ver} with php-composer(symfony/serializer) < %{symfony_max_ver})
Requires:  (php-composer(symfony/translation) >= %{symfony_min_ver} with php-composer(symfony/translation) < %{symfony_max_ver})
Requires:  (php-composer(symfony/validator) >= %{symfony_min_ver} with php-composer(symfony/validator) < %{symfony_max_ver})
Requires:  (php-composer(symfony/yaml) >= %{symfony_min_ver} with php-composer(symfony/yaml) < %{symfony_max_ver})
Requires:  (php-composer(twig/twig) >= %{twig_min_ver} with php-composer(twig/twig) < %{twig_max_ver})
Requires:  (php-composer(typo3/phar-stream-wrapper) >= %{typo3_phar_stream_wrapper_min_ver} with php-composer(typo3/phar-stream-wrapper) < %{typo3_phar_stream_wrapper_max_ver})
Requires:  (php-pear(Archive_Tar) >= %{pear_archive_tar_min_ver} with php-pear(Archive_Tar) < %{pear_archive_tar_max_ver})
%else
Requires:  php-composer(asm89/stack-cors) <  %{asm89_stack_cors_max_ver}
Requires:  php-composer(asm89/stack-cors) >= %{asm89_stack_cors_min_ver}
Requires:  php-composer(composer/semver) <  %{composer_semver_max_ver}
Requires:  php-composer(composer/semver) >= %{composer_semver_min_ver}
Requires:  php-composer(doctrine/annotations) <  %{doctrine_annotations_max_ver}
Requires:  php-composer(doctrine/annotations) >= %{doctrine_annotations_min_ver}
Requires:  php-composer(doctrine/common) <  %{doctrine_common_max_ver}
Requires:  php-composer(doctrine/common) >= %{doctrine_common_min_ver}
Requires:  php-composer(easyrdf/easyrdf) <  %{easyrdf_max_ver}
Requires:  php-composer(easyrdf/easyrdf) >= %{easyrdf_min_ver}
Requires:  php-composer(egulias/email-validator) <  %{email_validator_max_ver}
Requires:  php-composer(egulias/email-validator) >= %{email_validator_min_ver}
Requires:  php-composer(guzzlehttp/guzzle) <  %{guzzle_max_ver}
Requires:  php-composer(guzzlehttp/guzzle) >= %{guzzle_min_ver}
Requires:  php-composer(laminas/laminas-diactoros) <  %{laminas_diactoros_max_ver}
Requires:  php-composer(laminas/laminas-diactoros) >= %{laminas_diactoros_min_ver}
Requires:  php-composer(laminas/laminas-feed) <  %{laminas_feed_max_ver}
Requires:  php-composer(laminas/laminas-feed) >= %{laminas_feed_min_ver}
Requires:  php-composer(masterminds/html5) <  %{masterminds_html5_max_ver}
Requires:  php-composer(masterminds/html5) >= %{masterminds_html5_min_ver}
Requires:  php-composer(psr/log) <  %{psr_log_max_ver}
Requires:  php-composer(psr/log) >= %{psr_log_min_ver}
Requires:  php-composer(stack/builder) <  %{stack_builder_max_ver}
Requires:  php-composer(stack/builder) >= %{stack_builder_min_ver}
Requires:  php-composer(symfony-cmf/routing) <  %{symfony_cmf_routing_max_ver}
Requires:  php-composer(symfony-cmf/routing) >= %{symfony_cmf_routing_min_ver}
Requires:  php-composer(symfony/class-loader) <  %{symfony_max_ver}
Requires:  php-composer(symfony/class-loader) >= %{symfony_min_ver}
Requires:  php-composer(symfony/config) <  %{symfony_max_ver}
Requires:  php-composer(symfony/config) >= %{symfony_min_ver}
Requires:  php-composer(symfony/console) <  %{symfony_max_ver}
Requires:  php-composer(symfony/console) >= %{symfony_min_ver}
Requires:  php-composer(symfony/dependency-injection) <  %{symfony_max_ver}
Requires:  php-composer(symfony/dependency-injection) >= %{symfony_min_ver}
Requires:  php-composer(symfony/event-dispatcher) <  %{symfony_max_ver}
Requires:  php-composer(symfony/event-dispatcher) >= %{symfony_min_ver}
Requires:  php-composer(symfony/http-foundation) <  %{symfony_max_ver}
Requires:  php-composer(symfony/http-foundation) >= %{symfony_min_ver}
Requires:  php-composer(symfony/http-kernel) <  %{symfony_max_ver}
Requires:  php-composer(symfony/http-kernel) >= %{symfony_min_ver}
Requires:  php-composer(symfony/process) <  %{symfony_max_ver}
Requires:  php-composer(symfony/process) >= %{symfony_min_ver}
Requires:  php-composer(symfony/psr-http-message-bridge) <  %{symfony_psr_http_message_bridge_max_ver}
Requires:  php-composer(symfony/psr-http-message-bridge) >= %{symfony_psr_http_message_bridge_min_ver}
Requires:  php-composer(symfony/routing) <  %{symfony_max_ver}
Requires:  php-composer(symfony/routing) >= %{symfony_min_ver}
Requires:  php-composer(symfony/serializer) <  %{symfony_max_ver}
Requires:  php-composer(symfony/serializer) >= %{symfony_min_ver}
Requires:  php-composer(symfony/translation) <  %{symfony_max_ver}
Requires:  php-composer(symfony/translation) >= %{symfony_min_ver}
Requires:  php-composer(symfony/validator) <  %{symfony_max_ver}
Requires:  php-composer(symfony/validator) >= %{symfony_min_ver}
Requires:  php-composer(symfony/yaml) <  %{symfony_max_ver}
Requires:  php-composer(symfony/yaml) >= %{symfony_min_ver}
Requires:  php-composer(twig/twig) <  %{twig_max_ver}
Requires:  php-composer(twig/twig) >= %{twig_min_ver}
Requires:  php-composer(typo3/phar-stream-wrapper) <  %{typo3_phar_stream_wrapper_max_ver}
Requires:  php-composer(typo3/phar-stream-wrapper) >= %{typo3_phar_stream_wrapper_min_ver}
Requires:  php-pear(Archive_Tar) <  %{pear_archive_tar_max_ver}
Requires:  php-pear(Archive_Tar) >= %{pear_archive_tar_min_ver}
%endif
# phpcompatinfo (computed from version 8.4.5)
Requires:  php-bz2
Requires:  php-ctype
Requires:  php-curl
Requires:  php-ftp
Requires:  php-iconv
Requires:  php-intl
Requires:  php-libxml
Requires:  php-mbstring
Requires:  php-pdo_sqlite
Requires:  php-posix
Requires:  php-reflection
Requires:  php-zip
Requires:  php-zlib

# Weak dependencies
Suggests:  php-pecl(apcu)
Suggests:  php-pecl(yaml)

# Webserver
Requires:   %{name}-webserver = %{version}-%{release}
## Providers:
## - drupal8-httpd
## - FUTURE PLANNED: drupal8-nginx
Recommends: %{name}-httpd = %{version}-%{release}
#Suggests:   %%{name}-nginx = %%{version}-%%{release}

# core/composer.json: conflicts
Conflicts: php-composer(drush/drush) < 8.1.10

# Known conflict when Twig v2 is installed
#
# PHP Fatal error:  Class Drupal\Core\Template\Loader\StringLoader
# contains 1 abstract method and must therefore be declared abstract
# or implement the remaining methods (Twig_LoaderInterface::getSourceContext)
# in /usr/share/drupal8/core/lib/Drupal/Core/Template/Loader/StringLoader.php
# on line 23
#
# @todo Fix this conflict so Twig v2 is not autoloaded when installed
Conflicts: php-composer(twig/twig) >= %{twig_max_ver}

# drupal8(*) virtual provides
## Core
Provides:  drupal8(core) = %{version}
## Other
Provides:  drupal8(aaa_update_test) = %{version}
Provides:  drupal8(accept_header_routing_test) = %{version}
Provides:  drupal8(action_bulk_test) = %{version}
Provides:  drupal8(action_test) = %{version}
Provides:  drupal8(action) = %{version}
Provides:  drupal8(aggregator_display_configurable_test) = %{version}
Provides:  drupal8(aggregator_test) = %{version}
Provides:  drupal8(aggregator_test_views) = %{version}
Provides:  drupal8(aggregator) = %{version}
Provides:  drupal8(ajax_forms_test) = %{version}
Provides:  drupal8(ajax_test) = %{version}
Provides:  drupal8(automated_cron) = %{version}
Provides:  drupal8(ban) = %{version}
Provides:  drupal8(bartik) = %{version}
Provides:  drupal8(basic_auth_test) = %{version}
Provides:  drupal8(basic_auth) = %{version}
Provides:  drupal8(batch_test) = %{version}
Provides:  drupal8(bbb_update_test) = %{version}
Provides:  drupal8(big_pipe_regression_test) = %{version}
Provides:  drupal8(big_pipe_test_theme) = %{version}
Provides:  drupal8(big_pipe_test) = %{version}
Provides:  drupal8(big_pipe) = %{version}
Provides:  drupal8(block_content_test) = %{version}
Provides:  drupal8(block_content_test_views) = %{version}
Provides:  drupal8(block_content) = %{version}
Provides:  drupal8(block_test_specialchars_theme) = %{version}
Provides:  drupal8(block_test_theme) = %{version}
Provides:  drupal8(block_test) = %{version}
Provides:  drupal8(block_test_views) = %{version}
Provides:  drupal8(block) = %{version}
Provides:  drupal8(book_breadcrumb_test) = %{version}
Provides:  drupal8(book_test) = %{version}
Provides:  drupal8(book_test_views) = %{version}
Provides:  drupal8(book) = %{version}
Provides:  drupal8(breakpoint_module_test) = %{version}
Provides:  drupal8(breakpoint_theme_test) = %{version}
Provides:  drupal8(breakpoint) = %{version}
Provides:  drupal8(cache_test) = %{version}
Provides:  drupal8(ccc_update_test) = %{version}
Provides:  drupal8(ckeditor_test) = %{version}
Provides:  drupal8(ckeditor) = %{version}
Provides:  drupal8(claro) = %{version}
Provides:  drupal8(color_test_theme) = %{version}
Provides:  drupal8(color_test) = %{version}
Provides:  drupal8(color) = %{version}
Provides:  drupal8(comment_empty_title_test) = %{version}
Provides:  drupal8(comment_test) = %{version}
Provides:  drupal8(comment_test_views) = %{version}
Provides:  drupal8(comment) = %{version}
Provides:  drupal8(common_test_cron_helper) = %{version}
Provides:  drupal8(common_test) = %{version}
Provides:  drupal8(condition_test) = %{version}
Provides:  drupal8(config_clash_test_theme) = %{version}
Provides:  drupal8(config_collection_clash_install_test) = %{version}
Provides:  drupal8(config_collection_install_test) = %{version}
Provides:  drupal8(config_entity_static_cache_test) = %{version}
Provides:  drupal8(config_events_test) = %{version}
Provides:  drupal8(config_exclude_test) = %{version}
Provides:  drupal8(config_import_test) = %{version}
Provides:  drupal8(config_install_dependency_test) = %{version}
Provides:  drupal8(config_install_double_dependency_test) = %{version}
Provides:  drupal8(config_install_fail_test) = %{version}
Provides:  drupal8(config_integration_test) = %{version}
Provides:  drupal8(config_other_module_config_test) = %{version}
Provides:  drupal8(config_override_integration_test) = %{version}
Provides:  drupal8(config_override_test) = %{version}
Provides:  drupal8(config_test_id_mismatch) = %{version}
Provides:  drupal8(config_test_language) = %{version}
Provides:  drupal8(config_test_rest) = %{version}
Provides:  drupal8(config_test) = %{version}
Provides:  drupal8(config_transformer_test) = %{version}
Provides:  drupal8(config_translation_test_theme) = %{version}
Provides:  drupal8(config_translation_test) = %{version}
Provides:  drupal8(config_translation) = %{version}
Provides:  drupal8(config) = %{version}
Provides:  drupal8(conneg_test) = %{version}
Provides:  drupal8(contact_storage_test) = %{version}
Provides:  drupal8(contact_test) = %{version}
Provides:  drupal8(contact_test_views) = %{version}
Provides:  drupal8(contact) = %{version}
Provides:  drupal8(content_moderation_test_local_task) = %{version}
Provides:  drupal8(content_moderation_test_views) = %{version}
Provides:  drupal8(content_moderation) = %{version}
Provides:  drupal8(content_translation_test) = %{version}
Provides:  drupal8(content_translation_test_views) = %{version}
Provides:  drupal8(content_translation) = %{version}
Provides:  drupal8(contextual_test) = %{version}
Provides:  drupal8(contextual) = %{version}
Provides:  drupal8(cron_queue_test) = %{version}
Provides:  drupal8(csrf_race_test) = %{version}
Provides:  drupal8(csrf_test) = %{version}
Provides:  drupal8(css_disable_transitions_test) = %{version}
Provides:  drupal8(database_statement_monitoring_test) = %{version}
Provides:  drupal8(database_test) = %{version}
Provides:  drupal8(datetime_range_test) = %{version}
Provides:  drupal8(datetime_range) = %{version}
Provides:  drupal8(datetime_test) = %{version}
Provides:  drupal8(datetime) = %{version}
Provides:  drupal8(dblog_test_views) = %{version}
Provides:  drupal8(dblog) = %{version}
Provides:  drupal8(default_format_test) = %{version}
Provides:  drupal8(delay_cache_tags_invalidation) = %{version}
Provides:  drupal8(demo_umami) = %{version}
Provides:  drupal8(deprecation_test) = %{version}
Provides:  drupal8(dialog_renderer_test) = %{version}
Provides:  drupal8(display_variant_test) = %{version}
Provides:  drupal8(driver_test) = %{version}
Provides:  drupal8(drupal_system_cross_profile_test) = %{version}
Provides:  drupal8(drupal_system_listing_compatible_test) = %{version}
Provides:  drupal8(dynamic_page_cache_test) = %{version}
Provides:  drupal8(dynamic_page_cache) = %{version}
Provides:  drupal8(early_rendering_controller_test) = %{version}
Provides:  drupal8(early_translation_test) = %{version}
Provides:  drupal8(editor_private_test) = %{version}
Provides:  drupal8(editor_test) = %{version}
Provides:  drupal8(editor) = %{version}
Provides:  drupal8(element_info_test) = %{version}
Provides:  drupal8(entity_crud_hook_test) = %{version}
Provides:  drupal8(entity_reference_test) = %{version}
Provides:  drupal8(entity_reference_test_views) = %{version}
Provides:  drupal8(entity_schema_test) = %{version}
Provides:  drupal8(entity_serialization_test) = %{version}
Provides:  drupal8(entity_test_constraints) = %{version}
Provides:  drupal8(entity_test_extra) = %{version}
Provides:  drupal8(entity_test_operation) = %{version}
Provides:  drupal8(entity_test_revlog) = %{version}
Provides:  drupal8(entity_test_schema_converter) = %{version}
Provides:  drupal8(entity_test_third_party) = %{version}
Provides:  drupal8(entity_test_update) = %{version}
Provides:  drupal8(entity_test) = %{version}
Provides:  drupal8(error_service_test) = %{version}
Provides:  drupal8(error_test) = %{version}
Provides:  drupal8(experimental_module_dependency_test) = %{version}
Provides:  drupal8(experimental_module_requirements_test) = %{version}
Provides:  drupal8(experimental_module_test) = %{version}
Provides:  drupal8(experimental_theme_dependency_test) = %{version}
Provides:  drupal8(experimental_theme_test) = %{version}
Provides:  drupal8(field_discovery_test) = %{version}
Provides:  drupal8(field_layout_test) = %{version}
Provides:  drupal8(field_layout) = %{version}
Provides:  drupal8(field_normalization_test) = %{version}
Provides:  drupal8(field_plugins_test) = %{version}
Provides:  drupal8(field_test_boolean_access_denied) = %{version}
Provides:  drupal8(field_test_config) = %{version}
Provides:  drupal8(field_test) = %{version}
Provides:  drupal8(field_test_views) = %{version}
Provides:  drupal8(field_third_party_test) = %{version}
Provides:  drupal8(field_timestamp_test) = %{version}
Provides:  drupal8(field_ui_test) = %{version}
Provides:  drupal8(field_ui) = %{version}
Provides:  drupal8(field) = %{version}
Provides:  drupal8(file_module_test) = %{version}
Provides:  drupal8(file_test) = %{version}
Provides:  drupal8(file_test_views) = %{version}
Provides:  drupal8(file) = %{version}
Provides:  drupal8(filter_test_plugin) = %{version}
Provides:  drupal8(filter_test) = %{version}
Provides:  drupal8(filter) = %{version}
Provides:  drupal8(form_test) = %{version}
Provides:  drupal8(forum_test_views) = %{version}
Provides:  drupal8(forum) = %{version}
Provides:  drupal8(hal_test) = %{version}
Provides:  drupal8(hal) = %{version}
Provides:  drupal8(help_test) = %{version}
Provides:  drupal8(help_topics_test_theme) = %{version}
Provides:  drupal8(help_topics_test) = %{version}
Provides:  drupal8(help_topics) = %{version}
Provides:  drupal8(help) = %{version}
Provides:  drupal8(history) = %{version}
Provides:  drupal8(hold_test) = %{version}
Provides:  drupal8(httpkernel_test) = %{version}
Provides:  drupal8(image_access_test_hidden) = %{version}
Provides:  drupal8(image_module_test) = %{version}
Provides:  drupal8(image_test) = %{version}
Provides:  drupal8(image_test_views) = %{version}
Provides:  drupal8(image) = %{version}
Provides:  drupal8(inline_form_errors) = %{version}
Provides:  drupal8(invalid_module_name_over_the_maximum_allowed_character_length) = %{version}
Provides:  drupal8(js_ajax_test) = %{version}
Provides:  drupal8(js_cookie_test) = %{version}
Provides:  drupal8(js_deprecation_log_test) = %{version}
Provides:  drupal8(js_deprecation_test) = %{version}
Provides:  drupal8(js_message_test) = %{version}
Provides:  drupal8(jsonapi_test_collection_count) = %{version}
Provides:  drupal8(jsonapi_test_data_type) = %{version}
Provides:  drupal8(jsonapi_test_field_access) = %{version}
Provides:  drupal8(jsonapi_test_field_aliasing) = %{version}
Provides:  drupal8(jsonapi_test_field_filter_access) = %{version}
Provides:  drupal8(jsonapi_test_field_type) = %{version}
Provides:  drupal8(jsonapi_test_normalizers_kernel) = %{version}
Provides:  drupal8(jsonapi_test_resource_type_building) = %{version}
Provides:  drupal8(jsonapi_test_user) = %{version}
Provides:  drupal8(jsonapi) = %{version}
Provides:  drupal8(js_webassert_test) = %{version}
Provides:  drupal8(language_config_override_test) = %{version}
Provides:  drupal8(language_elements_test) = %{version}
Provides:  drupal8(language_entity_field_access_test) = %{version}
Provides:  drupal8(language_test) = %{version}
Provides:  drupal8(language) = %{version}
Provides:  drupal8(layout_builder_defaults_test) = %{version}
Provides:  drupal8(layout_builder_fieldblock_test) = %{version}
Provides:  drupal8(layout_builder_form_block_test) = %{version}
Provides:  drupal8(layout_builder_overrides_test) = %{version}
Provides:  drupal8(layout_builder_test) = %{version}
Provides:  drupal8(layout_builder_theme_suggestions_test) = %{version}
Provides:  drupal8(layout_builder) = %{version}
Provides:  drupal8(layout_builder_views_test) = %{version}
Provides:  drupal8(layout_discovery) = %{version}
Provides:  drupal8(layout_test) = %{version}
Provides:  drupal8(lazy_route_provider_install_test) = %{version}
Provides:  drupal8(link_generation_test) = %{version}
Provides:  drupal8(link_test_views) = %{version}
Provides:  drupal8(link) = %{version}
Provides:  drupal8(locale) = %{version}
Provides:  drupal8(mail_cancel_test) = %{version}
Provides:  drupal8(mail_html_test) = %{version}
Provides:  drupal8(media_library_test) = %{version}
Provides:  drupal8(media_library_test_widget) = %{version}
Provides:  drupal8(media_library) = %{version}
Provides:  drupal8(media_test_ckeditor) = %{version}
Provides:  drupal8(media_test_filter) = %{version}
Provides:  drupal8(media_test_oembed) = %{version}
Provides:  drupal8(media_test_source) = %{version}
Provides:  drupal8(media_test_type) = %{version}
Provides:  drupal8(media_test_views) = %{version}
Provides:  drupal8(media) = %{version}
Provides:  drupal8(menu_link_content) = %{version}
Provides:  drupal8(menu_test) = %{version}
Provides:  drupal8(menu_ui) = %{version}
Provides:  drupal8(migrate_cckfield_plugin_manager_test) = %{version}
Provides:  drupal8(migrate_drupal_ui) = %{version}
Provides:  drupal8(migrate_drupal) = %{version}
Provides:  drupal8(migrate_entity_test) = %{version}
Provides:  drupal8(migrate_events_test) = %{version}
Provides:  drupal8(migrate_external_translated_test) = %{version}
Provides:  drupal8(migrate_field_plugin_manager_test) = %{version}
Provides:  drupal8(migrate_high_water_test) = %{version}
Provides:  drupal8(migrate_lookup_test) = %{version}
Provides:  drupal8(migrate_no_migrate_drupal_test) = %{version}
Provides:  drupal8(migrate_overwrite_test) = %{version}
Provides:  drupal8(migrate_prepare_row_test) = %{version}
Provides:  drupal8(migrate_query_batch_test) = %{version}
Provides:  drupal8(migrate_state_finished_test) = %{version}
Provides:  drupal8(migrate_state_no_file_test) = %{version}
Provides:  drupal8(migrate_state_not_finished_test) = %{version}
Provides:  drupal8(migrate_state_no_upgrade_path) = %{version}
Provides:  drupal8(migrate_stub_test) = %{version}
Provides:  drupal8(migrate_track_changes_test) = %{version}
Provides:  drupal8(migrate) = %{version}
Provides:  drupal8(migration_directory_test) = %{version}
Provides:  drupal8(migration_provider_test) = %{version}
Provides:  drupal8(minimal) = %{version}
Provides:  drupal8(module_autoload_test) = %{version}
Provides:  drupal8(module_handler_test_no_hook) = %{version}
Provides:  drupal8(module_handler_test) = %{version}
Provides:  drupal8(module_install_class_loader_test1) = %{version}
Provides:  drupal8(module_install_class_loader_test2) = %{version}
Provides:  drupal8(module_installer_config_test) = %{version}
Provides:  drupal8(module_required_test) = %{version}
Provides:  drupal8(module_test) = %{version}
Provides:  drupal8(new_dependency_test) = %{version}
Provides:  drupal8(new_dependency_test_with_service) = %{version}
Provides:  drupal8(node_access_test_auto_bubbling) = %{version}
Provides:  drupal8(node_access_test_empty) = %{version}
Provides:  drupal8(node_access_test_language) = %{version}
Provides:  drupal8(node_access_test) = %{version}
Provides:  drupal8(node_display_configurable_test) = %{version}
Provides:  drupal8(node_test_config) = %{version}
Provides:  drupal8(node_test_exception) = %{version}
Provides:  drupal8(node_test) = %{version}
Provides:  drupal8(node_test_views) = %{version}
Provides:  drupal8(node) = %{version}
Provides:  drupal8(nyan_cat) = %{version}
Provides:  drupal8(off_canvas_test) = %{version}
Provides:  drupal8(options_config_install_test) = %{version}
Provides:  drupal8(options_test) = %{version}
Provides:  drupal8(options_test_views) = %{version}
Provides:  drupal8(options) = %{version}
Provides:  drupal8(page_cache_form_test) = %{version}
Provides:  drupal8(page_cache) = %{version}
Provides:  drupal8(pager_test) = %{version}
Provides:  drupal8(paramconverter_test) = %{version}
Provides:  drupal8(path_alias_deprecated_test) = %{version}
Provides:  drupal8(path_deprecated_test) = %{version}
Provides:  drupal8(path_encoded_test) = %{version}
Provides:  drupal8(path) = %{version}
Provides:  drupal8(phpunit_test) = %{version}
Provides:  drupal8(plugin_test_extended) = %{version}
Provides:  drupal8(plugin_test) = %{version}
Provides:  drupal8(quickedit_test) = %{version}
Provides:  drupal8(quickedit) = %{version}
Provides:  drupal8(rdf_conflicting_namespaces) = %{version}
Provides:  drupal8(rdf_test_namespaces) = %{version}
Provides:  drupal8(rdf_test) = %{version}
Provides:  drupal8(rdf) = %{version}
Provides:  drupal8(render_array_non_html_subscriber_test) = %{version}
Provides:  drupal8(render_attached_test) = %{version}
Provides:  drupal8(render_placeholder_message_test) = %{version}
Provides:  drupal8(requirements1_test) = %{version}
Provides:  drupal8(requirements2_test) = %{version}
Provides:  drupal8(responsive_image_test_module) = %{version}
Provides:  drupal8(responsive_image) = %{version}
Provides:  drupal8(rest_test) = %{version}
Provides:  drupal8(rest_test_views) = %{version}
Provides:  drupal8(rest) = %{version}
Provides:  drupal8(router_test) = %{version}
Provides:  drupal8(search_date_query_alter) = %{version}
Provides:  drupal8(search_embedded_form) = %{version}
Provides:  drupal8(search_extra_type) = %{version}
Provides:  drupal8(search_langcode_test) = %{version}
Provides:  drupal8(search_query_alter) = %{version}
Provides:  drupal8(search) = %{version}
Provides:  drupal8(serialization_test) = %{version}
Provides:  drupal8(serialization) = %{version}
Provides:  drupal8(service_provider_test) = %{version}
Provides:  drupal8(session_exists_cache_context_test) = %{version}
Provides:  drupal8(session_test) = %{version}
Provides:  drupal8(settings_tray_override_test) = %{version}
Provides:  drupal8(settings_tray_test_css) = %{version}
Provides:  drupal8(settings_tray_test) = %{version}
Provides:  drupal8(settings_tray) = %{version}
Provides:  drupal8(seven) = %{version}
Provides:  drupal8(shortcut) = %{version}
Provides:  drupal8(simpletest_deprecation_test) = %{version}
Provides:  drupal8(simpletest) = %{version}
Provides:  drupal8(standard) = %{version}
Provides:  drupal8(stark) = %{version}
Provides:  drupal8(statistics_test_attached) = %{version}
Provides:  drupal8(statistics_test_views) = %{version}
Provides:  drupal8(statistics) = %{version}
Provides:  drupal8(syslog_test) = %{version}
Provides:  drupal8(syslog) = %{version}
Provides:  drupal8(system_core_incompatible_semver_test) = %{version}
Provides:  drupal8(system_core_semver_test) = %{version}
Provides:  drupal8(system_dependencies_test) = %{version}
Provides:  drupal8(system_incompatible_core_version_dependencies_test) = %{version}
Provides:  drupal8(system_incompatible_core_version_test_1x) = %{version}
Provides:  drupal8(system_incompatible_core_version_test) = %{version}
Provides:  drupal8(system_incompatible_module_version_dependencies_test) = %{version}
Provides:  drupal8(system_incompatible_module_version_test) = %{version}
Provides:  drupal8(system_incompatible_php_version_test) = %{version}
Provides:  drupal8(system_mail_failure_test) = %{version}
Provides:  drupal8(system_module_test) = %{version}
Provides:  drupal8(system_project_namespace_test) = %{version}
Provides:  drupal8(system_test) = %{version}
Provides:  drupal8(system) = %{version}
Provides:  drupal8(tabledrag_test) = %{version}
Provides:  drupal8(taxonomy_crud) = %{version}
Provides:  drupal8(taxonomy_term_display_configurable_test) = %{version}
Provides:  drupal8(taxonomy_term_stub_test) = %{version}
Provides:  drupal8(taxonomy_test) = %{version}
Provides:  drupal8(taxonomy_test_views) = %{version}
Provides:  drupal8(taxonomy) = %{version}
Provides:  drupal8(telephone) = %{version}
Provides:  drupal8(test_another_module_required_by_theme) = %{version}
Provides:  drupal8(test_batch_test) = %{version}
Provides:  drupal8(test_ckeditor_stylesheets_external) = %{version}
Provides:  drupal8(test_ckeditor_stylesheets_protocol_relative) = %{version}
Provides:  drupal8(test_ckeditor_stylesheets_relative) = %{version}
Provides:  drupal8(test_core_semver) = %{version}
Provides:  drupal8(test_datatype_boolean_emoji_normalizer) = %{version}
Provides:  drupal8(test_fieldtype_boolean_emoji_normalizer) = %{version}
Provides:  drupal8(test_invalid_basetheme_sub) = %{version}
Provides:  drupal8(test_invalid_basetheme) = %{version}
Provides:  drupal8(test_invalid_core_semver) = %{version}
Provides:  drupal8(test_invalid_core) = %{version}
Provides:  drupal8(test_invalid_engine) = %{version}
Provides:  drupal8(test_invalid_region) = %{version}
Provides:  drupal8(test_layout_theme) = %{version}
Provides:  drupal8(test_legacy_stylesheets_remove) = %{version}
Provides:  drupal8(test_legacy_theme) = %{version}
Provides:  drupal8(test_messages) = %{version}
Provides:  drupal8(test_module_compatible_constraint) = %{version}
Provides:  drupal8(test_module_incompatible_constraint) = %{version}
Provides:  drupal8(test_module_required_by_theme) = %{version}
Provides:  drupal8(test_module) = %{version}
Provides:  drupal8(test_page_test) = %{version}
Provides:  drupal8(test_stable) = %{version}
Provides:  drupal8(test_subseven) = %{version}
Provides:  drupal8(test_subsubtheme) = %{version}
Provides:  drupal8(test_subtheme) = %{version}
Provides:  drupal8(test_theme_depending_on_constrained_modules) = %{version}
Provides:  drupal8(test_theme_depending_on_modules) = %{version}
Provides:  drupal8(test_theme_depending_on_nonexisting_module) = %{version}
Provides:  drupal8(test_theme_having_veery_long_name_which_is_too_long) = %{version}
Provides:  drupal8(test_theme_libraries_empty) = %{version}
Provides:  drupal8(test_theme_libraries_extend) = %{version}
Provides:  drupal8(test_theme_libraries_override_with_drupal_settings) = %{version}
Provides:  drupal8(test_theme_libraries_override_with_invalid_asset) = %{version}
Provides:  drupal8(test_theme_mixed_module_dependencies) = %{version}
Provides:  drupal8(test_theme_nyan_cat_engine) = %{version}
Provides:  drupal8(test_theme_settings_features) = %{version}
Provides:  drupal8(test_theme_settings) = %{version}
Provides:  drupal8(test_theme_theme) = %{version}
Provides:  drupal8(test_theme_twig_registry_loader_subtheme) = %{version}
Provides:  drupal8(test_theme_twig_registry_loader_theme) = %{version}
Provides:  drupal8(test_theme_twig_registry_loader) = %{version}
Provides:  drupal8(test_theme) = %{version}
Provides:  drupal8(test_theme_with_a_base_theme_depending_on_modules) = %{version}
Provides:  drupal8(test_wild_west) = %{version}
Provides:  drupal8(text) = %{version}
Provides:  drupal8(theme_legacy_suggestions_test) = %{version}
Provides:  drupal8(theme_legacy_test) = %{version}
Provides:  drupal8(theme_page_test) = %{version}
Provides:  drupal8(theme_region_test) = %{version}
Provides:  drupal8(theme_suggestions_test) = %{version}
Provides:  drupal8(theme_test) = %{version}
Provides:  drupal8(token_test) = %{version}
Provides:  drupal8(toolbar_disable_user_toolbar) = %{version}
Provides:  drupal8(toolbar_test) = %{version}
Provides:  drupal8(toolbar) = %{version}
Provides:  drupal8(tour_test) = %{version}
Provides:  drupal8(tour) = %{version}
Provides:  drupal8(tracker_test_views) = %{version}
Provides:  drupal8(tracker) = %{version}
Provides:  drupal8(trusted_hosts_test) = %{version}
Provides:  drupal8(twig_extension_test) = %{version}
Provides:  drupal8(twig_loader_test) = %{version}
Provides:  drupal8(twig_namespace_a) = %{version}
Provides:  drupal8(twig_namespace_b) = %{version}
Provides:  drupal8(twig_theme_test) = %{version}
Provides:  drupal8(twig) = %{version}
Provides:  drupal8(umami) = %{version}
Provides:  drupal8(unique_field_constraint_test) = %{version}
Provides:  drupal8(update_script_test) = %{version}
Provides:  drupal8(update_test_0) = %{version}
Provides:  drupal8(update_test_1) = %{version}
Provides:  drupal8(update_test_2) = %{version}
Provides:  drupal8(update_test_3) = %{version}
Provides:  drupal8(update_test_basetheme) = %{version}
Provides:  drupal8(update_test_failing) = %{version}
Provides:  drupal8(update_test_invalid_hook) = %{version}
Provides:  drupal8(update_test_last_removed) = %{version}
Provides:  drupal8(update_test_no_preexisting) = %{version}
Provides:  drupal8(update_test_postupdate) = %{version}
Provides:  drupal8(update_test_schema) = %{version}
Provides:  drupal8(update_test_semver_update_n) = %{version}
Provides:  drupal8(update_test_subtheme) = %{version}
Provides:  drupal8(update_test) = %{version}
Provides:  drupal8(update_test_with_7x) = %{version}
Provides:  drupal8(update) = %{version}
Provides:  drupal8(url_alter_test) = %{version}
Provides:  drupal8(user_access_test) = %{version}
Provides:  drupal8(user_batch_action_test) = %{version}
Provides:  drupal8(user_custom_phpass_params_test) = %{version}
Provides:  drupal8(user_form_test) = %{version}
Provides:  drupal8(user_hooks_test) = %{version}
Provides:  drupal8(user_test_theme) = %{version}
Provides:  drupal8(user_test_views) = %{version}
Provides:  drupal8(user) = %{version}
Provides:  drupal8(views_entity_test) = %{version}
Provides:  drupal8(views_test_cacheable_metadata_calculation) = %{version}
Provides:  drupal8(views_test_checkboxes_theme) = %{version}
Provides:  drupal8(views_test_classy_subtheme) = %{version}
Provides:  drupal8(views_test_config) = %{version}
Provides:  drupal8(views_test_data) = %{version}
Provides:  drupal8(views_test_formatter) = %{version}
Provides:  drupal8(views_test_language) = %{version}
Provides:  drupal8(views_test_modal) = %{version}
Provides:  drupal8(views_test_query_access) = %{version}
Provides:  drupal8(views_test_rss) = %{version}
Provides:  drupal8(views_test_theme) = %{version}
Provides:  drupal8(views_ui_test_field) = %{version}
Provides:  drupal8(views_ui_test) = %{version}
Provides:  drupal8(views_ui) = %{version}
Provides:  drupal8(views) = %{version}
Provides:  drupal8(vocabulary_serialization_test) = %{version}
Provides:  drupal8(workflows) = %{version}
Provides:  drupal8(workflow_third_party_settings_test) = %{version}
Provides:  drupal8(workflow_type_test) = %{version}
Provides:  drupal8(workspace_access_test) = %{version}
Provides:  drupal8(workspaces) = %{version}
Provides:  drupal8(workspace_update_test) = %{version}

# php-composer(*) virtual provides
## composer.json
Provides:  php-composer(packages.drupal.org/drupal/drupal) = %{version}
## **/composer.json
Provides:  php-composer(packages.drupal.org/drupal/action) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/aggregator) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/automated_cron) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/ban) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/bartik) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/basic_auth) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/big_pipe) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/block_content) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/block_place) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/block) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/book) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/breakpoint) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/ckeditor) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/claro) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/classy) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/color) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/comment) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/config_translation) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/config) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/contact) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/content_moderation) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/content_translation) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/contextual) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/core-annotation) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/core-assertion) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/core-bridge) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/core-class-finder) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/core-datetime) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/core-dependency-injection) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/core-diff) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/core-discovery) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/core-event-dispatcher) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/core-file-cache) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/core-file-security) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/core-filesystem) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/core-gettext) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/core-graph) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/core-http-foundation) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/core-php-storage) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/core-plugin) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/core-proxy-builder) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/core-render) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/core-serialization) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/core-transliteration) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/core-utility) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/core-uuid) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/core-version) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/core) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/datetime_range) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/datetime) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/dblog) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/dynamic_page_cache) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/editor) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/entity_reference) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/field_layout) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/field_ui) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/field) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/file) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/filter) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/forum) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/hal) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/help_topics) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/help) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/history) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/image) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/inline_form_errors) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/jsonapi) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/language) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/layout_builder) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/layout_discovery) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/legacy-project) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/link) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/locale) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/media_library) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/media) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/menu_link_content) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/menu_ui) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/migrate_drupal_multilingual) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/migrate_drupal_ui) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/migrate_drupal) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/migrate) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/minimal) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/node) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/options) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/page_cache) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/path_alias) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/path) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/quickedit) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/rdf) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/responsive_image) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/rest) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/search) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/serialization) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/settings_tray) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/seven) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/shortcut) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/simpletest) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/standard) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/stark) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/statistics) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/syslog) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/system) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/taxonomy) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/telephone) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/text) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/toolbar) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/tour) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/tracker) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/update) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/user) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/views_ui) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/views) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/workflows) = %{version}
Provides:  php-composer(packages.drupal.org/drupal/workspaces) = %{version}
Provides:  php-composer(packages.drupal.org/fixtures/drupal-assets-fixture) = %{version}
Provides:  php-composer(packages.drupal.org/fixtures/drupal-core-fixture) = %{version}
Provides:  php-composer(packages.drupal.org/fixtures/empty-fixture-allowing-core) = %{version}
Provides:  php-composer(packages.drupal.org/fixtures/empty-fixture) = %{version}
Provides:  php-composer(packages.drupal.org/fixtures/project-with-empty-scaffold-path) = %{version}
Provides:  php-composer(packages.drupal.org/fixtures/project-with-illegal-dir-scaffold) = %{version}
Provides:  php-composer(packages.drupal.org/fixtures/scaffold-override-fixture) = %{version}

# Bundled
## core/core.libraries.yml
### core/assets/vendor/backbone
###     License:  MIT
###     Upstream: https://github.com/jashkenas/backbone
Provides:  bundled(js-backbone) = 1.4.0
### core/assets/vendor/ckeditor
###     License:  GPLv2+
###     Upstream: https://github.com/ckeditor/ckeditor-dev
Provides:  bundled(ckeditor) = 4.14.0
### core/assets/vendor/classList
###     License:  Public Domain
###     Upstream: https://github.com/eligrey/classList.js
Provides:  bundled(js-classList) = 2014_12_13
### core/assets/vendor/js-cookie
###     License:  MIT
###     Upstream: https://github.com/js-cookie/js-cookie
Provides:  bundled(js-cookie) = 3.0.0-rc0
### core/assets/vendor/domready
###     License:  MIT
###     Upstream: https://github.com/ded/domready
Provides:  bundled(js-domready) = 1.0.8
### core/assets/vendor/farbtastic
###     License:  GPLv2+
###     Upstream: https://github.com/mattfarina/farbtastic
Provides:  bundled(js-farbtastic) = 1.2
### core/assets/vendor/html5shiv
###     License:  GPLv2+
###     Upstream: https://github.com/aFarkas/html5shiv
Provides:  bundled(js-html5shiv) = 3.7.3
### core/assets/vendor/jquery
###     License:  MIT
###     Upstream: https://github.com/jquery/jquery
Provides:  bundled(js-jquery) = 3.5.1
### core/assets/vendor/jquery.cookie
###     License:  MIT
###     Upstream: https://github.com/carhartl/jquery-cookie
Provides:  bundled(js-jquery-cookie) = 1.4.1
### core/assets/vendor/jquery-form
###     License:  GPLv2+
###     Upstream: https://github.com/jquery-form/form
Provides:  bundled(js-jquery-form) = 4.22
### core/assets/vendor/jquery-joyride
###     License:  MIT
###     Upstream: https://github.com/zurb/joyride
Provides:  bundled(js-jquery-joyride) = 2.1.0.1
### core/assets/vendor/jquery-once
###     License:  GPLv2+
###     Upstream: https://github.com/RobLoach/jquery-once
Provides:  bundled(js-jquery-once) = 2.2.3
### core/assets/vendor/jquery.ui
###     License:  Public Domain
###     Upstream: https://github.com/jquery/jquery-ui
Provides:  bundled(js-jquery-ui) = 1.12.1
### core/assets/vendor/jquery-ui-touch-punch
###     License:  GPLv2+
###     Upstream: https://github.com/furf/jquery-ui-touch-punch
Provides:  bundled(js-jquery-ui-touch-punch) = 0.2.3
### core/assets/vendor/matchMedia
###     License:  MIT
###     Upstream: https://github.com/paulirish/matchMedia.js
Provides:  bundled(js-matchMedia) = 0.2.0
### core/assets/vendor/modernizr
###     License:  MIT
###     Upstream: https://github.com/Modernizr/Modernizr
Provides:  bundled(js-modernizr) = 3.3.1
### core/assets/vendor/normalize-css
###     License:  MIT
###     Upstream: https://github.com/necolas/normalize.css
Provides:  bundled(css-normalize) = 3.0.3
### core/assets/vendor/picturefill
###     License:  MIT
###     Upstream: https://github.com/scottjehl/picturefill
Provides:  bundled(js-picturefill) = 3.0.3
### core/assets/vendor/popperjs
###     License: MIT
###     Upstream: https://github.com/popperjs/popper.js
Provides:  bundled(js-popperjs) = 1.16.0
### core/assets/vendor/sortable
###     License: MIT
###     Upstream: https://github.com/SortableJS/Sortable
Provides:  bundled(js-sortable) = 1.10.2
### core/assets/vendor/underscore
###     License:  MIT
###     Upstream: https://github.com/jashkenas/underscore
Provides:  bundled(js-underscore) = 1.9.1


%description
Drupal is an open source content management platform powering millions of
websites and applications. It’s built, used, and supported by an active and
diverse community of people around the world.

#-------------------------------------------------------------------------------

%package httpd

Summary:    HTTPD integration for %{name}

Requires:   %{name} = %{version}-%{release}
Requires:   httpd
Requires:   httpd-filesystem
Requires:   php(httpd)
# php(httpd) providers
Recommends: mod_php
Suggests:   php-fpm

Provides:   %{name}-webserver = %{version}-%{release}

%description httpd
%{summary}.

#-------------------------------------------------------------------------------

%package rpmbuild

Summary:  RPM build files for %{name}

License:  MIT

Requires: php-cli
Requires: php(language) >= 5.4.0
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires: (php-composer(symfony/console) >= %{symfony_min_ver} with php-composer(symfony/console) < %{symfony_max_ver})
Requires: (php-composer(symfony/yaml) >= %{symfony_min_ver} with php-composer(symfony/yaml) < %{symfony_max_ver})
%else
Requires: php-composer(symfony/console) >= %{symfony_min_ver}
Requires: php-composer(symfony/console) <  %{symfony_max_ver}
Requires: php-composer(symfony/yaml) >= %{symfony_min_ver}
Requires: php-composer(symfony/yaml) <  %{symfony_max_ver}
%endif

%description rpmbuild
%{summary}.

#-------------------------------------------------------------------------------

%prep
%setup -qn drupal-%{version}

: Copy other sources into build dir
mkdir .rpm
cp -p %{SOURCE1} .rpm/
cp -p %{SOURCE2} .rpm/
cp -p %{SOURCE3} .rpm/
cp -p %{SOURCE4} .rpm/
cp -p %{SOURCE5} .rpm/
cp -p %{SOURCE6} .rpm/
cp -p %{SOURCE7} .rpm/
cp -p %{SOURCE8} .rpm/
cp -p %{SOURCE9} .rpm/
cp -p %{SOURCE10} .rpm/

: Update dynamic values in sources
sed \
    -e 's:__DRUPAL8_CORE_VERSION__:%{version}:' \
    -e 's:__DRUPAL8_PHP_MIN_VER__:%{php_min_ver}:' \
    -e 's:__DRUPAL8__:%{drupal8}:' \
    -e 's:__DRUPAL8_VAR__:%{drupal8_var}:' \
    -e 's:__DRUPAL8_CONF__:%{drupal8_conf}:' \
    -e 's:__PEARDIR__:%{pear_phpdir}:' \
    -e 's:__PHPDIR__:%{phpdir}:' \
    -e 's:__SPEC_VERSION__:%{version}:' \
    -e 's:__SPEC_RELEASE__:%{release}:' \
    -e 's:__ETC__:%{_sysconfdir}:' \
    -e 's:__DOC__:%{_docdir}:' \
    -i .rpm/*

: Remove unneeded files
rm -rf vendor core/vendor
find . -name '.git*' -delete -print
find . -name 'web.config' -delete -print

: Autoloader
mv autoload.php autoload.php.dist
cp .rpm/%{name}-autoload.php autoload.php

: Licenses and docs
.rpm/%{name}-prep-licenses-and-docs.sh
mv core/INSTALL.*.* .rpm/docs/core/

: Move license and doc files required at runtime back in place
mv .rpm/docs/core/modules/system/tests/fixtures/HtaccessTest/composer.* \
    core/modules/system/tests/fixtures/HtaccessTest/
rmdir .rpm/docs/core/modules/system/tests/fixtures/HtaccessTest
rmdir .rpm/docs/core/modules/system/tests/fixtures
cp .rpm/docs/core/INSTALL.txt core/

: Remove all empty license and doc files
find .rpm/{licenses,docs}/ -type f -size 0 -delete -print

: RPM README
cp .rpm/%(basename %{SOURCE1}) .rpm/docs/README.fedora.md

: rpmbuild subpackage license
mkdir -p .rpm/rpmbuild
cp .rpm/%(basename %{SOURCE2}) .rpm/rpmbuild/LICENSE.txt

: Apache .htaccess
sed 's!# RewriteBase /$!# RewriteBase /\n  RewriteBase /drupal8!' \
    -i .htaccess

: Update php bin
sed 's#/bin/php#%{_bindir}/php#' \
    -i core/scripts/update-countries.sh

# TODO: Update phpunit bin
# core/modules/simpletest/simpletest.module:simpletest_phpunit_command()

: Fix "non-executable-script" rpmlint errors
chmod +x core/scripts/*.{php,sh}

: Fix "script-without-shebang" rpmlint errors
chmod -x core/scripts/run-tests.sh

#-------------------------------------------------------------------------------

%build
: Autoloader
pushd core
    : Create Composer autoloader
    cp ../.rpm/docs/core/composer.json .
    %{_bindir}/composer dump-autoload --optimize

    : Remove unneeded files
    rm -f composer.json vendor/web.config

    : Move autoloader license to licenses
    mkdir -p ../.rpm/licenses/core/vendor/composer
    mv vendor/composer/LICENSE ../.rpm/licenses/core/vendor/composer/
popd

: Upstream managed httpd config files
cat <<'HEADER' > .rpm/%{name}-managed-conf-header
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# This file is managed by the %{name} RPM to ensure it is automatically updated
# when there are changes instead of creating a *.rpmnew file and administrators
# having to manually update this file.
#
# Any changes to this file will be overwritten.  If you would like to make
# changes to this file, copy it to a new file name and modify the %{name}.conf
# file to load your custom file instead of this one.  Note that you will then
# have to ensure you manually modify your custom file with upstream changes
# including upstream security fixes.
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

HEADER
cat .rpm/%{name}-managed-conf-header .htaccess | tee .rpm/%{name}.htaccess
cat .rpm/%{name}-managed-conf-header core/vendor/.htaccess | tee .rpm/%{name}.deny-access

#-------------------------------------------------------------------------------

%install
: Main
mkdir -p %{buildroot}%{drupal8}
cp -pr * %{buildroot}%{drupal8}/

: Sites
mkdir -p %{buildroot}%{drupal8_conf}/sites
mv %{buildroot}%{drupal8}/sites/* %{buildroot}%{drupal8_conf}/sites/
rmdir %{buildroot}%{drupal8}/sites
ln -s %{drupal8_conf}/sites %{buildroot}%{drupal8}/sites

: Files
mkdir -p %{buildroot}%{drupal8_var}/files/{public,private}/default
ln -s %{drupal8_var}/files/public/default \
    %{buildroot}%{drupal8_conf}/sites/default/files

: rpmbuild
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
install -pm 0644 .rpm/macros.%{name} %{buildroot}%{_rpmconfigdir}/macros.d/
mkdir -p %{buildroot}%{_rpmconfigdir}/fileattrs
install -pm 0644 .rpm/%{name}.attr %{buildroot}%{_rpmconfigdir}/fileattrs/
install -pm 0755 .rpm/%{name}-find-provides.php %{buildroot}%{_rpmconfigdir}/
install -pm 0755 .rpm/%{name}-find-requires.php %{buildroot}%{_rpmconfigdir}/
install -pm 0755 .rpm/%{name}-get-dev-source.sh %{buildroot}%{_rpmconfigdir}/
install -pm 0755 .rpm/%{name}-prep-licenses-and-docs.sh %{buildroot}%{_rpmconfigdir}/

: Apache HTTPD conf files
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
install -pm 0644 .rpm/%{name}.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/
install -pm 0644 .rpm/%{name}.htaccess %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.htaccess
install -pm 0644 .rpm/%{name}.deny-access %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.deny-access

#-------------------------------------------------------------------------------

%check
: Version check
%{_bindir}/php -r '
    require_once "%{buildroot}%{drupal8}/core/lib/Drupal.php";
    $version = \Drupal::VERSION;
    echo "Version $version (expected %{version})\n";
    exit(version_compare("%{version}", "$version", "=") ? 0 : 1);
'

: Ensure RewriteBase in HTTPD config
grep \
    'RewriteBase /drupal8' \
        %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.htaccess \
        --quiet \
    || exit 1

: Ensure php bin updated
grep -r '#!/bin/php' . && exit 1

%if %{with_tests}
pushd core
    : Unit tests
    %{_bindir}/phpunit
popd
%else
: Test suite skipped
%endif

#-------------------------------------------------------------------------------

%files
%license .rpm/licenses/*
%doc .rpm/docs/*
%{drupal8}
%exclude %{drupal8}/core/vendor/.htaccess
# Sites
%dir               %{drupal8_conf}
%dir               %{drupal8_conf}/sites
%config(noreplace) %{drupal8_conf}/sites/development.services.yml
%dir               %{drupal8_conf}/sites/default
## Managed upstream example/default configs
%config            %{drupal8_conf}/sites/example.*
%config            %{drupal8_conf}/sites/default/default.*
# Files
%{drupal8_conf}/sites/default/files
%dir %{drupal8_var}
%dir %{drupal8_var}/files
%dir %{drupal8_var}/files/private
%dir %{drupal8_var}/files/public

#-------------------------------------------------------------------------------

%files httpd
# Configs
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
## Managed upstream configs
%config            %{_sysconfdir}/httpd/conf.d/%{name}.htaccess
%config            %{_sysconfdir}/httpd/conf.d/%{name}.deny-access
# Files
%dir %attr(0775,root,apache) %{drupal8_var}/files/private/default
%dir %attr(0775,root,apache) %{drupal8_var}/files/public/default

#-------------------------------------------------------------------------------

%files rpmbuild
%license .rpm/rpmbuild/LICENSE.txt
%{_rpmconfigdir}/fileattrs/%{name}.attr
%{_rpmconfigdir}/macros.d/macros.%{name}
%{_rpmconfigdir}/%{name}-find-provides.php
%{_rpmconfigdir}/%{name}-find-requires.php
%{_rpmconfigdir}/%{name}-get-dev-source.sh
%{_rpmconfigdir}/%{name}-prep-licenses-and-docs.sh

#-------------------------------------------------------------------------------

%changelog
* Sat Jun 06 2020 Shawn Iwinski <shawn@iwin.ski> - 8.9.0-1
- Update to 8.9.0
- https://www.drupal.org/sa-core-2020-002 / CVE-2020-11022 / CVE-2020-11023
- Fix FTI by removing php-recode dependency (RHBZ #1832048, 1833939)

* Sun Apr 05 2020 Shawn Iwinski <shawn@iwin.ski> - 8.8.5-1
- Update to 8.8.5 (RHBZ #1817768)

* Mon Mar 23 2020 Shawn Iwinski <shawn@iwin.ski> - 8.8.4-1
- Update to 8.8.4 (RHBZ #1705226)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Shawn Iwinski <shawn@iwin.ski> - 8.6.17-1
- Update to 8.6.17

* Fri May 10 2019 Shawn Iwinski <shawn@iwin.ski> - 8.6.16-1
- Update to 8.6.16
- https://www.drupal.org/SA-CORE-2019-007

* Mon Apr 29 2019 Shawn Iwinski <shawn@iwin.ski> - 8.6.15-1
- Update to 8.6.15 (RHBZ #1697173)
- https://www.drupal.org/SA-CORE-2019-005 (CVE-2019-10909 / CVE-2019-10910 / CVE-2019-10911)
- https://www.drupal.org/SA-CORE-2019-006 (CVE-2019-11358)

* Wed Mar 20 2019 Shawn Iwinski <shawn@iwin.ski> - 8.6.13-1
- Update to 8.6.13 (RHBZ #1688520)
- https://www.drupal.org/SA-CORE-2019-004

* Tue Feb 26 2019 Shawn Iwinski <shawn@iwin.ski> - 8.6.10-1
- Update to 8.6.10 (RHBZ #1673117)
- https://www.drupal.org/SA-CORE-2019-001
- https://www.drupal.org/SA-CORE-2019-002
- https://www.drupal.org/SA-CORE-2019-003
- Fix autoloader (RHBZ #1662604)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Shawn Iwinski <shawn@iwin.ski> - 8.6.2-1
- Update to 8.6.2 (RHBZ #1498687 / RHBZ #1643121 / RHBZ #1643123 / SA-CORE-2018-006)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 25 2018 Shawn Iwinski <shawn@iwin.ski> - 8.4.8-1
- Update to 8.4.8 (RHBZ #1572099 / RHBZ #1572101 / SA-CORE-2018-004 /
  CVE-2018-7602 / SA-CORE-2018-003 / CVE-2018-9861)
- Add composer.json files to repo
- Fix "rpmbuild" subpackage by adding range version dependencies for
  Fedora >= 27 || RHEL >= 8

* Mon Apr 09 2018 Shawn Iwinski <shawn@iwin.ski> - 8.4.6-3
- Add range version dependencies for Fedora >= 27 || RHEL >= 8
- Add php-composer(symfony/config) dependency

* Sat Mar 31 2018 Shawn Iwinski <shawn@iwin.ski> - 8.4.6-2
- Fix autoload of symfony/psr-http-message-bridge and symfony-cmf/routing
- Add conflict when Twig v2 is installed

* Wed Mar 28 2018 Shawn Iwinski <shawn@iwin.ski> - 8.4.6-1
- Update to 8.4.6 (SA-CORE-2018-002 / CVE-2018-7600)
- Make scripts' dependencies match Drupal Symfony version constraints

* Wed Mar 14 2018 Shawn Iwinski <shawn@iwin.ski> - 8.4.5-1
- Update to 8.4.5 (RHBZ #1548187 / RHBZ #1548188 / RHBZ #1548189 /
  RHBZ #1548192 / RHBZ #1548323 / RHBZ #1548325 / SA-CORE-2018-001 /
  CVE-2017-6926 / CVE-2017-6927 / CVE-2017-6930 / CVE-2017-6931)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 17 2017 Shawn Iwinski <shawn@iwin.ski> - 8.3.7-1
- Update to 8.3.7 (RHBZ #1482277 / SA-CORE-2017-004 / CVE-2017-6923 /
  CVE-2017-6924 / CVE-2017-6925)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Shawn Iwinski <shawn@iwin.ski> - 8.3.5-1
- Update to 8.3.5 (RHBZ #1468059)

* Thu Jun 22 2017 Shawn Iwinski <shawn@iwin.ski> - 8.3.4-1
- Update to 8.3.4 (RHBZ #1459711 / SA-CORE-2017-003 / CVE-2017-6920 /
  CVE-2017-6921 / CVE-2017-6922)

* Thu May 11 2017 Shawn Iwinski <shawn@iwin.ski> - 8.3.2-1
- Update to 8.3.2 (RHBZ #1447814)
- Add conflict: php-composer(drush/drush) < 8.1.10

* Thu Apr 20 2017 Shawn Iwinski <shawn@iwin.ski> - 8.3.1-1
- Update to 8.3.1 (SA-CORE-2017-002, RHBZ #1443782)

* Sat Apr 15 2017 Shawn Iwinski <shawn@iwin.ski> - 8.3.0-1
- Update to 8.3.0 (RHBZ #1439698)
- Update php-composer(*) Drupal-provides to php-composer(packages.drupal.org/*)
- Change Drupal-requires from drupal8(*) to php-composer(packages.drupal.org/*)

* Wed Mar 15 2017 Shawn Iwinski <shawn@iwin.ski> - 8.2.7-1
- Update to 8.2.7 (SA-CORE-2017-001)

* Tue Feb 28 2017 Shawn Iwinski <shawn@iwin.ski> - 8.2.6-1
- Update to 8.2.6 (RHBZ #1418483)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Shawn Iwinski <shawn@iwin.ski> - 8.2.5-1
- Update to 8.2.5 (RHBZ #1410077)

* Mon Dec 26 2016 Shawn Iwinski <shawn@iwin.ski> - 8.2.4-2
- Add missing php-composer(asm89/stack-cors) dependency (RHBZ #1408675)

* Sun Dec 11 2016 Shawn Iwinski <shawn@iwin.ski> - 8.2.4-1
- Update to 8.2.4 (RHBZ #1402613)

* Thu Nov 17 2016 Shawn Iwinski <shawn@iwin.ski> - 8.2.3-1
- Update to 8.2.3 (RHBZ #1395919 / SA-CORE-2016-005)
- Update %%__drupal8_path (RPM fileattrs) to only include drupal8* doc paths

* Thu Nov 03 2016 Shawn Iwinski <shawn@iwin.ski> - 8.2.2-2
- Add RPM README
- Rename HTTPD config file "drupal8.no-access" to "drupal8.deny-access"

* Thu Nov 03 2016 Shawn Iwinski <shawn@iwin.ski> - 8.2.2-1
- Update to 8.2.2 (RHBZ #1383483)
- Update license from "GPLv2+ and MIT and Public Domain and (GPLv2+ or MPLv1.1+ or LGPLv2.1+)"
  to "GPLv2+ and MIT and Public Domain and (GPLv2+ or MPLv1.1+ or LGPLv2+)"

* Fri Aug 05 2016 Shawn Iwinski <shawn@iwin.ski> - 8.1.8-2
- Update license from "GPLv2+ or MPLv1.1+ or LGPLv2.1+" to
  "GPLv2+ and MIT and Public Domain and (GPLv2+ or MPLv1.1+ or LGPLv2.1+)"
- Add LICENSE file to rpmbuild subpackage
- Add missing "php-cli" dependency (for "/usr/bin/env php" usage)
- Move license and doc files required at runtime back in place
- Remove all empty license and doc files
- Add header to managed httpd conf files

* Thu Aug 04 2016 Shawn Iwinski <shawn@iwin.ski> - 8.1.8-1
- Update to 8.1.8
- Fix drupal8(*) virtual provides:
-- drupal8(drupal/*) => drupal8(*)
-- Only *.info.yml (instead of all composer names)

* Mon Jul 18 2016 Shawn Iwinski <shawn@iwin.ski> - 8.1.7-1
- Update to 8.1.7

* Wed Jul 13 2016 Shawn Iwinski <shawn@iwin.ski> - 8.1.6-1
- Update to 8.1.6
- Rewrite top-level autoload.php instead of modifying core's composer.json
- Fix drupal8-get-dev-source.sh she-bang
- No "rpm" subdirectory for %%drupal8_{modules,profiles,themes} macros
- Include main .htaccess in httpd conf instead of soft-linking
- Apache conf for no access
- %%files %%config updates
- httpd subpackage now owns %%{drupal8_var}/files/{public,private}/default
  because of %%attr

* Thu Mar 10 2016 Shawn Iwinski <shawn@iwin.ski> - 8.0.5-1
- Update to 8.0.5

* Sun Jan 31 2016 Shawn Iwinski <shawn@iwin.ski> - 8.0.2-3
- Fix build requires and %%check in clean buildroot

* Sun Jan 31 2016 Shawn Iwinski <shawn@iwin.ski> - 8.0.2-2
- Fix typo in drupal8-prep-licenses-and-docs.sh
- Fix finding of composer.json files in drupal8.attr
- Update automatic provides and requires for single file input and
  ignore directories
- Remove "--spec-name" option from automatic requires
- Fix automatic provides version when version = 0
- %%{name}-prep-licenses-and-docs.sh usage in %%prep

* Tue Jan 26 2016 Shawn Iwinski <shawn@iwin.ski> - 8.0.2-1
- Updated to 8.0.2
- Main package license changed from "GPLv2+" to "GPLv2+ and MIT and Public Domain"
- "rpmbuild" sub-package "MIT" license added
- Dynamic %%doc and %%license
- Modified drupal8(*) virtual provides
- Added php-composer(*) virtual provides
- Added custom autoloader (and removed Composer autoload modifications)
- Added "drupal8_var" and "drupal8_conf" macros
- "%%{_sysconfdir}/%%{name}/*" => "%%{_sysconfdir}/%%{name}/sites/*"
- "%%{_localstatedir}/lib/%%{name}/*" => "%%{_localstatedir}/lib/%%{name}/files/*"
- Separation of HTTPD web server configs into sub-package (%%{name}-httpd)
- Added version check in %%check
- Removed filesystem modifications in %%check

* Sat Oct 10 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0.0-0.14.rc1
- Updated to 8.0.0-rc1

* Sat Nov 22 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0.0-0.13.beta3
- Updated to 8.0.0-beta3

* Wed Jul 02 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.12.alpha13
- Updated to 8.0-alpha13

* Sun Jun 29 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.11.alpha12
- Updated to 8.0-alpha12

* Fri May 23 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.10.alpha11
- Updated to 8.0-alpha11
- Many more changes...

* Sun Jan 12 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.9.alpha7
- Updated to release tag 8.0-alpha7
- Updated URL
- Moved .htaccess file to Apache conf dir
- Fixed Apache conf file
- Removed PSR Log dependency (dependencies pull this in)
- Unbundle EasyRDF, Gliph, Symfony, Zend Framework 2 Feed
- Added specific file requires to make sure broken dependency if providing
  pkg moves file
- Keep modules, profiles, and themes README files in directories
- Unbundling now uses autoloader instead of symlinks

* Wed Oct 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.8.alpha4
- Updated to release tag 8.0-alpha4
- Require correct min PHP version 5.3.10 instead of 5.3.3
- Require correct min/max pkg versions
- Use bundled Doctrine, EasyRdf, Symfony, Symfony CMF Routing, and Twig
  because required versions are not available in Fedora
- Updated phpcompatinfo requires:
  Added: openssl, tokenizer
  Removed: bcmath, gmp

* Sun Jun 16 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.7.20130616git1648a47
- Updated to 2013-06-16 snapshot
- No auto-provide hidden projects
- Static virtual provides instead of dynamic

* Wed Jun 12 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.6.20130612gite952a21
- Updated to 2013-06-12 snapshot

* Sun May 05 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.5.20130504git5838ea9
- Updated to 2013-05-04 snapshot

* Thu Apr 04 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.4.20130403giteebd063
- Updated to 2013-04-03 snapshot
- Updated note about PHP minimum version
- Added php-Assetic and php-SymfonyCmfRouting requires
- Removed vendors (bundled libraries) phpci requires
- Updated composer file locations

* Thu Mar 21 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.3.20130309git3210003
- %%{drupal8}/sites => %%{_sysconfdir}/%%{name}
- Marked Apache config as %%config
- Marked modules/profiles/themes README.txt as %%doc
- Specific dir and file ownership
- Removed example.gitignore
- Added files dir and symlink

* Sat Mar 09 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.2.20130309git3210003
- Updated to latest 2013-03-09 snapshot
- *.info => *.info.yml
- Added PyYAML require for rpmbuild sub-package
- Un-bundled PHPUnit

* Mon Feb 25 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.1.20130224git8afbc08
- Initial package
